# Given the root of a binary tree, a target node present in the tree, and an integer K, return the values of all nodes whose distance from the target is exactly K edges.

# The required nodes may lie:

# inside the target's subtree,

# above the target through its ancestors, or

# inside a different subtree reached through an ancestor.

# The nodes may be returned in any order.

# Example 1
# Input:
# root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], target = 5, K = 2

# Output:
# [7, 4, 1]

# Explanation:
# Nodes 7 and 4 are two edges below target 5. Node 1 is reached through the path 5 -> 3 -> 1, which also contains 2 edges.

# Example 2
# Input:
# root = [1], target = 1, K = 0

# Output:
# [1]

# Explanation:
# The target node itself is at distance 0, so it is the only node included in the answer.

# Approach 1
# A normal binary tree allows movement only from a parent to its children. However, nodes at distance K from the target may also require movement upward toward an ancestor.

# For example, node 1 in Example 1 is reached from target 5 using:

# 5 -> 3 -> 1

# To allow movement in both directions, every parent-child connection is treated as an undirected edge. An adjacency list is used to store all neighboring nodes so that movement from parent to child as well as child to parent becomes possible.

# A queue is then used for BFS starting from the target. A variable currLevel is maintained because it represents the number of edges between the target and the nodes currently being processed.

# A visited set is also maintained because converting the tree into an undirected graph introduces cycles such as:

# parent -> child -> parent

# The set prevents the same node from being processed repeatedly.

# Algorithm
# An adjacency list is constructed by traversing the binary tree, and every parent-child connection is stored in both directions so that movement upward and downward becomes possible.

# A BFS queue is initialized with the target, while a visited set is initialized with the target so that nodes are not revisited through bidirectional edges.

# A variable currLevel is initialized to 0 because the target itself lies at distance 0.

# While the queue is not empty and currLevel is smaller than K, all nodes belonging to the current BFS level are processed.

# For every processed node, each unvisited neighbor is marked as visited and inserted into the queue because that neighbor lies one additional edge away from the target.

# After one complete BFS level has been processed, currLevel is increased by 1.

# When currLevel becomes K, further expansion is stopped because every node currently remaining in the queue is exactly K edges away from the target.

# The values of all nodes remaining in the queue are collected and returned.

from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Converts each parent-child connection
    # into an undirected graph edge.
    def build_graph(self, node, graph):
        if node is None:
            return

        # Both directions are stored so traversal
        # can move downward as well as upward.
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

    # Returns all nodes exactly K edges
    # away from the target node.
    def distance_k(
        self,
        root,
        target,
        k
    ):
        if root is None:
            return []

        graph = defaultdict(list)

        self.build_graph(
            root,
            graph
        )

        nodes_queue = deque([target])

        # visited prevents movement back through
        # the bidirectional graph edges.
        visited = {target}

        # curr_level represents the distance
        # of the current BFS level from target.
        curr_level = 0

        while nodes_queue:

            # Every queued node is now exactly
            # k edges away from the target.
            if curr_level == k:
                break

            level_size = len(nodes_queue)

            # Exactly one BFS level is processed.
            for _ in range(level_size):
                node = nodes_queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited:

                        # Mark before insertion so
                        # duplicate visits are prevented.
                        visited.add(neighbor)
                        nodes_queue.append(neighbor)

            # One full level corresponds
            # to one additional edge.
            curr_level += 1

        return [
            node.val
            for node in nodes_queue
        ]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    target = root.left
    k = 2

    solution = Solution()

    print(
        solution.distance_k(
            root,
            target,
            k
        )
    )


# Approach 2
# Constructing a complete undirected adjacency list stores more information than is actually required.

# Every tree node already provides access to its left and right children. The only missing direction is movement from a child to its parent.

# Therefore, a mapping named parentTrack is maintained:

# child -> parent

# The name parentTrack indicates that the structure is used to keep track of each node's parent so that traversal can move upward when required.

# Once this mapping is available, every node effectively has at most three possible neighbors:

# left child,

# right child,

# parent.

# A nodesQueue is used for BFS from the target, while a visited set prevents movement back to nodes that have already been processed.

# A variable currLevel represents the current distance from the target because every BFS level corresponds to one additional edge.

# Algorithm
# A queue-based level-order traversal is performed from the root, and a map named parentTrack is constructed so that every non-root node can move upward to its parent.

# The root is treated separately in the parent mapping because it has no parent and therefore does not need an upward connection.

# A nodesQueue is initialized with the target because BFS must expand outward from the target one edge at a time.

# A visited set is initialized with the target so that movement through parent and child links cannot cause the same node to be processed again.

# A variable currLevel is initialized to 0 because the target is at distance 0 from itself.

# At each BFS level, the left child, right child, and mapped parent of every node are considered whenever they exist and have not already been visited.

# Every newly discovered neighbor is marked as visited before being inserted into nodesQueue, preventing duplicate insertion through another direction.

# After one complete level has been processed, currLevel is increased because all newly queued nodes are one edge farther from the target.

# When currLevel becomes K, further traversal is stopped, and the values of all nodes remaining in nodesQueue are returned.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Builds child-to-parent relationships
    # using level-order traversal.
    def build_parent_track(
        self,
        root,
        parent_track
    ):
        nodes_queue = deque([root])

        # The root has no parent, so None
        # represents the end of upward movement.
        parent_track[root] = None

        while nodes_queue:
            node = nodes_queue.popleft()

            if node.left is not None:
                parent_track[node.left] = node
                nodes_queue.append(node.left)

            if node.right is not None:
                parent_track[node.right] = node
                nodes_queue.append(node.right)

    # Performs BFS using left, right,
    # and parent connections.
    def distance_k(
        self,
        root,
        target,
        k
    ):
        if root is None:
            return []

        # parent_track stores every child's
        # parent to enable upward movement.
        parent_track = {}

        self.build_parent_track(
            root,
            parent_track
        )

        nodes_queue = deque([target])

        # visited prevents repeated movement
        # between a node and its neighbors.
        visited = {target}

        # curr_level stores the current
        # distance from the target.
        curr_level = 0

        while nodes_queue:

            # All nodes now in the queue
            # are exactly k edges away.
            if curr_level == k:
                break

            level_size = len(nodes_queue)

            for _ in range(level_size):
                node = nodes_queue.popleft()

                if (
                    node.left is not None
                    and node.left not in visited
                ):
                    visited.add(node.left)
                    nodes_queue.append(node.left)

                if (
                    node.right is not None
                    and node.right not in visited
                ):
                    visited.add(node.right)
                    nodes_queue.append(node.right)

                parent = parent_track[node]

                # The stored parent provides the
                # upward direction missing from the tree.
                if (
                    parent is not None
                    and parent not in visited
                ):
                    visited.add(parent)
                    nodes_queue.append(parent)

            # Completing one level increases
            # the distance by exactly one edge.
            curr_level += 1

        return [
            node.val
            for node in nodes_queue
        ]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    target = root.left
    k = 2

    solution = Solution()

    print(
        solution.distance_k(
            root,
            target,
            k
        )
    )

# Approach 3
# The parent map can be avoided completely by using recursion to determine how far the target lies below each ancestor.

# Two types of nodes can exist at distance K from the target:

# Nodes below the target.

# Nodes reached by moving upward to an ancestor and then either selecting that ancestor or moving into its opposite subtree.

# A helper is used to collect nodes lying a specific number of edges below a given node.

# Another recursive function returns the distance between the current node and the target. A returned value of -1 indicates that the target does not exist in that subtree. Otherwise, the returned value tells an ancestor how many edges below it the target was found.

# Suppose an ancestor is distance edges away from the target:

# if distance == K, that ancestor itself is included;

# otherwise, the ancestor's opposite subtree is searched for nodes that can complete the remaining distance.

# This allows both downward and upward paths to be handled without storing parent pointers.

# Algorithm
# A helper is used to collect nodes that lie exactly a required number of edges below a given node.

# A DFS is started from the root, and each recursive call is made to return the distance from the current node to the target, while -1 is returned when the target is absent from that subtree.

# When the target node is reached, all descendants exactly K edges below it are collected, and distance 0 is returned to its parent.

# If a valid distance is returned from the left child, that value is increased by 1 to obtain the current node's distance from the target.

# If this updated distance equals K, the current ancestor is inserted into the answer. Otherwise, the right subtree is searched for nodes whose additional distance completes exactly K edges.

# The same symmetric process is performed when the target is found in the right subtree, with the left subtree being treated as the opposite subtree.

# The calculated target distance is propagated upward until every relevant ancestor and opposite subtree has been processed.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Collects nodes exactly distance edges
    # below the given subtree root.
    def collect_down(
        self,
        node,
        distance,
        answer
    ):
        if (
            node is None
            or distance < 0
        ):
            return

        if distance == 0:
            answer.append(node.val)
            return

        self.collect_down(
            node.left,
            distance - 1,
            answer
        )

        self.collect_down(
            node.right,
            distance - 1,
            answer
        )

    # Returns the distance from node to target,
    # or -1 when target is absent.
    def find_target(
        self,
        node,
        target,
        k,
        answer
    ):
        if node is None:
            return -1

        # Descendants exactly k edges below
        # the target are collected here.
        if node is target:
            self.collect_down(
                node,
                k,
                answer
            )

            return 0

        left_result = self.find_target(
            node.left,
            target,
            k,
            answer
        )

        if left_result != -1:
            current_distance = (
                left_result + 1
            )

            if current_distance == k:
                answer.append(node.val)

            else:
                # The right subtree is opposite
                # to the path containing target.
                self.collect_down(
                    node.right,
                    k - current_distance - 1,
                    answer
                )

            return current_distance

        right_result = self.find_target(
            node.right,
            target,
            k,
            answer
        )

        if right_result != -1:
            current_distance = (
                right_result + 1
            )

            if current_distance == k:
                answer.append(node.val)

            else:
                # The left subtree is opposite
                # when target lies on the right.
                self.collect_down(
                    node.left,
                    k - current_distance - 1,
                    answer
                )

            return current_distance

        return -1

    # Finds nodes at distance k without
    # storing explicit parent links.
    def distance_k(
        self,
        root,
        target,
        k
    ):
        answer = []

        self.find_target(
            root,
            target,
            k,
            answer
        )

        return answer


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    target = root.left
    k = 2

    solution = Solution()

    print(
        solution.distance_k(
            root,
            target,
            k
        )
    )