# iven the root of a binary tree, return its bottom view from left to right.

# The bottom view contains the nodes visible when the tree is observed from below. For every vertical position, the deepest node on that vertical line is visible.

# To identify vertical positions, a horizontal distance (hd) is assigned to every node. It represents the horizontal position of a node relative to the root:

# The root has hd = 0.

# The left child has hd = parentHD - 1.

# The right child has hd = parentHD + 1.

# If multiple nodes lie at the same horizontal distance and depth, the node encountered later in level-order traversal is considered visible.

# The visible node values must be returned from the smallest horizontal distance to the largest.

# Example 1
# Input: root = [1, 2, 3, 4, 5, 6, 7]

# Output: [4, 2, 6, 3, 7]

# Explanation: The deepest visible nodes from the leftmost to the rightmost vertical line are 4, 2, 6, 3, 7. Nodes 1 and 5 are hidden by deeper nodes lying on the same vertical positions.

# Example 2
# Input: root = [20, 8, 22, 5, 3, null, 25, null, null, 10, 14]

# Output: [5, 10, 3, 14, 25]

# Explanation: For each horizontal distance, the deepest node is selected. Therefore, the bottom view from left to right is 5, 10, 3, 14, 25.

# rute Force Approach
# Nodes having the same horizontal distance (hd) belong to the same vertical line. Here, hd is used to identify which nodes compete for the same position in the bottom view.

# For each vertical line, the node having the greatest depth must be selected because it is the closest node to an observer looking from below.

# Therefore, every node can be recorded along with its horizontal distance, level, and traversal order. The level determines which node is deeper, while traversal order is used to resolve the case where two nodes occur at the same horizontal distance and depth.

# After all nodes have been collected, the entries are sorted so that nodes belonging to the same vertical line are grouped together. The last suitable entry for each horizontal distance becomes part of the bottom view.

# The approach is straightforward, but storing and sorting all N nodes introduces an additional O(N log N) cost.

# Algorithm
# Every node is traversed level by level, and its horizontalDistance, level, and traversal order are recorded so that both its vertical position and depth can be determined.

# The root is assigned horizontal distance 0 and level 0. A left child is assigned hd - 1, while a right child is assigned hd + 1.

# All stored entries are sorted by horizontal distance, then by level, and finally by traversal order so that deeper and later nodes can be identified correctly.

# For each horizontal distance, the last valid entry in the sorted group is selected because it represents the deepest node, while later traversal order resolves equal-depth ties.

# The selected values are returned from the smallest horizontal distance to the largest.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Stores every node with its horizontal distance,
    # depth, and level-order traversal position.
    def bottom_view(self, root):
        # An empty tree has no bottom view.
        if root is None:
            return []

        nodes = []
        nodes_queue = deque([(root, 0, 0)])

        order = 0

        while nodes_queue:
            node, hd, level = nodes_queue.popleft()

            nodes.append(
                (hd, level, order, node.val)
            )

            order += 1

            if node.left is not None:
                nodes_queue.append(
                    (
                        node.left,
                        hd - 1,
                        level + 1
                    )
                )

            if node.right is not None:
                nodes_queue.append(
                    (
                        node.right,
                        hd + 1,
                        level + 1
                    )
                )

        # Sorting groups equal horizontal distances.
        # Deeper and later level-order nodes appear last.
        nodes.sort(
            key=lambda item: (
                item[0],
                item[1],
                item[2]
            )
        )

        answer = []
        i = 0

        while i < len(nodes):
            j = i

            while (
                j + 1 < len(nodes)
                and nodes[j + 1][0] == nodes[i][0]
            ):
                j += 1

            # The final entry for this hd is the
            # deepest visible node from below.
            answer.append(nodes[j][3])

            i = j + 1

        return answer


if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(25)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    solution = Solution()

    print(
        solution.bottom_view(root)
    )

# Better Approach
# Sorting information for every node is unnecessary because only the best candidate for each horizontal distance needs to be retained.

# During DFS, two values are tracked:

# hd represents the horizontal distance of the current node from the root and identifies its vertical line.

# level represents the depth of the current node.

# For every horizontal distance, an ordered map stores the current bottom-view candidate together with its storedLevel. The storedLevel represents the greatest depth seen so far at that horizontal distance.

# If another node reaches the same horizontal distance at a deeper level, it must replace the stored node because it lies lower in the tree. If it is reached at the same level, it is also allowed to replace the previous node so that the later traversal candidate receives priority.

# Because an ordered map keeps horizontal distances sorted, the answer can be collected directly from left to right after DFS finishes.

# Algorithm
# DFS is started from the root with horizontal distance 0 and level 0, while an ordered map is maintained to store the deepest storedLevel and corresponding node value for every horizontal distance.

# When a horizontal distance is encountered for the first time, the current node and its level are stored because no better candidate is known yet.

# If the same horizontal distance has already been recorded, its value is replaced whenever currentLevel >= storedLevel, allowing deeper nodes and later equal-depth nodes to become the visible candidate.

# The left subtree is explored with hd - 1 and the right subtree with hd + 1, so the correct vertical positions are preserved throughout the traversal.

# After DFS is completed, the ordered map is read from the smallest horizontal distance to the largest to construct the bottom view.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Keeps the deepest candidate
    # for every horizontal distance.
    def dfs(
        self,
        node,
        hd,
        level,
        bottom
    ):
        # Null children cannot contribute
        # to the bottom view.
        if node is None:
            return

        # A deeper node replaces the stored candidate.
        # Equal depth also replaces it for the tie rule.
        if (
            hd not in bottom
            or level >= bottom[hd][0]
        ):
            bottom[hd] = (
                level,
                node.val
            )

        # Left-first DFS preserves left-to-right order
        # among nodes lying at the same depth.
        self.dfs(
            node.left,
            hd - 1,
            level + 1,
            bottom
        )

        self.dfs(
            node.right,
            hd + 1,
            level + 1,
            bottom
        )

    def bottom_view(self, root):
        # An empty tree has no visible nodes.
        if root is None:
            return []

        bottom = {}

        self.dfs(
            root,
            0,
            0,
            bottom
        )

        answer = []

        # Horizontal distances are sorted so
        # the result is returned left to right.
        for hd in sorted(bottom):
            answer.append(
                bottom[hd][1]
            )

        return answer


if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(25)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    solution = Solution()

    print(
        solution.bottom_view(root)
    )

# Optimal Approach
# BFS is particularly suitable for the Bottom View because nodes are processed level by level, from shallower levels toward deeper levels.

# Here, hd identifies the vertical line of the current node. Unlike Top View, where the first node at each horizontal distance is retained, the Bottom View requires the stored value to be overwritten whenever another node is encountered at the same hd.

# Since BFS visits deeper levels later, the most recently stored value naturally becomes the deepest visible node. If two nodes occur at the same depth and horizontal distance, the node encountered later in BFS also replaces the earlier one, satisfying the required tie rule.

# Two additional variables are maintained:

# minHD stores the smallest horizontal distance reached and identifies the leftmost vertical line.

# maxHD stores the largest horizontal distance reached and identifies the rightmost vertical line.

# These boundaries allow the final answer to be collected directly from minHD to maxHD without sorting the horizontal distances afterward.

# Algorithm
# If the root is null, an empty result is returned because no node is visible.

# The pair (root, 0) is inserted into a queue, while a map is maintained from horizontal distance to the most recently encountered node value. The variables minHD and maxHD are initialized to 0 to track the horizontal range covered by the tree.

# During BFS, the value stored for the current hd is overwritten by the current node, because nodes processed later are either deeper or receive priority when depth is equal.

# The left child is inserted with hd - 1 and the right child with hd + 1, while minHD and maxHD are updated whenever a new horizontal extreme is reached.

# After BFS is completed, the stored values are collected from minHD through maxHD so that the bottom view is returned from left to right.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def bottom_view(self, root):
        # An empty tree has no bottom view.
        if root is None:
            return []

        bottom = {}
        nodes_queue = deque([(root, 0)])

        min_hd = 0
        max_hd = 0

        while nodes_queue:
            node, hd = nodes_queue.popleft()

            # Later BFS nodes overwrite earlier nodes
            # at the same horizontal distance.
            bottom[hd] = node.val

            if node.left is not None:
                left_hd = hd - 1

                nodes_queue.append(
                    (
                        node.left,
                        left_hd
                    )
                )

                # min_hd keeps track of the
                # leftmost vertical line reached.
                min_hd = min(
                    min_hd,
                    left_hd
                )

            if node.right is not None:
                right_hd = hd + 1

                nodes_queue.append(
                    (
                        node.right,
                        right_hd
                    )
                )

                # max_hd keeps track of the
                # rightmost vertical line reached.
                max_hd = max(
                    max_hd,
                    right_hd
                )

        answer = []

        # Traversing this range directly returns
        # the bottom view from left to right.
        for hd in range(
            min_hd,
            max_hd + 1
        ):
            answer.append(bottom[hd])

        return answer


if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(25)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    solution = Solution()

    print(
        solution.bottom_view(root)
    )