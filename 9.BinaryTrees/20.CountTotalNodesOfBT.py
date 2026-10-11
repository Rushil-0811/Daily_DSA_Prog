# Given the root of a complete binary tree, determine the total number of nodes present in the tree.

# In a complete binary tree:

# Every level except possibly the last is completely filled.

# Nodes in the last level are placed as far left as possible.

# Example 1
# Input:
# root = [1, 2, 3, 4, 5, 6]

# Output:
# 6

# Explanation:
# The binary tree contains a total of 6 nodes.

# Example 2
# Input:
# root = [1]

# Output:
# 1

# Explanation:
# The tree contains only its root node, so the total number of nodes is 1.

# Brute Force Approach
# The most direct way to count the nodes is to visit every node once.

# For any non-null node, the total number of nodes in its subtree is:

# 1 + nodes in left subtree + nodes in right subtree

# The 1 represents the current node, while the remaining two terms represent the nodes belonging to its left and right subtrees.

# This method works for every binary tree and does not make use of the special structure of a complete binary tree. Therefore, even when an entire subtree is perfectly filled and its size could be calculated directly, every node inside it is still visited.

# Algorithm
# If the current node is null, 0 is returned because no node is present in that subtree.

# The number of nodes in the left subtree is recursively calculated.

# The number of nodes in the right subtree is recursively calculated.

# 1 is added for the current node along with the counts obtained from both subtrees.

# The resulting count is returned to the parent recursive call.

# Once the root has been processed, the returned value represents the total number of nodes in the tree.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Counts every node by recursively
    # combining the left and right subtree counts.
    def count_nodes(self, root):
        if root is None:
            return 0

        left_count = self.count_nodes(root.left)
        right_count = self.count_nodes(root.right)

        return 1 + left_count + right_count


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    solution = Solution()

    print(
        solution.count_nodes(root)
    )

# Optimal Approach
# The structure of a complete binary tree can be used to avoid visiting every node.

# For each subtree, two heights are calculated:

# leftHeight represents the number of nodes encountered while repeatedly moving through left children from the current node.

# rightHeight represents the number of nodes encountered while repeatedly moving through right children from the current node.

# If leftHeight and rightHeight are equal, the current subtree is a perfect binary tree.

# A perfect binary tree with height H, where height represents the number of nodes or levels along the extreme path, contains:

# 2^H - 1

# nodes.

# Therefore, when equal heights are found, the entire subtree can be counted immediately without traversing every node inside it.

# If the two heights are different, the current subtree is not perfect. Its left and right subtrees are then processed recursively.

# Because the original tree is complete, many large subtrees are detected as perfect and counted directly, reducing the amount of traversal required.

# Algorithm
# If the current node is null, 0 is returned because the subtree contains no nodes.

# The value of leftHeight is calculated by repeatedly following left-child pointers from the current node.

# The value of rightHeight is calculated by repeatedly following right-child pointers from the current node.

# If leftHeight and rightHeight are equal, the subtree is identified as perfect and its node count is calculated directly as 2^leftHeight - 1.

# If the two heights are different, the left and right subtrees are recursively processed because the current subtree cannot be counted directly using the perfect-tree formula.

# In this case, 1 + countNodes(root->left) + countNodes(root->right) is returned, where 1 represents the current node and the recursive calls count the nodes in both subtrees.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Measures the extreme left height
    # of the current subtree.
    def get_left_height(self, node):
        height = 0

        # Following only left children gives
        # the extreme left height of this subtree.
        while node is not None:
            height += 1
            node = node.left

        return height

    # Measures the extreme right height
    # of the current subtree.
    def get_right_height(self, node):
        height = 0

        # Following only right children gives
        # the extreme right height of this subtree.
        while node is not None:
            height += 1
            node = node.right

        return height

    # Uses the complete-tree property to count
    # perfect subtrees without visiting every node.
    def count_nodes(self, root):
        if root is None:
            return 0

        left_height = self.get_left_height(root)
        right_height = self.get_right_height(root)

        # Equal extreme heights mean this complete
        # subtree is a perfect binary tree.
        if left_height == right_height:

            # A perfect tree with left_height levels
            # contains 2^left_height - 1 nodes.
            return (1 << left_height) - 1

        # When the subtree is not perfect, both sides
        # are counted recursively along with the root.
        return (
            1
            + self.count_nodes(root.left)
            + self.count_nodes(root.right)
        )


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    solution = Solution()

    print(
        solution.count_nodes(root)
    )

