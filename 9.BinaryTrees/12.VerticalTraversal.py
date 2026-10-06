# Given the root of a binary tree, return its vertical order traversal from left to right.

# A coordinate is assigned to every node:

# The root is placed at row = 0, column = 0.

# The left child of a node at (row, column) is placed at (row + 1, column - 1).

# The right child is placed at (row + 1, column + 1).

# Nodes are grouped according to their column.

# Within each column:

# Nodes with a smaller row appear first.

# If multiple nodes have the same row and column, their values appear in ascending order.

# The traversal is returned as a list of columns from the smallest column to the largest.

# Example 1
# Input:
# root = [3, 9, 20, null, null, 15, 7]

# Output:
# [[9], [3, 15], [20], [7]]

# Explanation:
# Node 9 lies at column -1. Nodes 3 and 15 lie at column 0, with 3 appearing first because it has the smaller row. Node 20 lies at column 1, and node 7 lies at column 2.

# Example 2
# Input:
# root = [1, 2, 3, 4, 6, 5, 7]

# Output:
# [[4], [2], [1, 5, 6], [3], [7]]

# Explanation:
# Nodes 5 and 6 occupy the same row and column. Their values are therefore placed in ascending order as 5, 6. The columns are returned from left to right.

# Approach 1
# Vertical traversal depends on three pieces of information:

# column → row → value

# The column determines the vertical line to which a node belongs. The row determines its top-to-bottom position within that column, while the node value resolves ties when multiple nodes occupy the same row and column.

# Therefore, every node can be stored as:

# (column, row, value)

# Once all nodes have been collected, these entries can be sorted by column, then row, and finally value. This directly produces the ordering required by the problem.

# While the sorted entries are being converted into the final result, a variable previousColumn is used to remember the column of the previously processed entry. Whenever the current column differs from previousColumn, a new vertical list is started. This allows consecutive nodes belonging to the same column to be grouped together efficiently.

# Algorithm
# The tree is traversed while the row and column of every node are tracked, and each node is stored as (column, row, value) so that all required ordering information is preserved.

# For every left child, the coordinates are transformed to (row + 1, column - 1), while every right child is assigned (row + 1, column + 1).

# After traversal, all stored entries are sorted first by column, then by row, and finally by node value so that the required vertical ordering is obtained.

# A variable previousColumn is maintained while the sorted entries are processed. Whenever a different column is encountered, a new vertical list is created.

# Nodes having the same column are appended to the current vertical list, and all completed lists are stored from the smallest column to the largest.

# The grouped vertical lists are returned as the final traversal.Dry Run

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Stores every node with its
    # column, row, and value.
    def dfs(
        self,
        node,
        row,
        column,
        nodes
    ):
        if node is None:
            return

        nodes.append(
            (column, row, node.val)
        )

        # Moving left increases the row
        # and decreases the column.
        self.dfs(
            node.left,
            row + 1,
            column - 1,
            nodes
        )

        # Moving right increases both
        # the row and column.
        self.dfs(
            node.right,
            row + 1,
            column + 1,
            nodes
        )

    # Returns nodes grouped by vertical
    # columns from left to right.
    def vertical_traversal(self, root):
        if root is None:
            return []

        nodes = []

        self.dfs(
            root,
            0,
            0,
            nodes
        )

        # Tuple sorting follows column,
        # then row, then value.
        nodes.sort()

        answer = []
        previous_column = None

        # A new group is started whenever
        # the column changes.
        for column, row, value in nodes:
            if (
                previous_column is None
                or column != previous_column
            ):
                answer.append([])
                previous_column = column

            answer[-1].append(value)

        return answer


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()

    print(
        solution.vertical_traversal(root)
    )

# Approach 2
# Instead of collecting every node first and sorting everything afterward, the nodes can be organized according to their coordinates during traversal itself.

# A nested ordered structure is used:

# map<int, map<int, multiset<int>>>

# Each level of this structure has a specific purpose:

# The outer map uses the column as its key, so vertical lines remain ordered from left to right.

# The inner map uses the row as its key, so nodes within each column remain ordered from top to bottom.

# The multiset stores values of nodes that share the exact same (column, row) position and automatically keeps those values in ascending order.

# This structure directly matches the ordering rules of the problem and avoids requiring one global sort over all node coordinates.

# BFS can then be used to traverse the tree while carrying each node's row and column.

# Algorithm
# If the root is non-null, a queue is initialized with the root at (row = 0, column = 0) so that coordinate information can be carried during BFS.

# A nested ordered structure of the form column → row → sorted values is maintained, allowing columns, rows, and equal-position values to remain ordered automatically.

# Whenever a node is removed from the queue, its value is inserted into the collection corresponding to its current (column, row) position.

# For every left child, (row + 1, column - 1) is assigned, while every right child is assigned (row + 1, column + 1), preserving their correct vertical positions.

# After traversal, the outer map is processed from the smallest column to the largest, while each inner map is processed from the smallest row to the largest. Values stored in each multiset are appended in their already sorted order.

# Each completed column is added to the final result, producing the required vertical traversal from left to right.

from collections import defaultdict, deque
import heapq


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # Organizes nodes directly by
    # column, row, and sorted value.
    def vertical_traversal(self, root):
        if root is None:
            return []

        # Each column contains rows, while
        # each position uses a min-heap for ties.
        nodes = defaultdict(
            lambda: defaultdict(list)
        )

        queue = deque([
            (root, 0, 0)
        ])

        # BFS carries the coordinate
        # of every visited node.
        while queue:
            node, row, column = queue.popleft()

            heapq.heappush(
                nodes[column][row],
                node.val
            )

            # A left child moves one row down
            # and one column to the left.
            if node.left is not None:
                queue.append(
                    (
                        node.left,
                        row + 1,
                        column - 1
                    )
                )

            # A right child moves one row down
            # and one column to the right.
            if node.right is not None:
                queue.append(
                    (
                        node.right,
                        row + 1,
                        column + 1
                    )
                )

        answer = []

        # Columns and rows are sorted, while
        # heap extraction resolves value ties.
        for column in sorted(nodes):
            column_values = []

            for row in sorted(nodes[column]):
                values = nodes[column][row]

                while values:
                    column_values.append(
                        heapq.heappop(values)
                    )

            answer.append(column_values)

        return answer


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()

    print(
        solution.vertical_traversal(root)
    )