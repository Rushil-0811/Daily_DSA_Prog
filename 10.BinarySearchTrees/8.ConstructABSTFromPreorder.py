# Given an array preorder that represents the preorder traversal of a Binary Search Tree, construct the BST and return its root. In preorder traversal, nodes are visited in this order:

# Root

# Left subtree

# Right subtree

# In a BST, every value in the left subtree is smaller than the root, and every value in the right subtree is greater than the root.

# Example 1
# Input: array = [8, 5, 1, 7, 10, 12]

# Output: tree generated

# Explanation: In preorder (Root ->Left ->Right), the first value 8 is the tree root.

# BST rules state all smaller values go left and all larger values go right, splitting the rest into left subtree [5, 1, 7] and right subtree [10, 12].

# Applying the same logic recursively:

# For [5, 1, 7]: 5 is the root, 1 is smaller (left child), and 7 is larger (right child).

# For [10, 12]: 10 is the root, there are no smaller values (no left child), and 12 is larger (right child).

# Example 2
# Input: array = [10, 4, 1, 6, 15, 20]

# Output: tree generated

# Explanation: In preorder (Root -> Left -> Right), the first value 10 is the tree root.

# BST rules state all smaller values go left and all larger values go right, splitting the rest into left subtree [4, 1, 6] and right subtree [15, 20]. Applying the same logic recursively: For [4, 1, 6]: 4 is the root, 1 is smaller (left child), and 6 is larger (right child). For [15, 20]: 15 is the root, there are no smaller values (no left child), and 20 is larger (right child).

# Brute Force Approach
# The most direct idea is to rebuild the BST in the same order in which preorder gives the values.

# Preorder visits a node before its children, so the first value is the root. After that, every next value can simply be inserted into the BST using the normal BST insertion rule.

# If the value is smaller than the current node, move left. If it is greater, move right. Eventually an empty position is found, and the value is placed there.

# This works because inserting values one by one into an empty BST using the given preorder order creates the same BST. The only drawback is that the tree can become skewed, and insertion may take linear time for many nodes.

# Algorithm
# Start with an empty root because no node has been created yet.

# Traverse every value in preorder from left to right. This is done because preorder already gives the root before its subtree nodes.

# Insert each value into the BST using the normal BST rule. If the value is smaller, it must go somewhere in the left subtree; if it is greater, it must go somewhere in the right subtree.

# When an empty position is reached, create a new node there because that is the correct place for the current value.

# After all values are inserted, return the root of the constructed BST.

from typing import List, Optional


class TreeNode:
    # Creates a tree node with left and right child links.
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class Solution:
    # Inserts one value into the BST and returns the subtree root.
    def insert_node(
        self,
        root: Optional[TreeNode],
        value: int
    ) -> TreeNode:
        # An empty position is the correct place for the new value.
        if root is None:
            return TreeNode(value)

        # Smaller values must be placed somewhere in the left subtree.
        if value < root.val:
            root.left = self.insert_node(root.left, value)
        # Greater values must be placed somewhere in the right subtree.
        elif value > root.val:
            root.right = self.insert_node(root.right, value)

        return root

    """
    Builds a BST by inserting preorder values
    one by one using the normal BST rule.
    """
    def bst_from_preorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Stores the root of the BST built so far.
        root: Optional[TreeNode] = None

        for value in preorder:
            root = self.insert_node(root, value)

        return root

    # Prints inorder traversal of the constructed BST.
    def print_inorder(self, root: Optional[TreeNode]) -> None:
        # Empty subtree has nothing to print.
        if root is None:
            return

        self.print_inorder(root.left)
        print(root.val, end=" ")
        self.print_inorder(root.right)


# Driver code starts
def main() -> None:
    preorder: List[int] = [8, 5, 1, 7, 10, 12]

    obj = Solution()
    root = obj.bst_from_preorder(preorder)

    obj.print_inorder(root)


if __name__ == "__main__":
    main()

# Better Approach
# In preorder traversal, the first value of any subtree is its root.

# Now apply the BST property. In the preorder segment for a subtree, all values smaller than the root belong to the left subtree. Once a value greater than the root appears, the right subtree starts.

# For example, in [8, 5, 1, 7, 10, 12], root is 8. Values 5, 1, 7 are smaller than 8, so they belong to the left subtree. The first greater value is 10, so the right subtree starts there.

# This gives a clean recursive split.

# The small improvement is to find this split point using binary search. The whole segment is not sorted, but the condition value > root changes only once: first all left-subtree values are smaller than root, then all right-subtree values are greater than root.

# So binary search can find the first value greater than the root.

# Algorithm
# Treat the current preorder range as one subtree. This is useful because preorder keeps each subtree's nodes together.

# The first value of the range becomes the root because preorder always visits root first.

# Use binary search to find the first value greater than the root. This split point is needed because smaller values form the left subtree and greater values form the right subtree.

# Recursively build the left subtree from the values before the split point.

# Recursively build the right subtree from the values from the split point onward.

# Return the root after connecting both subtrees.

from typing import List, Optional

class TreeNode:
    # Creates a tree node with left and right child links.
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class Solution:
    # Builds the BST from preorder values inside one range.
    def build(
        self,
        preorder: List[int],
        start: int,
        end: int
    ) -> Optional[TreeNode]:
        # No values are left in this range, so no subtree exists.
        if start > end:
            return None

        # The first value of this range is the subtree root.
        root = TreeNode(preorder[start])

        # Defines the search space for the first greater value.
        left: int = start + 1
        right: int = end + 1

        while left < right:
            mid: int = left + (right - left) // 2

            # A greater middle value may be the first right-subtree value.
            if preorder[mid] > root.val:
                right = mid
            # A smaller middle value still belongs to the left subtree.
            else:
                left = mid + 1

        # Marks where the right subtree begins.
        split_index: int = left

        root.left = self.build(preorder, start + 1, split_index - 1)
        root.right = self.build(preorder, split_index, end)

        return root

    """
    Builds a BST by using binary search
    to split each preorder range.
    """
    def bst_from_preorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, 0, len(preorder) - 1)

    # Prints inorder traversal of the constructed BST.
    def print_inorder(self, root: Optional[TreeNode]) -> None:
        # Empty subtree has nothing to print.
        if root is None:
            return

        self.print_inorder(root.left)
        print(root.val, end=" ")
        self.print_inorder(root.right)

    # Prints inorder traversal of the constructed BST.
    def print_tree(self, root: Optional[TreeNode]) -> None:
        self.print_inorder(root)


# Driver code starts
def main() -> None:
    preorder: List[int] = [8, 5, 1, 7, 10, 12]

    obj = Solution()
    root = obj.bst_from_preorder(preorder)

    obj.print_tree(root)


if __name__ == "__main__":
    main()

# Optimal Approach
# The previous approach keeps scanning to find where the left subtree ends. A better thought is: why search for the split again and again when the valid range of each subtree already tells the story?

# For any node in a BST:

# Its left subtree can only contain values smaller than that node.

# Its right subtree can only contain values greater than that node.

# So while reading preorder from left to right, keep a valid range for the current subtree. If the next value fits in that range, it belongs here. If it does not fit, that subtree is finished, and the value should be used by some ancestor's right subtree.

# The index moves forward only when a node is actually created. That is the key reason this approach becomes linear.

# Algorithm
# Keep one index that points to the next unused value in preorder. This avoids slicing arrays or rechecking old values.

# Start with the widest possible range, because the root can be any valid value.

# For each recursive call, check whether the next preorder value fits inside the allowed range. This check is needed because each subtree can only accept values allowed by its ancestors.

# If the value does not fit, return null without moving the index. This is important because the value may belong to another subtree that will be built later.

# If the value fits, create a node and move the index forward because this value has now been consumed.

# Build the left subtree with an upper bound equal to the current node's value, then build the right subtree with a lower bound equal to the current node's value.

# Return the node after both subtrees are connected.

from typing import List, Optional


class TreeNode:
    # Creates a tree node with left and right child links.
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class Solution:
    # Builds the subtree whose values must stay inside the given bounds.
    def build(
        self,
        preorder: List[int],
        lower: float,
        upper: float
    ) -> Optional[TreeNode]:
        # All preorder values are already used, so there is no subtree left.
        if self.index >= len(preorder):
            return None

        # Stores the next value that has not been used yet.
        value: int = preorder[self.index]

        # A value outside the range belongs to another subtree.
        if value <= lower or value >= upper:
            return None

        # The value fits this range, so it becomes the current root.
        root = TreeNode(value)

        # Move forward because this value is now used.
        self.index += 1

        root.left = self.build(preorder, lower, value)
        root.right = self.build(preorder, value, upper)

        return root

    """
    Builds a BST by consuming preorder values
    only when they fit the current valid range.
    """
    def bst_from_preorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Points to the next preorder value that still needs placement.
        self.index: int = 0

        return self.build(preorder, float("-inf"), float("inf"))

    # Prints inorder traversal of the constructed BST.
    def print_inorder(self, root: Optional[TreeNode]) -> None:
        # Empty subtree has nothing to print.
        if root is None:
            return

        self.print_inorder(root.left)
        print(root.val, end=" ")
        self.print_inorder(root.right)

    # Prints inorder traversal of the constructed BST.
    def print_tree(self, root: Optional[TreeNode]) -> None:
        self.print_inorder(root)


# Driver code starts
def main() -> None:
    preorder: List[int] = [8, 5, 1, 7, 10, 12]

    obj = Solution()
    root = obj.bst_from_preorder(preorder)

    obj.print_tree(root)


if __name__ == "__main__":
    main()