# Given the roots of two binary trees, p and q, determine whether the two trees are identical.

# Two binary trees are identical only if:

# Their structure is exactly the same.

# Nodes at corresponding positions contain the same values.

# If both trees are empty, they are considered identical. If only one tree is empty, they are not identical.

# Example 1
# Input: p = [1, 2, 3], q = [1, 2, 3]

# Output: true

# Explanation: Both trees have the same structure, and every pair of corresponding nodes contains the same value. Therefore, the trees are identical.

# Example 2
# Input: p = [1, 2], q = [1, null, 2]

# Output: false

# Explanation: Both trees contain the values 1 and 2, but their structures are different. In p, node 2 is the left child of 1, while in q, node 2 is the right child of 1. Therefore, the trees are not identical.

# Approach 1
# Two trees are identical only when the nodes at every corresponding position match in both existence and value.

# Recursion fits naturally because after comparing the current pair of nodes, the same condition must hold for their left subtrees and their right subtrees.

# If both current nodes are null, that position matches. If only one is null, the structure differs. Otherwise, their values must match before checking the corresponding children.

# Algorithm
# If both p and q are null, return true because both subtrees are empty.

# If exactly one of them is null, return false because their structures differ.

# Compare p.val and q.val; return false immediately if the values are different.

# Recursively compare p.left with q.left to verify the left subtrees.

# Recursively compare p.right with q.right to verify the right subtrees.

# Return true only if both recursive comparisons are true.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Compares corresponding nodes
    # of both trees recursively.
    def is_same_tree(self, p, q):
        # Both trees are empty
        # at this position.
        if p is None and q is None:
            return True

        # Only one node exists,
        # so the structures differ.
        if p is None or q is None:
            return False

        # Different values make
        # the trees non-identical.
        if p.val != q.val:
            return False

        # Both corresponding subtrees
        # must also be identical.
        return (
            self.is_same_tree(p.left, q.left)
            and self.is_same_tree(p.right, q.right)
        )


if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    solution = Solution()

    print(solution.is_same_tree(p, q))

# Approach 2
# The recursive solution compares corresponding positions in both trees. The same comparison can be performed iteratively by storing pairs of corresponding nodes in a queue.

# For every pair, first verify that their structure matches and then compare their values. If the pair is valid, their left children are paired together and their right children are paired together.

# Any mismatch can return false immediately.

# Algorithm
# Push the initial pair (p, q) into a queue because comparison begins at the roots.

# Remove one pair at a time from the queue.

# If both nodes are null, continue because that position matches; if exactly one is null, return false.

# If both nodes exist but their values differ, return false.

# Push their left children as one pair and their right children as another pair so corresponding positions remain aligned.

# If every pair is processed without a mismatch, return true.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Compares corresponding nodes
    # using breadth-first traversal.
    def is_same_tree(self, p, q):
        queue = deque([(p, q)])

        # Process one corresponding
        # node pair at a time.
        while queue:
            node_p, node_q = queue.popleft()

            # Both positions are empty,
            # so this pair matches.
            if node_p is None and node_q is None:
                continue

            # Only one node exists,
            # so the structures differ.
            if node_p is None or node_q is None:
                return False

            # Corresponding nodes must
            # contain the same value.
            if node_p.val != node_q.val:
                return False

            # Keep corresponding children
            # paired for later comparison.
            queue.append(
                (node_p.left, node_q.left)
            )

            queue.append(
                (node_p.right, node_q.right)
            )

        return True


if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    solution = Solution()

    print(solution.is_same_tree(p, q))

# Approach 3
# Recursive DFS does not require level-order processing; it only needs corresponding positions from the two trees to remain paired.

# The recursion stack can therefore be replaced with an explicit stack containing (nodeFromP, nodeFromQ) pairs. Each pair undergoes the same structural and value checks as in the recursive solution.

# This avoids recursion while preserving the depth-first comparison order.

# Algorithm
# Push (p, q) into a stack to begin comparison from the roots.

# Pop one pair at a time while the stack is not empty.

# If both nodes are null, continue; if exactly one is null, return false.

# If both nodes exist but their values differ, return false.

# Push the corresponding right children first and the corresponding left children afterward, so the left pair is processed next and the traversal follows depth-first order.

# If the stack becomes empty without finding any mismatch, return true.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Compares corresponding nodes
    # using an explicit DFS stack.
    def is_same_tree(self, p, q):
        stack = [(p, q)]

        # Process one corresponding
        # node pair at a time.
        while stack:
            node_p, node_q = stack.pop()

            # Both positions are empty,
            # so this pair matches.
            if node_p is None and node_q is None:
                continue

            # Only one node exists,
            # so the structures differ.
            if node_p is None or node_q is None:
                return False

            # Corresponding nodes must
            # contain the same value.
            if node_p.val != node_q.val:
                return False

            # Push right first so
            # the left pair is checked next.
            stack.append(
                (node_p.right, node_q.right)
            )

            stack.append(
                (node_p.left, node_q.left)
            )

        return True


if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    solution = Solution()

    print(solution.is_same_tree(p, q))

