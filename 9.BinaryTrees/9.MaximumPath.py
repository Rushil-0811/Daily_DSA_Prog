# Given the root of a binary tree, return the maximum path sum among all non-empty paths in the tree.

# A path is a sequence of connected nodes where no node appears more than once. The path may start and end at any nodes and does not need to pass through the root.

# Since node values may be negative, the maximum path sum can also be negative.

# Example 1
# Input: root = [1, 2, 3]

# Output: 6

# Explanation: The best path is 2 -> 1 -> 3. The sum is 2 + 1 + 3 = 6.

# Example 2
# Input: root = [-10, 9, 20, null, null, 15, 7]

# Output: 42

# Explanation: The best path is 15 -> 20 -> 7. Its sum is 15 + 20 + 7 = 42. The root -10 is not included because it reduces the sum.

# Brute Force Approach
# Any node can act as the highest point of a path. From that node, the path may take the best downward contribution from its left subtree, the best downward contribution from its right subtree, or neither if a contribution is negative.

# So, for every node, calculate:

# node value + useful left gain + useful right gain

# The answer cannot be checked only at the root because the best path may lie completely inside a subtree.

# The drawback is that the best downward gain of the same subtree is recalculated for many different nodes, causing repeated work.

# Algorithm
# A helper findMaxDownwardPath is used to calculate the best path sum that starts at a node and continues downward through at most one child.

# For a null node, 0 is returned because an empty branch contributes nothing to a downward path.

# For every non-null node, the best downward gains from the left and right children are calculated, while negative gains are replaced with 0 so that they do not reduce the path sum.

# The value node value + max(leftGain, rightGain) is returned because an extendable path can continue through only one child.

# For every node, the useful left and right contributions are calculated and combined with the current node as node value + leftContribution + rightContribution to represent the complete path passing through that node.

# The left and right subtrees are also checked recursively, and the maximum among the current path, the best left-subtree path, and the best right-subtree path is returned.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Returns the best path starting
    # here and moving through one child.
    def find_max_downward_path(self, root):
        if root is None:
            return 0

        # Negative branches are ignored
        # because they reduce the path sum.
        left_gain = max(
            0,
            self.find_max_downward_path(root.left)
        )

        # Negative branches are ignored
        # because they reduce the path sum.
        right_gain = max(
            0,
            self.find_max_downward_path(root.right)
        )

        # Only one branch can continue
        # as a downward path.
        return root.val + max(
            left_gain,
            right_gain
        )

    # Finds the best path by considering
    # every node as a turning point.
    def max_path_sum(self, root):
        if root is None:
            return float("-inf")

        # Negative contributions are skipped
        # while forming the current path.
        left_contribution = max(
            0,
            self.find_max_downward_path(root.left)
        )

        right_contribution = max(
            0,
            self.find_max_downward_path(root.right)
        )

        # Both branches may participate when
        # this node is the path's turning point.
        current_path = (
            root.val
            + left_contribution
            + right_contribution
        )

        # The best path may lie completely
        # inside either subtree.
        left_best = (
            self.max_path_sum(root.left)
            if root.left is not None
            else float("-inf")
        )

        right_best = (
            self.max_path_sum(root.right)
            if root.right is not None
            else float("-inf")
        )

        return max(
            current_path,
            left_best,
            right_best
        )


if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()

    print(solution.max_path_sum(root))

# Optimal Approach
# The Brute Force Approach already gives the correct path formula. Its only problem is recalculating subtree gains.

# Post-order DFS removes that repetition. Each node first receives the best extendable gain from its left and right children.

# At the current node, both gains may be used to form a complete candidate path:

# node value + leftGain + rightGain

# But only one side can be returned to the parent, because a path passed upward must remain a single chain rather than split into two branches.

# Negative gains are ignored because including them would only decrease the path sum.

# Algorithm
# A variable maxSum is initialized with negative infinity or the minimum integer value so that trees containing only negative values are handled correctly.

# A recursive helper findMaxGain is used to return the best path sum starting at the current node and extending downward through at most one child.

# For a null node, 0 is returned because no contribution is provided by an empty branch.

# The left and right gains are calculated recursively, and every negative gain is replaced with 0 because including such a branch would only decrease the path sum.

# The complete candidate path through the current node is formed as node value + leftGain + rightGain, and maxSum is updated whenever this candidate is larger.

# The value node value + max(leftGain, rightGain) is returned to the parent because only one branch can remain part of a valid upward path.

# After the complete post-order traversal has been performed, maxSum is returned as the maximum path sum.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Returns the best extendable path
    # starting from the current node.
    def find_max_gain(self, root):
        if root is None:
            return 0

        # Negative left contributions are clamped
        # to 0 to avoid reducing the path sum.
        left_gain = max(
            0,
            self.find_max_gain(root.left)
        )

        # Negative right contributions are clamped
        # to 0 to avoid reducing the path sum.
        right_gain = max(
            0,
            self.find_max_gain(root.right)
        )

        # Both branches may form a complete
        # path through the current node.
        current_path = (
            root.val
            + left_gain
            + right_gain
        )

        self.max_sum = max(
            self.max_sum,
            current_path
        )

        # Only one branch can continue upward
        # without creating a branching path.
        return root.val + max(
            left_gain,
            right_gain
        )

    # Returns the maximum path sum
    # among all non-empty paths.
    def max_path_sum(self, root):
        self.max_sum = float("-inf")

        self.find_max_gain(root)

        return self.max_sum


if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()

    print(solution.max_path_sum(root))