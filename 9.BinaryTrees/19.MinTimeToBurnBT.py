# Given the root of a binary tree and a target node present in the tree, determine the minimum time required to burn the entire tree if the fire starts from the target.

# The fire spreads every second from a burning node to all directly connected nodes:

# its left child,

# its right child,

# its parent.

# A node burns only once, and all possible neighboring nodes catch fire simultaneously.

# Example 1
# Input:
# root = [1, 2, 3, 4, 5, null, 6], target = 2

# Output:
# 3

# Explanation:
# At time 0, node 2 starts burning. After 1 second, nodes 1, 4, and 5 burn. After 2 seconds, node 3 burns, and after 3 seconds, node 6 burns. Therefore, the entire tree burns in 3 seconds.

# Example 2
# Input:
# root = [1], target = 1

# Output:
# 0

# Explanation:
# The target is the only node in the tree, so the complete tree is already burning at time 0.

# Approach 1
# A binary tree normally provides links only from a parent to its children. Burning, however, must be allowed to spread in both directions.

# Therefore, every parent-child connection is converted into an undirected edge. Once this conversion is performed, the tree behaves like an undirected graph in which the fire can move to every directly connected node.

# A BFS is then started from the target.

# A queue is used because nodes that burn at the same second must be processed together. The variable levelSize stores the number of nodes burning during the current second so that exactly one BFS level can be processed at a time.

# A set named burned is maintained to represent nodes that have already caught fire. It prevents the same node from being reached repeatedly through the bidirectional graph.

# A boolean variable spread is used to record whether at least one new node caught fire during the current BFS level. Time is increased only when spread becomes true, because a second should be counted only when the fire actually reaches another node.

# Algorithm
# An adjacency list is constructed by traversing the binary tree, and every parent-child connection is stored in both directions so that fire can spread both upward and downward.

# A BFS queue is initialized with the target, and the target is inserted into the burned set because it is already burning at time 0.

# For each BFS iteration, the current queue size is stored in levelSize so that all nodes burning during the same second are processed together.

# A boolean variable spread is initialized as false before the current level is processed so that it can record whether the fire reaches at least one new node.

# For every node in the current level, all adjacent nodes that are not present in burned are marked as burned, inserted into the queue, and spread is set to true.

# After the complete level has been processed, the burning time is increased by 1 only if spread is true, because at least one new node has caught fire.

# The process is continued until the queue becomes empty, after which the recorded time is returned.

from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Builds an undirected graph so fire
    # can move between parent and child.
    def build_graph(self, node, graph):
        if node is None:
            return

        # Both directions are stored because
        # fire can spread upward and downward.
        if node.left is not None:
            graph[node].append(node.left)
            graph[node.left].append(node)

            self.build_graph(
                node.left,
                graph
            )

        if node.right is not None:
            graph[node].append(node.right)
            graph[node.right].append(node)

            self.build_graph(
                node.right,
                graph
            )

    # Returns the minimum time required
    # to burn the complete tree.
    def min_time(self, root, target):
        if root is None:
            return 0

        graph = defaultdict(list)

        self.build_graph(
            root,
            graph
        )

        nodes_queue = deque([target])

        # burned prevents a node from catching
        # fire more than once.
        burned = {target}

        time = 0

        while nodes_queue:
            level_size = len(nodes_queue)

            # spread records whether at least one
            # new node catches fire this second.
            spread = False

            # One complete level represents
            # all nodes burning at the same time.
            for _ in range(level_size):
                node = nodes_queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in burned:
                        burned.add(neighbor)
                        nodes_queue.append(neighbor)
                        spread = True

            # No second is counted when no
            # new node catches fire.
            if spread:
                time += 1

        return time


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    target = root.left

    solution = Solution()

    print(
        solution.min_time(
            root,
            target
        )
    )

# Approach 2
# Constructing a complete undirected graph is unnecessary because every node already provides references to its left and right children.

# The only missing connection is:

# child → parent

# Therefore, a map named parentTrack can be maintained. The name indicates that it is used to track the parent of each node, allowing the fire to move upward during BFS.

# After this preprocessing, every node effectively has at most three neighbors:

# left child,

# right child,

# parent.

# A queue is then used to simulate the burning process level by level.

# The variable levelSize stores how many nodes are burning during the current second. A set named burned keeps track of nodes that have already caught fire so that the fire cannot move back and forth between a node and its parent.

# A boolean variable spread records whether any new node catches fire during the current level. The elapsed time is increased only when this happens.

# Algorithm
# A queue-based traversal is performed from the root, and a map named parentTrack is constructed so that every non-root node is associated with its parent.

# The root is stored with no parent, or is treated separately, because no node exists above it.

# A BFS queue is initialized with the target, and the target is inserted into the burned set because it burns at time 0.

# At the beginning of each BFS level, the number of currently burning nodes is stored in levelSize, while spread is initialized as false.

# For every node in that level, its left child, right child, and mapped parent are examined.

# Whenever an existing neighbor has not already been burned, it is inserted into burned and the queue, while spread is set to true.

# After all levelSize nodes have been processed, the elapsed time is increased only when spread is true, indicating that the fire has reached at least one new node.

# Once the queue becomes empty, the recorded time is returned as the minimum time required to burn the entire tree.


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Builds child-to-parent links so fire
    # can also spread upward.
    def build_parent_track(
        self,
        root,
        parent_track
    ):
        nodes_queue = deque([root])

        # The root has no parent, so None
        # marks the end of upward movement.
        parent_track[root] = None

        while nodes_queue:
            node = nodes_queue.popleft()

            if node.left is not None:
                parent_track[node.left] = node
                nodes_queue.append(node.left)

            if node.right is not None:
                parent_track[node.right] = node
                nodes_queue.append(node.right)

    # Simulates fire using child
    # and parent connections.
    def min_time(self, root, target):
        if root is None:
            return 0

        parent_track = {}

        self.build_parent_track(
            root,
            parent_track
        )

        nodes_queue = deque([target])

        # burned prevents already burned nodes
        # from entering the queue again.
        burned = {target}

        time = 0

        while nodes_queue:
            level_size = len(nodes_queue)

            # spread records whether at least
            # one new node catches fire.
            spread = False

            # One complete queue level
            # corresponds to one burning stage.
            for _ in range(level_size):
                node = nodes_queue.popleft()

                if (
                    node.left is not None
                    and node.left not in burned
                ):
                    burned.add(node.left)
                    nodes_queue.append(node.left)
                    spread = True

                if (
                    node.right is not None
                    and node.right not in burned
                ):
                    burned.add(node.right)
                    nodes_queue.append(node.right)
                    spread = True

                parent = parent_track[node]

                # parent_track provides the
                # upward connection for the fire.
                if (
                    parent is not None
                    and parent not in burned
                ):
                    burned.add(parent)
                    nodes_queue.append(parent)
                    spread = True

            # Time advances only when the fire
            # reaches a new node.
            if spread:
                time += 1

        return time


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    target = root.left

    solution = Solution()

    print(
        solution.min_time(
            root,
            target
        )
    )

# Approach 3
# The total burning time is equal to the maximum distance from the target to any node in the tree.

# Instead of explicitly creating parent connections and simulating every second, this maximum distance can be determined using postorder DFS.

# For every subtree, two pieces of information are useful:

# height represents how far the deepest node lies below the current subtree.

# distanceFromTarget represents the distance from the current node to the target. A value of -1 indicates that the target is absent from that subtree.

# Suppose the target is found in the left subtree. If distanceFromTarget represents the distance from the current node to the target, the fire can reach a node in the opposite right subtree by travelling:

# target → current node → right subtree

# If the opposite subtree has height oppositeHeight, the total distance to its deepest node becomes:

# distanceFromTarget + 1 + oppositeHeight

# The additional 1 represents the edge from the current node into the root of the opposite subtree.

# The same reasoning is applied symmetrically when the target lies in the right subtree.

# By evaluating this maximum distance at every ancestor, the farthest node from the target is found.

# Algorithm
# A postorder DFS is performed so that information from the left and right child subtrees is available before the current node is processed.

# For every subtree, its height is calculated so that the maximum downward distance available through that subtree is known.

# A value named distanceFromTarget is maintained to represent the number of edges between the current node and the target, while -1 is used when the target is absent from that subtree.

# When the target itself is reached, distanceFromTarget is set to 0, and the subtree height is used to account for nodes lying below the target.

# If the target is found in the left subtree, its returned distance is increased by 1 to obtain the current node's distanceFromTarget.

# The farthest distance through the opposite right subtree is then calculated using distanceFromTarget + 1 + rightHeight, where the additional 1 represents the edge from the current node to the right child.

# The same calculation is performed symmetrically when the target is found in the right subtree, using the height of the left subtree.

# The maximum burning distance is updated whenever a larger candidate is obtained, and distanceFromTarget is propagated upward.

# After the root has been completely processed, the maximum recorded distance is returned as the minimum burning time.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Returns subtree height and the distance
    # from the current node to the target.
    def dfs(self, node, target):
        if node is None:
            return -1, -1

        left_height, left_distance = (
            self.dfs(node.left, target)
        )

        right_height, right_distance = (
            self.dfs(node.right, target)
        )

        height = (
            1
            + max(
                left_height,
                right_height
            )
        )

        # When target is reached, its subtree
        # height gives the farthest downward burn.
        if node is target:
            self.max_time = max(
                self.max_time,
                height
            )

            return height, 0

        if left_distance != -1:
            distance_from_target = (
                left_distance + 1
            )

            # The route moves from target to this
            # ancestor, then into the opposite subtree.
            self.max_time = max(
                self.max_time,
                distance_from_target
                + 1
                + right_height
            )

            return (
                height,
                distance_from_target
            )

        if right_distance != -1:
            distance_from_target = (
                right_distance + 1
            )

            # The left subtree becomes the opposite
            # branch when target lies on the right.
            self.max_time = max(
                self.max_time,
                distance_from_target
                + 1
                + left_height
            )

            return (
                height,
                distance_from_target
            )

        return height, -1

    # Finds the maximum distance from target
    # without storing explicit parent links.
    def min_time(self, root, target):
        if root is None:
            return 0

        self.max_time = 0

        self.dfs(
            root,
            target
        )

        return self.max_time


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    target = root.left

    solution = Solution()

    print(
        solution.min_time(
            root,
            target
        )
    )