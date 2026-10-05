# Given the root of a binary tree, return its boundary traversal in anti-clockwise order, starting from the root.

# The boundary consists of:

# The root node.

# The left boundary, excluding leaf nodes.

# All leaf nodes from left to right.

# The right boundary, excluding leaf nodes, added in reverse order.

# Each node must appear only once in the traversal.

# Example 1
# Input: root = [1, 2, 3, 4, 5, 6, 7]

# Output: [1, 2, 4, 5, 6, 7, 3]

# Explanation: The root 1 is added first. The left boundary contributes 2, the leaf nodes from left to right are 4, 5, 6, 7, and the right boundary contributes 3 in bottom-up order.

# Example 2
# Input: root = [1, 2, 3, null, 4, 5, null]

# Output: [1, 2, 4, 5, 3]

# Explanation: Node 2 belongs to the left boundary, leaves 4 and 5 are added from left to right, and node 3 forms the right boundary. Leaf nodes are not repeated in the side boundaries.

# Approach 1
# The anti-clockwise boundary can naturally be divided into three sections after the root:

# Left Boundary → Leaf Nodes → Reversed Right Boundary

# Different traversal rules are required for these sections.

# For the left boundary, the outermost nodes are followed from top to bottom by preferring the left child. If a left child is unavailable, the right child is followed instead. Leaf nodes are excluded because they are collected separately.

# For the right boundary, the outermost nodes are similarly followed by preferring the right child. However, these nodes are discovered from top to bottom while the required boundary order is bottom to top. Therefore, a temporary array called rightBoundary is used. It stores the right-boundary nodes during downward traversal so that they can later be added in reverse order.

# Leaf nodes are collected separately through DFS from left to right. By excluding leaves from both side boundaries, every node is guaranteed to appear only once.

# Algorithm
# An empty result is returned when the tree is empty. The root is added separately when it is not a leaf so that it is not duplicated during leaf collection.

# Starting from root.left, the left boundary is followed by preferring the left child and using the right child only when the left child is absent. Only non-leaf nodes are added because leaf nodes are handled separately.

# A DFS traversal of the complete tree is performed so that all leaf nodes are collected from left to right.

# Starting from root.right, the right boundary is followed by preferring the right child and using the left child when the right child is absent. Non-leaf nodes are stored in the temporary rightBoundary array as they are encountered from top to bottom.

# The values stored in rightBoundary are then appended in reverse order so that the right boundary appears from bottom to top and the anti-clockwise traversal is completed.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Checks whether a node
    # has no children.
    def is_leaf(self, node):
        return (
            node is not None
            and node.left is None
            and node.right is None
        )

    # Adds non-leaf nodes from the
    # left boundary in top-down order.
    def add_left_boundary(
        self,
        root,
        boundary
    ):
        current = root.left

        # The outermost available child
        # continues the left boundary.
        while current is not None:
            # Leaves are collected separately,
            # so they are skipped here.
            if not self.is_leaf(current):
                boundary.append(current.val)

            if current.left is not None:
                current = current.left
            else:
                current = current.right

    # Collects all leaf nodes
    # from left to right.
    def add_leaves(
        self,
        node,
        boundary
    ):
        if node is None:
            return

        # A leaf belongs directly
        # to the leaf section.
        if self.is_leaf(node):
            boundary.append(node.val)
            return

        self.add_leaves(
            node.left,
            boundary
        )

        self.add_leaves(
            node.right,
            boundary
        )

    # Adds the right boundary
    # in required bottom-up order.
    def add_right_boundary(
        self,
        root,
        boundary
    ):
        current = root.right
        right_boundary = []

        # right_boundary stores nodes top-down.
        # They are reversed for bottom-up order.
        while current is not None:
            # Leaves are collected separately,
            # so they are skipped here.
            if not self.is_leaf(current):
                right_boundary.append(
                    current.val
                )

            if current.right is not None:
                current = current.right
            else:
                current = current.left

        # Reverse traversal places the
        # right boundary from bottom to top.
        for value in reversed(right_boundary):
            boundary.append(value)

    # Returns the anti-clockwise
    # boundary traversal of the tree.
    def boundary_traversal(self, root):
        if root is None:
            return []

        boundary = []

        # A non-leaf root is added here.
        # A single-node root is added as a leaf.
        if not self.is_leaf(root):
            boundary.append(root.val)

        self.add_left_boundary(
            root,
            boundary
        )

        self.add_leaves(
            root,
            boundary
        )

        self.add_right_boundary(
            root,
            boundary
        )

        return boundary


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    solution = Solution()

    print(
        solution.boundary_traversal(root)
    )

# Approach 2
# The three boundary sections can also be generated during a single DFS by carrying information about whether the current node belongs to the outer left or right boundary.

# Two boolean variables are used for this purpose:

# isLeftBoundary indicates whether the current node lies on the outer left boundary of the remaining subtree. Such a node must be added before its descendants because the left boundary is required from top to bottom.

# isRightBoundary indicates whether the current node lies on the outer right boundary. Such a node must be added after its descendants because the right boundary is required from bottom to top.

# These flags are propagated carefully. When a node belongs to the left boundary, its left child continues that boundary whenever it exists; otherwise, the right child becomes the new outermost left-boundary node. The opposite rule is applied for isRightBoundary.

# Leaf nodes are handled separately inside the same DFS. Once a leaf is added, processing of that node is completed immediately so that it cannot also be inserted as a left- or right-boundary node.

# Algorithm
# An empty result is returned when root is null. The root is added first, and processing is completed immediately when it is the only node.

# DFS is started on root.left with isLeftBoundary = true and on root.right with isRightBoundary = true, so the outer boundary roles of both sides are identified from the beginning.

# When a leaf node is reached, its value is added immediately and that call is completed so that the same node cannot be added again as a side-boundary node.

# A node marked by isLeftBoundary is added before its children are processed, because the left boundary must appear from top to bottom.

# The boundary flags are propagated according to the outermost available child: the left-boundary role is passed to the left child when possible and otherwise to the right child, while the symmetric rule is applied to the right-boundary role.

# A node marked by isRightBoundary is added only after its children have been processed, causing right-boundary nodes to appear automatically in bottom-up order.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Checks whether a node
    # has no children.
    def is_leaf(self, node):
        return (
            node is not None
            and node.left is None
            and node.right is None
        )

    # Builds the complete boundary
    # using boundary-role flags.
    def dfs(
        self,
        node,
        is_left_boundary,
        is_right_boundary,
        boundary
    ):
        if node is None:
            return

        # Leaves are added exactly once
        # and need no boundary-role handling.
        if self.is_leaf(node):
            boundary.append(node.val)
            return

        # Left-boundary nodes are added before
        # descendants for top-down order.
        if is_left_boundary:
            boundary.append(node.val)

        # A missing left child makes the
        # right child continue the left boundary.
        left_child_is_left_boundary = (
            is_left_boundary
        )

        right_child_is_left_boundary = (
            is_left_boundary
            and node.left is None
        )

        # A missing right child makes the
        # left child continue the right boundary.
        left_child_is_right_boundary = (
            is_right_boundary
            and node.right is None
        )

        right_child_is_right_boundary = (
            is_right_boundary
        )

        self.dfs(
            node.left,
            left_child_is_left_boundary,
            left_child_is_right_boundary,
            boundary
        )

        self.dfs(
            node.right,
            right_child_is_left_boundary,
            right_child_is_right_boundary,
            boundary
        )

        # Right-boundary nodes are added after
        # recursion for bottom-up order.
        if is_right_boundary:
            boundary.append(node.val)

    # Returns the anti-clockwise
    # boundary using a single DFS.
    def boundary_traversal(self, root):
        if root is None:
            return []

        # A single-node tree contains
        # only one boundary node.
        if self.is_leaf(root):
            return [root.val]

        boundary = [root.val]

        self.dfs(
            root.left,
            True,
            False,
            boundary
        )

        self.dfs(
            root.right,
            False,
            True,
            boundary
        )

        return boundary


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    solution = Solution()

    print(
        solution.boundary_traversal(root)
    )