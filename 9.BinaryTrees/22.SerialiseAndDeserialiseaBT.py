# Design a method to serialize a binary tree into a string and another method to deserialize that string back into the original binary tree.

# The serialized representation must preserve:

# The value of every node

# The exact structure of the tree

# Every missing left and right child

# After deserialization, the reconstructed tree must be structurally identical to the original tree.

# In this article, tokens are separated using commas, but a trailing comma is not added. An empty tree is represented consistently as:

# "#"

# Example 1
# Input: root = [1, 2, 3, null, null, 4, 5]

# Output: "1,2,#,#,3,4,#,#,5,#,#"

# Explanation: Deserializing this string reconstructs root = [1, 2, 3, null, null, 4, 5].

# Example 2
# Input: root = []

# Output: "#"

# Explanation: The marker # represents an empty tree.

# Approach 1
# A normal preorder traversal records nodes in the following order:

# Root → Left → Right

# However, node values alone are insufficient to preserve the structure.

# For example, consider one tree in which node 2 is the left child of node 1 and another tree in which node 2 is the right child of node 1.

# Both trees produce:

# 1,2

# when missing children are ignored.

# To remove this ambiguity, every null child is recorded using a special marker such as #.

# The preorder sequence then contains enough information to identify both the node values and the missing-child positions.

# During deserialization, the tokens are read in the same order. A value creates a node, while # represents a missing child. The left subtree is reconstructed before the right subtree, matching the preorder structure.

# Algorithm
# Serialization
# The tree is traversed in preorder so that every node is recorded before its left and right subtrees.

# When a null node is reached, # is appended so that the missing-child position is preserved.

# When a non-null node is reached, its value is appended.

# The left subtree is serialized before the right subtree.

# All recorded tokens are joined using commas without adding a trailing comma.

# For an empty root, "#" is returned.

# Deserialization
# The serialized string is split into tokens, and an index is maintained for the next unread token.

# When # is encountered, null is returned because the current child position is empty.

# Otherwise, a node is created using the current token.

# The left subtree is reconstructed first because it appears before the right subtree in preorder.

# The right subtree is then reconstructed using the remaining tokens.

# The reconstructed node is returned to its parent call.

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # Converts the binary tree into a preorder string.
    def serialize(
        self,
        root: TreeNode | None
    ) -> str:
        tokens = []

        # Records nodes while preserving every missing child.
        def dfs(node: TreeNode | None) -> None:
            # Record a marker when the current child is missing.
            if node is None:
                tokens.append("#")
                return

            tokens.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(tokens)

    # Reconstructs the original tree from the serialized string.
    def deserialize(
        self,
        data: str
    ) -> TreeNode | None:
        tokens = data.split(",")
        index = 0

        # Builds one subtree from the preorder token sequence.
        def dfs() -> TreeNode | None:
            nonlocal index

            # A null marker means this child does not exist.
            if tokens[index] == "#":
                index += 1
                return None

            root = TreeNode(int(tokens[index]))
            index += 1

            # Preorder stores the left subtree before the right subtree.
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()


# Prints the reconstructed tree in preorder for verification.
def print_preorder(root: TreeNode | None) -> None:
    # Stop after reaching an empty subtree.
    if root is None:
        return

    print(root.val, end=" ")

    print_preorder(root.left)
    print_preorder(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Solution()

    data = solution.serialize(root)
    print(data)

    new_root = solution.deserialize(data)

    print_preorder(new_root)

# Approach 2
# The tree can also be serialized level by level using BFS.

# A queue is used to process nodes from top to bottom. For every non-null node, its value is recorded and its two child positions are added to the queue. When a child is missing, # is recorded.

# These null markers preserve the exact left and right positions of every child.

# During deserialization, the first token is used to create the root. The remaining tokens are consumed in pairs for every parent removed from the queue:

# The first token represents its left child.

# The second token represents its right child.

# The tree is therefore reconstructed level by level.

# For the tree:

# root = [1, 2, 3, null, null, 4, 5]

# one valid BFS serialization is:

# "1,2,3,#,#,4,5,#,#,#,#"

# No trailing comma is added.

# Algorithm
# Serialization
# If the tree is empty, "#" is returned.

# The root is placed into a queue so that level-order processing can begin.

# A non-null node’s value is recorded, and both of its child positions are added to the queue.

# When a null position is removed from the queue, # is recorded.

# Processing is continued until the queue becomes empty.

# All recorded tokens are joined using commas without adding a trailing comma.

# Deserialization
# If the serialized string is "#", null is returned.

# The root is created using the first token and is placed into a queue.

# One parent is removed from the queue, and the next token is read for its left child.

# If the token is not #, a left child is created and added to the queue.

# The following token is read for the right child.

# If that token is not #, a right child is created and added to the queue.

# Processing is continued until all tokens have been consumed.

# The reconstructed root is returned.

from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # Converts the tree into a level-order string with null markers.
    def serialize(
        self,
        root: TreeNode | None
    ) -> str:
        # An empty tree is represented by a single null marker.
        if root is None:
            return "#"

        tokens = []
        queue = deque([root])

        # Process every tree position needed to preserve its structure.
        while queue:
            node = queue.popleft()

            # Preserve the position of a missing child.
            if node is None:
                tokens.append("#")
                continue

            tokens.append(str(node.val))

            queue.append(node.left)
            queue.append(node.right)

        return ",".join(tokens)

    # Reconstructs the tree level by level from the serialized string.
    def deserialize(
        self,
        data: str
    ) -> TreeNode | None:
        # A null marker represents an empty tree.
        if data == "#":
            return None

        tokens = data.split(",")

        root = TreeNode(int(tokens[0]))
        queue = deque([root])

        index = 1

        # Attach the next two tokens as children of each queued node.
        while queue and index < len(tokens):
            node = queue.popleft()

            # Create the left child only when its token is not null.
            if tokens[index] != "#":
                node.left = TreeNode(
                    int(tokens[index])
                )
                queue.append(node.left)

            index += 1

            # Create the right child only when its token is not null.
            if (
                index < len(tokens)
                and tokens[index] != "#"
            ):
                node.right = TreeNode(
                    int(tokens[index])
                )
                queue.append(node.right)

            index += 1

        return root


# Prints the reconstructed tree in preorder for verification.
def print_preorder(root: TreeNode | None) -> None:
    # Stop after reaching an empty subtree.
    if root is None:
        return

    print(root.val, end=" ")

    print_preorder(root.left)
    print_preorder(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Solution()

    data = solution.serialize(root)
    print(data)

    new_root = solution.deserialize(data)

    print_preorder(new_root)