# Given the root of a binary tree, find the size of the largest subtree that is also a Binary Search Tree. The size of a subtree means the number of nodes in that subtree.

# A subtree is a BST if:

# Every value in the left subtree is smaller than the root value.

# Every value in the right subtree is greater than the root value.

# The left and right subtrees are also BSTs.

# Example 1
# Input: root = [2, 1, 3]

# Output: 3

# Explanation: The given complete binary tree is a BST consisting of 3 nodes.

# Example 2
# Input: root = [10, null, 20, null, 30, null, 40, null, 50]

# Output: 5

# Explanation: If we consider node 10 as the root, it forms the largest BST in the tree, with a size of 5.

# Brute Force Approach
# The most direct thought is: check every subtree one by one.

# For any node, treat that node as the root of a subtree. If that whole subtree is a valid BST, count its nodes and consider it as an answer. If it is not a BST, move to its left and right children and repeat the same check there.

# This works because the answer must be rooted at some node in the tree. The only problem is that the same nodes may be checked again and again while validating different subtrees.

# Algorithm
# For every node, first check whether the subtree rooted at that node is a valid BST. This is done using lower and upper bounds, because every node must fit inside the range decided by its ancestors.

# If the subtree is valid, count all nodes in that subtree. This gives the size of one possible BST answer.

# If the subtree is not valid, recursively find the largest BST in the left subtree and in the right subtree. This is needed because the current root cannot be used, but a valid BST may still exist below it.

# Return the larger value from the left and right side.

from typing import Optional

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class Solution:
    """
    Checks whether the current subtree follows
    the BST rule inside the allowed value range.
    """
    def is_valid_bst(self, root: Optional[Node], low: float, high: float) -> bool:
        # An empty subtree is always valid.
        if root is None:
            return True

        # The current value must stay inside its valid BST range.
        if root.data <= low or root.data >= high:
            return False

        # The left and right subtrees get stricter ranges.
        return (
            self.is_valid_bst(root.left, low, root.data)
            and self.is_valid_bst(root.right, root.data, high)
        )

    """
    Counts all nodes in the current subtree.
    """
    def count_nodes(self, root: Optional[Node]) -> int:
        # Empty subtree contributes zero nodes.
        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    """
    Returns the size of the largest subtree
    that satisfies the BST property.
    """
    def largestBst(self, root: Optional[Node]) -> int:
        # Empty tree has no BST nodes.
        if root is None:
            return 0

        # If the whole current subtree is BST, its full size is the answer here.
        if self.is_valid_bst(root, float("-inf"), float("inf")):
            return self.count_nodes(root)

        # Otherwise, the answer must be fully inside one child subtree.
        return max(self.largestBst(root.left), self.largestBst(root.right))


# Driver code starts
def main() -> None:
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(1)
    root.left.right = Node(8)
    root.right.right = Node(7)

    sol = Solution()
    print(sol.largestBst(root))


if __name__ == "__main__":
    main()

# Optimal Approach
# The brute force method keeps asking the same question again: “Is this subtree a BST?” A better way is to make every subtree answer that question only once. For each node, the parent needs three useful facts from its left and right children:

# What is the minimum value in that subtree?

# What is the maximum value in that subtree?

# What is the largest BST size found there?

# This naturally suggests postorder traversal, because children must be solved before the parent. At a node, the current subtree becomes a BST only if: left maximum < current value < right minimum

# If this condition is true, both child BSTs can join with the current node. If it is false, the current subtree cannot be a BST, but the largest BST may still be inside the left or right child.

# Algorithm
# For a null node, return a valid empty subtree with size 0, minimum as positive infinity, and maximum as negative infinity. This makes leaf-node comparisons work naturally.

# Recursively solve the left and right children first. This is done because the current node needs child minimums, maximums, and sizes before it can decide anything.

# If the left maximum is smaller than the current value and the current value is smaller than the right minimum, the current subtree is a valid BST. Return its updated minimum, maximum, and total size.

# If the condition fails, return an invalid range. This prevents the parent from wrongly using this subtree as part of a larger BST.

# Even when the current subtree is invalid, keep the best size from the left and right side, because the answer may already exist below the current node.

from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class Info:
    def __init__(self, min_value: float, max_value: float, size: int) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.size = size


class Solution:
    """
    Returns subtree boundaries and the largest BST size
    found inside the current subtree.
    """
    def solve(self, root: Optional[Node]) -> Info:
        # Empty subtree is valid and should not block leaf comparisons.
        if root is None:
            return Info(float("inf"), float("-inf"), 0)

        # Left information is needed before checking the current root.
        left_info = self.solve(root.left)

        # Right information is needed before checking the current root.
        right_info = self.solve(root.right)

        # The current root can join both children only if BST bounds fit.
        if left_info.max_value < root.data < right_info.min_value:
            # The new BST size includes left, right, and the current node.
            current_size = left_info.size + right_info.size + 1

            # These boundaries describe the full valid BST rooted here.
            current_min = min(left_info.min_value, root.data)
            current_max = max(right_info.max_value, root.data)

            return Info(current_min, current_max, current_size)

        # Invalid boundaries stop the parent from using this subtree as BST.
        return Info(float("-inf"), float("inf"), max(left_info.size, right_info.size))

    """
    Returns the size of the largest subtree
    that satisfies the BST property.
    """
    def largestBst(self, root: Optional[Node]) -> int:
        # The helper stores the final answer in its size field.
        return self.solve(root).size


# Driver code starts
def main() -> None:
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(1)
    root.left.right = Node(8)
    root.right.right = Node(7)

    sol = Solution()
    print(sol.largestBst(root))


if __name__ == "__main__":
    main()