# Given the root of a binary tree, return the diameter of the tree.

# The diameter is the length of the longest path between any two nodes. This path may or may not pass through the root.

# The path length is measured using the number of edges, not nodes. Therefore, a tree containing only one node has diameter 0.

# Example 1
# Input: root = [1, 2, 3, 4, 5]

# Output: 3

# Explanation: The longest path can be 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3. Both paths contain 3 edges, so the diameter is 3.

# Example 2
# Input: root = [1, 2]

# Output: 1

# Explanation: The longest path is from node 2 to node 1. This path contains exactly one edge

# Brute Force Approach
# For any node, the longest path passing through it can extend to the deepest node in its left subtree and the deepest node in its right subtree.

# If the heights of the child subtrees are measured in nodes, then:

# leftHeight + rightHeight

# directly gives the number of edges in the path passing through the current node.

# However, the actual diameter may lie completely inside the left or right subtree. Therefore, every node must be considered as a possible highest point of the longest path.

# The drawback is that subtree heights are recalculated for different ancestors, which creates repeated work.

# Algorithm
# If the current node is null, return 0 because an empty subtree has no diameter.

# Use a helper findHeight to calculate the height of a subtree in terms of nodes.

# Calculate leftHeight and rightHeight from the current node's children.

# Use leftHeight + rightHeight as the diameter passing through the current node.

# Recursively find the best diameter in the left and right subtrees because the longest path may not pass through the current node.

# Return the maximum among the current path, left-subtree diameter, and right-subtree diameter.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Returns subtree height
    # measured in nodes.
    def find_height(self, node):
        # An empty subtree
        # has height zero.
        if node is None:
            return 0

        left_height = self.find_height(
            node.left
        )

        right_height = self.find_height(
            node.right
        )

        return 1 + max(
            left_height,
            right_height
        )

    # Checks every node as the
    # highest point of the diameter.
    def find_diameter(self, node):
        # An empty subtree
        # has diameter zero.
        if node is None:
            return 0

        # Heights from both children form
        # the path through this node.
        left_height = self.find_height(
            node.left
        )

        right_height = self.find_height(
            node.right
        )

        current_diameter = (
            left_height + right_height
        )

        # The longest path may lie
        # completely inside either subtree.
        left_diameter = self.find_diameter(
            node.left
        )

        right_diameter = self.find_diameter(
            node.right
        )

        return max(
            current_diameter,
            left_diameter,
            right_diameter
        )

    # Returns the diameter
    # measured in edges.
    def diameter_of_binary_tree(self, root):
        return self.find_diameter(root)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()

    print(
        solution.diameter_of_binary_tree(root)
    )

# Better Approach
# A binary tree can be viewed as an undirected tree by treating every parent-child connection as a two-way edge.

# For an unweighted tree, starting from any node and finding a farthest node gives one endpoint of a diameter. Running BFS again from that endpoint gives the maximum distance to the opposite endpoint, which is the diameter.

# This approach runs in O(N) time, so it already removes the repeated work of the Brute Force Approach. However, converting the binary tree into an explicit graph requires O(N) additional space. The Optimal Approach keeps the same O(N) time complexity while avoiding this graph construction.

# Algorithm
# If root is null, return 0 because an empty tree has no diameter.

# Convert every parent-child connection into two graph edges so that traversal can move in both directions.

# Run BFS from root to find a node farthest from it. In a tree, this node can serve as one endpoint of a diameter.

# Run a second BFS from this endpoint to find the farthest reachable node.

# The maximum distance found during the second BFS is the diameter measured in edges.

# Return this distance.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Converts parent-child links
    # into two-way graph edges.
    def build_graph(self, node, graph):
        # A null node adds no edge.
        if node is None:
            return

        graph.setdefault(node, [])

        # Connect the left child
        # in both directions.
        if node.left is not None:
            graph.setdefault(node.left, [])

            graph[node].append(node.left)
            graph[node.left].append(node)

            self.build_graph(
                node.left,
                graph
            )

        # Connect the right child
        # in both directions.
        if node.right is not None:
            graph.setdefault(node.right, [])

            graph[node].append(node.right)
            graph[node.right].append(node)

            self.build_graph(
                node.right,
                graph
            )

    # Returns the farthest node
    # and its distance from start.
    def bfs(self, start, graph):
        queue = deque([(start, 0)])
        visited = {start}

        farthest_node = start
        max_distance = 0

        # BFS explores nodes by
        # increasing edge distance.
        while queue:
            node, distance = queue.popleft()

            # Track the farthest node
            # reached so far.
            if distance > max_distance:
                max_distance = distance
                farthest_node = node

            # Visit each neighbor once
            # to avoid moving in cycles.
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)

                    queue.append(
                        (neighbor, distance + 1)
                    )

        return farthest_node, max_distance

    # Finds the diameter using
    # two BFS traversals.
    def diameter_of_binary_tree(self, root):
        # An empty tree
        # has diameter zero.
        if root is None:
            return 0

        graph = {}

        self.build_graph(root, graph)

        # First BFS finds one
        # endpoint of a diameter.
        endpoint, _ = self.bfs(
            root,
            graph
        )

        # Second BFS finds the
        # diameter from that endpoint.
        _, diameter = self.bfs(
            endpoint,
            graph
        )

        return diameter


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()

    print(
        solution.diameter_of_binary_tree(root)
    )

# Optimal Approach
# The Brute Force Approach already gives the required relation:

# diameter through a node = leftHeight + rightHeight

# Its inefficiency comes from recalculating subtree heights for different nodes. Post-order DFS removes this repeated work by calculating each subtree height exactly once.

# At every node, the left and right subtree heights are first obtained. Their sum gives the diameter passing through that node, while only the larger of the two heights can continue upward to the parent.

# Like the BFS approach, this solution runs in O(N) time. Its main advantage is that it works directly on the binary tree and avoids constructing an explicit graph. Therefore, its auxiliary space is only the recursion stack, O(H), instead of the O(N) graph storage required by BFS.

# Algorithm
# Initialize diameter = 0 to store the longest path found so far.

# Use a recursive helper that returns the height of the current subtree in terms of nodes.

# If the current node is null, return 0 because an empty subtree contributes no height.

# Recursively calculate leftHeight and rightHeight before processing the current node.

# Update diameter with leftHeight + rightHeight, since this is the number of edges in the longest path passing through the current node.

# Return 1 + max(leftHeight, rightHeight) because only one downward branch can be extended by the parent.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Returns subtree height
    # while updating the diameter.
    def find_height(self, node):
        # An empty subtree
        # contributes height zero.
        if node is None:
            return 0

        left_height = self.find_height(
            node.left
        )

        right_height = self.find_height(
            node.right
        )

        # Both branches can form
        # a path through this node.
        self.diameter = max(
            self.diameter,
            left_height + right_height
        )

        # Only one branch can
        # continue toward the parent.
        return 1 + max(
            left_height,
            right_height
        )

    # Returns the diameter
    # measured in edges.
    def diameter_of_binary_tree(self, root):
        self.diameter = 0

        self.find_height(root)

        return self.diameter


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()

    print(
        solution.diameter_of_binary_tree(root)
    )