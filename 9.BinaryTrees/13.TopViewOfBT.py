# Given the root of a binary tree, return its top view from left to right.

# The top view contains the nodes that are visible when the tree is observed from above. For every vertical position, only the node closest to the root is visible; nodes lying below it at the same position are hidden.

# To identify vertical positions, a horizontal distance (hd) is assigned to every node. It represents how far a node lies horizontally from the root:

# The root has hd = 0.

# A left child has hd = parentHD - 1.

# A right child has hd = parentHD + 1.

# The visible node values must be returned from the smallest horizontal distance to the largest.

# Example 1
# Input: root = [1, 2, 3, null, 4, null, 5]

# Output: [2, 1, 3, 5]

# Explanation: Node 2 is visible at horizontal distance -1, node 1 at 0, node 3 at 1, and node 5 at 2. Node 4 lies below node 1 at horizontal distance 0, so it is hidden from the top view.

# Example 2
# Input: root = [1, 2, 3, 4, 5, 6, 7]

# Output: [4, 2, 1, 3, 7]

# Explanation: The topmost nodes from the leftmost to the rightmost vertical line are 4, 2, 1, 3, 7. Nodes 5 and 6 lie below node 1 on the same vertical line and are therefore not visible from above.

# Brute Force Approach
# Nodes lying on the same vertical line have the same horizontal distance (hd). Here, hd is used to group nodes belonging to the same vertical position.

# For the top view, the node with the smallest level on each vertical line must be selected because it is closest to the root. Therefore, every node can be recorded along with its horizontal distance and level.

# A traversal order can also be stored as a tie-breaker when multiple nodes appear at the same horizontal distance and level. After all nodes have been collected, the entries are sorted first by horizontal distance and then by level.

# The first node appearing for every horizontal distance after sorting represents the topmost visible node.

# This approach is straightforward, but sorting information for all N nodes introduces an additional O(N log N) cost.

# Algorithm
# Each node is traversed along with its horizontalDistance, level, and traversal order so that its vertical position and depth are recorded.

# The root is assigned horizontal distance 0 and level 0. For every left child, the horizontal distance is decreased by 1, while for every right child, it is increased by 1.

# All recorded entries are sorted first by horizontal distance and then by level, while traversal order is used to resolve ties.

# For every horizontal distance, the first node appearing in the sorted sequence is selected because it has the minimum depth for that vertical line.

# All remaining nodes having the same horizontal distance are ignored because they are hidden below the selected node.

# The selected values are returned from the smallest horizontal distance to the largest.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Finds the top view by storing
    # and sorting information for all nodes.
    def top_view(self, root):
        if root is None:
            return []

        nodes = []
        queue = deque([(root, 0, 0)])

        order = 0

        # Traverse the complete tree and store
        # horizontal distance, level, and order.
        while queue:
            node, hd, level = queue.popleft()

            nodes.append(
                (hd, level, order, node.val)
            )

            order += 1

            if node.left is not None:
                queue.append(
                    (node.left, hd - 1, level + 1)
                )

            if node.right is not None:
                queue.append(
                    (node.right, hd + 1, level + 1)
                )

        # Sorting places vertical lines from left
        # to right and shallower nodes first.
        nodes.sort(
            key=lambda entry: (
                entry[0],
                entry[1],
                entry[2]
            )
        )

        answer = []
        previous_hd = None

        # The first node for each horizontal
        # distance is visible from the top.
        for hd, level, order, value in nodes:
            if previous_hd is None or hd != previous_hd:
                answer.append(value)
                previous_hd = hd

        return answer


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Solution()

    print(solution.top_view(root))

# Better Approach
# Sorting information for every node is unnecessary because only the topmost node for each horizontal distance is required.

# During DFS, two values are tracked:

# hd represents the horizontal distance of the current node from the root and identifies its vertical line.

# level represents the depth of the current node and determines how close it is to the root.

# For every horizontal distance, an ordered map stores two pieces of information: the current topmost node value and its storedLevel. The storedLevel represents the smallest depth encountered so far for that horizontal distance.

# If another node reaches the same horizontal distance at a greater level, it lies below the already stored node and cannot belong to the top view. A replacement is made only when a node is found at a smaller level.

# Because an ordered map keeps ho

# Algorithm
# DFS is started from the root with horizontal distance 0 and level 0.

# An ordered map is maintained in which every horizontal distance stores the smallest storedLevel encountered so far and its corresponding node value.

# When a horizontal distance is encountered for the first time, the current node and its level are stored because it is currently the topmost known node on that vertical line.

# If the same horizontal distance has already been recorded, its entry is replaced only when the current level is smaller than storedLevel.

# The left subtree is explored with hd - 1, while the right subtree is explored with hd + 1, so their vertical positions remain correctly represented.

# After the traversal is completed, the ordered map is read from the smallest horizontal distance to the largest to construct the top view.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Stores the shallowest node
    # found for every horizontal distance.
    def dfs(self, node, hd, level, top_nodes):
        if node is None:
            return

        # DFS may reach a deeper node first.
        # Keep only the smallest level for this hd.
        if (
            hd not in top_nodes
            or level < top_nodes[hd][0]
        ):
            top_nodes[hd] = (
                level,
                node.val
            )

        self.dfs(
            node.left,
            hd - 1,
            level + 1,
            top_nodes
        )

        self.dfs(
            node.right,
            hd + 1,
            level + 1,
            top_nodes
        )

    # Finds the top view using DFS
    # with level information.
    def top_view(self, root):
        if root is None:
            return []

        top_nodes = {}

        self.dfs(
            root,
            0,
            0,
            top_nodes
        )

        answer = []

        # Sort horizontal distances so
        # the answer is returned left to right.
        for hd in sorted(top_nodes):
            answer.append(
                top_nodes[hd][1]
            )

        return answer


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Solution()

    print(solution.top_view(root))

# Optimal Approach
# For the top view, only the shallowest node at each horizontal distance is required.

# BFS is well suited to this requirement because nodes are processed level by level. Therefore, the first node encountered at a particular hd is already the closest node to the root on that vertical line.

# Here, hd identifies the vertical line of the current node. Once a value has been stored for an hd, later nodes encountered at the same position are deeper and are not allowed to replace it.

# Two additional variables are maintained:

# minHD stores the smallest horizontal distance encountered and identifies the leftmost visible vertical line.

# maxHD stores the largest horizontal distance encountered and identifies the rightmost visible vertical line.

# These boundaries allow the final answer to be collected directly from minHD to maxHD without sorting the horizontal distances afterward.

# Algorithm
# If the root is null, an empty result is returned because no node is visible.

# The pair (root, 0) is inserted into a queue, where 0 represents the root's horizontal distance.

# A map is maintained from horizontal distance to node value, while minHD and maxHD are maintained to record the leftmost and rightmost horizontal distances reached.

# During BFS, a node value is stored only when its horizontal distance has not been recorded earlier, because the first node encountered by BFS is the shallowest node at that vertical position.

# The left child is inserted with hd - 1 and the right child with hd + 1, while minHD and maxHD are updated whenever the horizontal range expands.

# After BFS is completed, the stored values are collected from minHD through maxHD so that the result is produced from left to right.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Finds the top view by recording
    # the first node at every hd.
    def top_view(self, root):
        if root is None:
            return []

        top_node = {}
        queue = deque([(root, 0)])

        min_hd = 0
        max_hd = 0

        # BFS processes shallower nodes first.
        # The first node at an hd is topmost.
        while queue:
            node, hd = queue.popleft()

            # Once an hd is recorded, deeper
            # nodes at that hd stay hidden.
            if hd not in top_node:
                top_node[hd] = node.val

            if node.left is not None:
                left_hd = hd - 1

                queue.append(
                    (node.left, left_hd)
                )

                min_hd = min(
                    min_hd,
                    left_hd
                )

            if node.right is not None:
                right_hd = hd + 1

                queue.append(
                    (node.right, right_hd)
                )

                max_hd = max(
                    max_hd,
                    right_hd
                )

        answer = []

        # Read from minHD to maxHD
        # to preserve left-to-right order.
        for hd in range(
            min_hd,
            max_hd + 1
        ):
            answer.append(top_node[hd])

        return answer


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Solution()

    print(solution.top_view(root))