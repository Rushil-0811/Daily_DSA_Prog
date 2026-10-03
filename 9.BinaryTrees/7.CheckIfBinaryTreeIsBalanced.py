# Given the root of a binary tree, determine whether it is height-balanced.

# A binary tree is height-balanced if, for every node, the absolute difference between the heights of its left and right subtrees is at most 1.

# In other words, for every node:

# |leftHeight - rightHeight| <= 1

# If even one node violates this condition, the entire tree is considered unbalanced.

# Example 1
# Input: root = [3, 9, 20, null, null, 15, 7]

# Output: true

# Explanation: The left subtree has height 1 and the right subtree has height 2. Their difference is 1, and every other node also satisfies the balance condition.

# Example 2
# Input: root = [1, 2, 2, 3, 3, null, null, 4, 4]

# Output: false

# Explanation: At one of the nodes, the left subtree becomes more than one level deeper than the right subtree. Since the height difference exceeds 1, the tree is not height-balanced.

# Approach 1
# The balance condition must be verified at every node.

# For the current node, first calculate the heights of its left and right subtrees. If their difference is greater than 1, the tree is immediately unbalanced.

# Even if the current node satisfies the condition, the same check must still be performed inside both subtrees because an imbalance may exist deeper in the tree.

# The drawback is that subtree heights are calculated repeatedly for different ancestors, creating unnecessary work.

# Algorithm
# If root is null, return true because an empty tree is balanced.

# Use a helper function height that returns the height of a subtree.

# Calculate leftHeight and rightHeight for the current node.

# If abs(leftHeight - rightHeight) > 1, return false because the current node violates the balance condition.

# Recursively verify that both the left and right subtrees are balanced.

# Return true only if the current node and both subtrees satisfy the condition.

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def _height(self, root: TreeNode | None) -> int:
        # Height is needed to check the current node's balance.
        if root is None:
            return 0

        return 1 + max(
            self._height(root.left),
            self._height(root.right)
        )

    def is_balanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        left_height = self._height(root.left)
        right_height = self._height(root.right)

        # This node violates the balance condition.
        if abs(left_height - right_height) > 1:
            return False

        # Every node in both subtrees must also be balanced.
        return (
            self.is_balanced(root.left)
            and self.is_balanced(root.right)
        )


if __name__ == "__main__":
    """
            1
           / \
          2   2
         /     \
        3       3
       /
      4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)

    solution = Solution()

    print(solution.is_balanced(root))

# Approach 2
# The Approach 1 performs two related tasks separately:

# calculate subtree heights,

# check whether those subtrees are balanced.

# Both can instead be handled during the same post-order traversal.

# For every node, first obtain the heights of its left and right subtrees. If either subtree is already unbalanced, return a special value -1 immediately.

# Otherwise, check the current height difference. If it exceeds 1, return -1; if not, return the normal subtree height.

# This works because valid subtree heights are always 0 or greater, so -1 can safely represent an unbalanced subtree.

# Algorithm
# Create a helper checkHeight that returns the subtree height when balanced and -1 when unbalanced.

# If the current node is null, return 0 because an empty subtree has height zero.

# Compute leftHeight; if it is -1, return -1 immediately because the left subtree is already unbalanced.

# Compute rightHeight; if it is -1, return -1 for the same reason.

# If abs(leftHeight - rightHeight) > 1, return -1; otherwise return 1 + max(leftHeight, rightHeight).

# The complete tree is balanced only if checkHeight(root) != -1.

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def _check_height(self, root: TreeNode | None) -> int:
        # Return -1 to propagate an imbalance upward.
        if root is None:
            return 0

        left_height = self._check_height(root.left)

        if left_height == -1:
            return -1

        right_height = self._check_height(root.right)

        if right_height == -1:
            return -1

        # The current subtree is invalid if the difference exceeds one.
        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    def is_balanced(self, root: TreeNode | None) -> bool:
        return self._check_height(root) != -1


if __name__ == "__main__":
    """
            1
           / \
          2   2
         /     \
        3       3
       /
      4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)

    solution = Solution()

    print(solution.is_balanced(root))

# Approach 3
# The Optimized DFS works in post-order because the height of a node can be determined only after the heights of its children are known.

# The same order can be reproduced without recursion by using a stack. Each stack entry stores a node together with a flag indicating whether its children have already been processed.

# Once a node is processed after its children, their heights are available in a map. Those heights are used to check the balance condition and calculate the current node's height.

# This avoids recursion but requires additional storage for the height of processed nodes.

# Algorithm
# If root is null, return true.

# Use a stack containing (node, visited) pairs and a map heightMap to store computed subtree heights.

# When a node is first encountered, push it back with visited = true, then push its children so they are processed first.

# When the node is popped with visited = true, obtain its left and right heights from heightMap, using 0 for missing children.

# If their difference exceeds 1, return false; otherwise store 1 + max(leftHeight, rightHeight) as the current node's height.

# If every node is processed without finding a violation, return true.

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def is_balanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        # visited=True means both children are ready to use.
        nodes_stack = [(root, False)]
        height_map = {}

        while nodes_stack:
            node, visited = nodes_stack.pop()

            if not visited:
                nodes_stack.append((node, True))

                if node.right is not None:
                    nodes_stack.append((node.right, False))

                if node.left is not None:
                    nodes_stack.append((node.left, False))

            else:
                # Postorder guarantees child heights are already stored.
                left_height = (
                    height_map[node.left]
                    if node.left is not None
                    else 0
                )

                right_height = (
                    height_map[node.right]
                    if node.right is not None
                    else 0
                )

                if abs(left_height - right_height) > 1:
                    return False

                height_map[node] = 1 + max(
                    left_height,
                    right_height
                )

        return True


if __name__ == "__main__":
    """
            1
           / \
          2   2
         /     \
        3       3
       /
      4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)

    solution = Solution()

    print(solution.is_balanced(root))