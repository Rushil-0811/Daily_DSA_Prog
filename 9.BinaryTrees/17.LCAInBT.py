# Lowest Common Ancestor in a Binary Tree
# Given the root of a binary tree and two nodes p and q present in the tree, find their Lowest Common Ancestor (LCA).

# The LCA is the deepest node in the tree that is an ancestor of both p and q.

# A node can also be considered an ancestor of itself. Therefore, if one of the given nodes lies on the path from the root to the other node, that node itself can be the LCA.

# Example 1
# Input:
# root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1

# Output:
# 3

# Explanation:
# Node 3 is the deepest node that is an ancestor of both nodes 5 and 1, so their Lowest Common Ancestor is 3.

# Example 2
# Input:
# root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4

# Output:
# 5

# Explanation:
# Node 5 is an ancestor of node 4. Since a node can be considered an ancestor of itself, the Lowest Common Ancestor is 5.

# Approach 1
# Every node in a binary tree has exactly one path from the root.

# Two lists, pathP and pathQ, are maintained. pathP stores the sequence of ancestors from the root to node p, while pathQ stores the corresponding sequence from the root to node q.

# Once both paths are available, they remain identical from the root until their deepest common node. After that point, either the paths move into different branches or one of them ends.

# Therefore, the last matching node in pathP and pathQ is the Lowest Common Ancestor.

# This approach follows the definition directly, but two complete root-to-node paths must first be found and stored.

# Algorithm
# A path named pathP is constructed using DFS so that the complete ancestor chain from the root to node p is stored.

# A second path named pathQ is constructed in the same way so that the ancestor chain from the root to node q is available.

# Both paths are compared from their first position because their common prefix represents the nodes that are ancestors of both targets.

# Matching nodes are processed until different nodes are encountered or one of the paths ends.

# The last matching node is identified as the deepest node shared by both ancestor chains.

# That node is returned as the Lowest Common Ancestor.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Stores the root-to-target path
    # using DFS and backtracking.
    def find_path(
        self,
        node,
        target,
        path
    ):
        if node is None:
            return False

        path.append(node)

        # The required ancestor chain is complete
        # once the target node is reached.
        if node is target:
            return True

        if (
            self.find_path(node.left, target, path)
            or self.find_path(node.right, target, path)
        ):
            return True

        # The node is removed when the target
        # is not present in this subtree.
        path.pop()

        return False

    # Finds the last common node in
    # the root-to-p and root-to-q paths.
    def lowest_common_ancestor(
        self,
        root,
        p,
        q
    ):
        path_p = []
        path_q = []

        self.find_path(root, p, path_p)
        self.find_path(root, q, path_q)

        lca = None

        limit = min(
            len(path_p),
            len(path_q)
        )

        # Both paths share the same prefix
        # until their Lowest Common Ancestor.
        for i in range(limit):
            if path_p[i] is not path_q[i]:
                break

            lca = path_p[i]

        return lca


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left
    q = root.left.right.right

    solution = Solution()

    lca = solution.lowest_common_ancestor(
        root,
        p,
        q
    )

    print(lca.val)

# Approach 2
# If every node knew its parent, the search could be performed upward instead of repeatedly moving downward from the root.

# A mapping of:

# node → parent

# is first constructed.

# A queue named nodesQueue is used for a level-order traversal because it stores the nodes whose children still need to be processed while the parent relationships are being built.

# After the mapping has been constructed, an ancestors set is used to store every node encountered while moving from p toward the root. The set is chosen because it allows constant-time average membership checks when the ancestor chain of q is later examined.

# Node q is then moved upward through its parent links. The first node encountered that already exists in ancestors is the deepest node shared by both ancestor chains and is therefore the LCA.

# Algorithm
# A parent mapping is constructed using a queue-based level-order traversal (BFS) so that every visited child is associated with its parent.

# A queue named nodesQueue is maintained because it stores nodes whose children still need to be examined while the parent mapping is being created.

# BFS is continued until parent information for both p and q has been discovered.

# A set named ancestors is then created to store all nodes encountered while moving upward from p, allowing nodes in this ancestor chain to be checked efficiently.

# Starting from p, parent links are repeatedly followed and every visited node is inserted into ancestors.

# Starting from q, parent links are followed upward until a node already present in ancestors is encountered.

# The first such node is returned because it is the lowest ancestor shared by both target nodes.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Builds parent relationships using BFS
    # and compares the ancestor chains.
    def lowest_common_ancestor(
        self,
        root,
        p,
        q
    ):
        parent = {
            root: None
        }

        # nodes_queue stores nodes whose children
        # still need parent information.
        nodes_queue = deque([root])

        # BFS continues until both target nodes
        # have known parent relationships.
        while p not in parent or q not in parent:
            node = nodes_queue.popleft()

            if node.left is not None:
                parent[node.left] = node
                nodes_queue.append(node.left)

            if node.right is not None:
                parent[node.right] = node
                nodes_queue.append(node.right)

        # ancestors stores every node on
        # p's path from itself to the root.
        ancestors = set()

        current = p

        while current is not None:
            ancestors.add(current)
            current = parent[current]

        current = q

        # The first node from q's ancestor chain
        # already seen from p is the LCA.
        while current not in ancestors:
            current = parent[current]

        return current


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left
    q = root.left.right.right

    solution = Solution()

    lca = solution.lowest_common_ancestor(
        root,
        p,
        q
    )

    print(lca.val)

# Optimal Approach
# The LCA can be found without storing complete root-to-node paths or explicit parent relationships.

# For every recursive call, the following question is considered:

# Does this subtree contain p, q, or their LCA?

# Two variables, leftResult and rightResult, are used to store what is returned from the left and right subtree searches. These names make their purpose explicit: each variable represents useful information discovered within its respective subtree.

# If the current node is p or q, that node is returned upward because one of the required targets has been found and may itself become the LCA.

# If both leftResult and rightResult are non-null, one target has been found on each side. Therefore, the current node is the deepest point where the two branches meet.

# If only one result is non-null, that result is propagated upward because both targets may lie in that branch, or one target may be an ancestor of the other.

# Algorithm
# If the current node is null, null is returned because the subtree contains neither target.

# If the current node is equal to p or q, the current node is returned because one target has been found and may itself be the Lowest Common Ancestor.

# The result of searching the left subtree is stored in leftResult, while the result of searching the right subtree is stored in rightResult, so information found in both branches can be compared.

# If both leftResult and rightResult are non-null, the current node is returned because the two target nodes have been found in different branches.

# If only leftResult is non-null, it is propagated upward because the useful result lies in the left subtree.

# Otherwise, rightResult is propagated upward because the useful result lies in the right subtree or neither target has been found.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Returns p, q, or their LCA
    # when found inside the current subtree.
    def lowest_common_ancestor(
        self,
        root,
        p,
        q
    ):
        if root is None:
            return None

        # A target node may itself
        # be the Lowest Common Ancestor.
        if root is p or root is q:
            return root

        # left_result and right_result capture
        # useful nodes found in each subtree.
        left_result = self.lowest_common_ancestor(
            root.left,
            p,
            q
        )

        right_result = self.lowest_common_ancestor(
            root.right,
            p,
            q
        )

        # Non-null results from both sides mean
        # the targets lie in different branches.
        if (
            left_result is not None
            and right_result is not None
        ):
            return root

        # A single non-null result is propagated
        # upward until another target is found.
        if left_result is not None:
            return left_result

        return right_result


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left
    q = root.left.right.right

    solution = Solution()

    lca = solution.lowest_common_ancestor(
        root,
        p,
        q
    )

    print(lca.val)