# Given the root of a binary tree, return all root-to-leaf paths.

# A root-to-leaf path starts at the root and ends at a leaf node. A leaf is a node that has no left or right child.

# Each path should contain the node values in the same order in which they appear from the root to the leaf.

# Example 1
# Input:
# root = [1, 2, 3, null, 5]

# Output:
# [[1, 2, 5], [1, 3]]

# Explanation:
# There are two root-to-leaf paths: 1 -> 2 -> 5 and 1 -> 3.

# Example 2
# Input:
# root = [1, 2, 3, 4, 5, null, 6]

# Output:
# [[1, 2, 4], [1, 2, 5], [1, 3, 6]]

# Explanation:
# The leaf nodes are 4, 5, and 6, so the corresponding root-to-leaf paths are 1 -> 2 -> 4, 1 -> 2 -> 5, and 1 -> 3 -> 6

# Approach 1
# To construct a root-to-leaf path, every node needs access to the sequence of nodes visited before reaching it.

# Two variables are used:

# currentPath stores the sequence of node values from the root to the current node.

# paths stores all completed root-to-leaf paths found during traversal.

# A straightforward DFS approach is used in which each recursive branch receives its own copy of currentPath. Because each branch owns a separate path copy, changes made while exploring one subtree cannot affect another subtree.

# Whenever a leaf node is reached, the current path already represents a complete root-to-leaf path and is stored in paths.

# This avoids the need to undo changes while returning from recursion, but repeatedly copying partial paths creates additional work and memory usage.

# Algorithm
# If root is null, an empty paths list is returned because no root-to-leaf path exists.

# A result list paths is maintained to store completed paths, while currentPath is used to represent the path from the root to the currently visited node.

# Whenever a node is visited, its value is appended to currentPath because it becomes part of the active root-to-node path.

# If the current node is a leaf, the completed currentPath is stored in paths.

# Before the left and right children are explored, separate copies of currentPath are passed to those recursive calls so that modifications in one branch cannot affect the other.

# After every reachable leaf has been processed, all paths stored in paths are returned.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Builds root-to-leaf paths using
    # a separate path for each branch.
    def dfs(
        self,
        node,
        current_path,
        paths
    ):
        # An empty subtree cannot
        # extend the current path.
        if node is None:
            return

        current_path.append(node.val)

        # A leaf completes one
        # valid root-to-leaf path.
        if (
            node.left is None
            and node.right is None
        ):
            paths.append(current_path.copy())
            return

        # Separate copies prevent changes
        # in one branch affecting another.
        self.dfs(
            node.left,
            current_path.copy(),
            paths
        )

        self.dfs(
            node.right,
            current_path.copy(),
            paths
        )

    # Returns all paths starting at
    # the root and ending at leaves.
    def root_to_leaf_paths(self, root):
        paths = []

        if root is None:
            return paths

        self.dfs(
            root,
            [],
            paths
        )

        return paths


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    solution = Solution()

    print(
        solution.root_to_leaf_paths(root)
    )

# Approach 2
# The repeated copying performed in Approach 1 is unnecessary because DFS explores only one root-to-current-node route at a time.

# Instead, a single mutable list currentPath is maintained. It always represents the active path from the root to the current node, while paths stores copies of completed root-to-leaf paths.

# When a node is entered, its value is added to currentPath. If a leaf is reached, a copy of currentPath is stored in paths.

# After both child subtrees have been explored, the current node is removed from currentPath. This restores the path to the exact state it had before that node was entered.

# This follows the backtracking pattern:

# Choose → Explore → Undo

# Algorithm
# A result list paths and a mutable list currentPath are maintained, where paths stores completed root-to-leaf paths and currentPath represents the active root-to-node route.

# If the current node is null, the recursive call is terminated because no path can be extended through an empty subtree.

# When a non-null node is entered, its value is appended to currentPath because it becomes part of the active path.

# If the current node is a leaf, a copy of currentPath is stored in paths because a complete root-to-leaf path has been formed.

# Otherwise, the left and right children are explored recursively using the same currentPath.

# After the current node and its descendants have been processed, the current node is removed from currentPath so that the parent path state is restored before another branch is explored.

# After DFS has finished, all paths stored in paths are returned.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Builds paths using one shared
    # path with backtracking.
    def dfs(
        self,
        node,
        current_path,
        paths
    ):
        # An empty subtree cannot
        # extend the current path.
        if node is None:
            return

        current_path.append(node.val)

        # A copy is stored because
        # current_path changes during backtracking.
        if (
            node.left is None
            and node.right is None
        ):
            paths.append(current_path.copy())
        else:
            self.dfs(
                node.left,
                current_path,
                paths
            )

            self.dfs(
                node.right,
                current_path,
                paths
            )

        # Remove the current node to
        # restore the parent's path.
        current_path.pop()

    # Returns all paths starting at
    # the root and ending at leaves.
    def root_to_leaf_paths(self, root):
        paths = []
        current_path = []

        self.dfs(
            root,
            current_path,
            paths
        )

        return paths


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    solution = Solution()

    print(
        solution.root_to_leaf_paths(root)
    )

