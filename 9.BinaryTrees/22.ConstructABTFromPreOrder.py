# Given two integer arrays, preorder and inorder, representing the preorder and inorder traversals of the same binary tree, construct and return the original binary tree.

# All node values are distinct, and both traversals contain the same set of values.

# Recall:

# Preorder → Root, Left, Right

# Inorder → Left, Root, Right

# Example 1
# Input:
# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]

# Output:
# [3, 9, 20, null, null, 15, 7]

# Explanation:
# The first preorder value 3 becomes the root. Its position in inorder separates node 9 into the left subtree and nodes 15, 20, 7 into the right subtree. Repeating the same process reconstructs the complete tree.

# Example 2
# Input:
# preorder = [1, 2, 4, 5, 3]
# inorder = [4, 2, 5, 1, 3]

# Output:
# [1, 2, 3, 4, 5]

# Explanation:
# Node 1 is identified as the root from preorder. Its inorder position separates [4, 2, 5] as the left subtree and [3] as the right subtree.

# Brute Force Approach
# Preorder traversal provides the most important information first: the root of the current subtree.

# Once that root is located in inorder, the inorder traversal divides the current subtree into:

# Left Subtree | Root | Right Subtree

# This process can then be repeated recursively.

# A variable named preIndex is maintained to represent the index of the next unused element in preorder. Since preorder always visits the root before its children, preorder[preIndex] always gives the root of the subtree currently being constructed.

# Two variables, inStart and inEnd, represent the boundaries of the portion of the inorder array belonging to the current subtree. These boundaries prevent recursive calls from processing nodes that belong to some other subtree.

# For every newly selected root, its position is searched linearly between inStart and inEnd. This correctly divides the current subtree into its left and right portions.

# The repeated linear search makes this approach inefficient in the worst case.

# Algorithm
# A variable preIndex is initialized to 0 so that it points to the next unused root value in preorder.

# The variables inStart and inEnd are used to represent the current valid range in inorder from which a subtree must be constructed.

# If inStart > inEnd, null is returned because no nodes belong to that subtree.

# The value at preorder[preIndex] is selected as the current root, and preIndex is incremented so that the next preorder value can be used by a later recursive call.

# The current root value is searched linearly within the inorder range [inStart, inEnd], and its position is used to divide the range into left and right subtree portions.

# The left subtree is recursively constructed from [inStart, rootIndex - 1].

# The right subtree is recursively constructed from [rootIndex + 1, inEnd].

# After both child links have been assigned, the current root is returned to the parent recursive call.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Builds the tree using the current inorder range.
    def build(
        self,
        preorder,
        inorder,
        in_start,
        in_end
    ):
        if in_start > in_end:
            return None

        # preorder[pre_index] is the root
        # of the current subtree.
        root_value = preorder[self.pre_index]
        self.pre_index += 1

        root = TreeNode(root_value)

        root_index = in_start

        # The root position splits inorder
        # into left and right subtree ranges.
        while (
            root_index <= in_end
            and inorder[root_index] != root_value
        ):
            root_index += 1

        root.left = self.build(
            preorder,
            inorder,
            in_start,
            root_index - 1
        )

        root.right = self.build(
            preorder,
            inorder,
            root_index + 1,
            in_end
        )

        return root

    # Reconstructs the binary tree from
    # preorder and inorder traversals.
    def build_tree(self, preorder, inorder):
        self.pre_index = 0

        return self.build(
            preorder,
            inorder,
            0,
            len(inorder) - 1
        )


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    solution = Solution()

    root = solution.build_tree(
        preorder,
        inorder
    )

# Optimal Approach
# The expensive operation in the brute-force approach is repeatedly searching for each root inside the inorder traversal.

# Because all values are distinct, every value has exactly one position in inorder. Therefore, a hash map can be created before reconstruction begins:

# node value → inorder index

# This allows each root position to be found in O(1) average time.

# The variable preIndex again represents the index of the next unused preorder value. Since preorder follows Root → Left → Right, the value at preorder[preIndex] is always the root of the current subtree.

# The variables inStart and inEnd represent the left and right boundaries of the inorder section belonging to that subtree. Once the current root's inorder index is obtained from the hash map, these boundaries can be divided directly into the ranges belonging to the left and right subtrees.

# Therefore:

# preorder determines which node becomes the root,

# inorder determines which nodes belong to its left and right subtrees.

# Each node is created exactly once, and repeated inorder scanning is eliminated.

# Algorithm
# A hash map is constructed so that the inorder index of every node value can be accessed directly.

# A variable preIndex is initialized to 0 so that the next unused value in preorder can be selected as the root of each subtree.

# The variables inStart and inEnd are used to represent the inorder interval belonging to the subtree currently being constructed.

# If inStart > inEnd, null is returned because the current inorder interval contains no nodes.

# A new node is created using preorder[preIndex], and preIndex is incremented so that the next preorder value becomes available.

# The inorder position of the current root is obtained from the hash map in O(1) average time.

# The left subtree is recursively constructed using the inorder interval [inStart, rootIndex - 1].

# The right subtree is recursively constructed using [rootIndex + 1, inEnd].

# After both subtrees have been attached, the current root is returned.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Builds a subtree using its valid
    # interval in the inorder traversal.
    def build(
        self,
        preorder,
        in_start,
        in_end
    ):
        if in_start > in_end:
            return None

        # pre_index points to the next root
        # available in preorder.
        root_value = preorder[self.pre_index]
        self.pre_index += 1

        root = TreeNode(root_value)

        # The stored inorder position divides
        # the current subtree into two ranges.
        root_index = self.inorder_index[
            root_value
        ]

        root.left = self.build(
            preorder,
            in_start,
            root_index - 1
        )

        root.right = self.build(
            preorder,
            root_index + 1,
            in_end
        )

        return root

    # Reconstructs the tree using constant-time
    # average lookup of inorder positions.
    def build_tree(self, preorder, inorder):
        self.pre_index = 0
        self.inorder_index = {}

        # Each value is mapped to its unique
        # position in the inorder traversal.
        for i in range(len(inorder)):
            self.inorder_index[inorder[i]] = i

        return self.build(
            preorder,
            0,
            len(inorder) - 1
        )


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    solution = Solution()

    root = solution.build_tree(
        preorder,
        inorder
    )