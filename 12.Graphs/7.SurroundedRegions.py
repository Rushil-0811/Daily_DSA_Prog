# Given an R × C board containing X and O, capture every region of O cells completely surrounded by X.

# A region is formed by horizontal and vertical connections between O cells. A region touching any board boundary remains safe. Every remaining enclosed region must be changed from O to X in place.

# Example 1
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation: The bottom boundary cell remains safe. The middle region has no boundary path, so all middle O cells become X.

# Example 2
# Input: board = [["X","O","X"],["O","O","X"],["X","X","X"]]

# Output: [["X","O","X"],["O","O","X"],["X","X","X"]]

# Explanation: Every O cell connects to a boundary O, so no cell gets captured.

# Approach 1
# Boundary-connected O cells are safe because a surrounded region cannot touch any board border. Depth First Search begins from every boundary O and marks all reachable O cells with a temporary symbol such as #.

# After all safe regions are marked, a nested traversal converts the remaining O cells into X and restores every temporary marker to O.

# Algorithm
# Store the row count in R and the column count in C, allowing boundary validation and complete board traversal.

# Traverse the left and right borders across all rows and start DFS from every cell containing O, since such cells cannot belong to a surrounded region.

# Traverse the top and bottom borders across all columns and start DFS from every cell containing O, ensuring that all four board borders are covered.

# End the current DFS call when the row or column lies outside the board or when the current cell does not contain O, as such a cell cannot extend the safe region.

# Replace the current O with # before exploring neighboring cells. The temporary marker identifies a safe cell and prevents repeated DFS visits.

# Continue DFS in the upward, downward, left, and right directions to mark every O connected to the boundary.

# Traverse the complete board using an outer loop for rows and an inner loop for columns, ensuring that every cell is processed.

# Convert every remaining O into X, as unmarked O cells are fully surrounded. Restore every # to O, as temporary markers represent boundary-connected safe cells.

from typing import List

class Solution:
    # Marks boundary-connected cells using DFS.
    def markSafe(self, row: int, col: int, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        # Base case: stop for invalid cells and non-'O' cells.
        if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != 'O':
            return

        # Mark the current cell as safe.
        board[row][col] = '#'

        # Move to the upper cell.
        self.markSafe(row - 1, col, board)

        # Move to the lower cell.
        self.markSafe(row + 1, col, board)

        # Move to the left cell.
        self.markSafe(row, col - 1, board)

        # Move to the right cell.
        self.markSafe(row, col + 1, board)

    # Captures surrounded regions using DFS.
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        # Mark safe cells from the left and right borders.
        for row in range(rows):
            self.markSafe(row, 0, board)
            self.markSafe(row, cols - 1, board)

        # Mark safe cells from the top and bottom borders.
        for col in range(cols):
            self.markSafe(0, col, board)
            self.markSafe(rows - 1, col, board)

        # Flip captured cells and restore safe cells.
        for row in range(rows):
            for col in range(cols):
                # Captured cells are still marked as 'O'.
                if board[row][col] == 'O':
                    board[row][col] = 'X'

                # Safe cells were temporarily marked as '#'.
                elif board[row][col] == '#':
                    board[row][col] = 'O'


# Prints the board.
def printBoard(board: List[List[str]]) -> None:
    for row in board:
        print(*row)


# Driver code.
if __name__ == "__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    sol = Solution()

    sol.solve(board)

    printBoard(board)\

# Approach 2
# Breadth First Search uses a queue to identify safe regions without recursive calls. All boundary O cells serve as starting points, creating a multi-source traversal from the four board edges.

# Every reachable O is temporarily marked before queue insertion to prevent duplicate entries. A final nested traversal captures unmarked regions and restores marked safe cells.

# Algorithm
# Store the row count in R and the column count in C, and initialize a queue to manage boundary-connected cells awaiting exploration.

# Traverse all four borders and add every cell containing O to the queue, since each boundary O represents a safe starting point.

# Replace every boundary O with # before queue insertion. Early marking prevents duplicate insertion, especially for corner cells.

# Continue processing while the queue contains cells, ensuring that every safe region connected to any boundary source is explored.

# Remove the front cell and examine neighboring cells in the upward, downward, left, and right directions.

# For every in-bounds neighbor containing O, replace the value with # before adding the coordinates to the queue. Early marking ensures that each cell enters the queue only once.

# Traverse the complete board using an outer loop for rows and an inner loop for columns.

# Convert every remaining O into X, as no boundary path exists. Restore every # to O, as marked cells belong to safe boundary-connected regions.

from typing import List

class Solution:
    # Marks boundary-connected cells using DFS.
    def markSafe(self, row: int, col: int, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        # Base case: stop for invalid cells and non-'O' cells.
        if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != 'O':
            return

        # Mark the current cell as safe.
        board[row][col] = '#'

        # Move to the upper cell.
        self.markSafe(row - 1, col, board)

        # Move to the lower cell.
        self.markSafe(row + 1, col, board)

        # Move to the left cell.
        self.markSafe(row, col - 1, board)

        # Move to the right cell.
        self.markSafe(row, col + 1, board)

    # Captures surrounded regions using DFS.
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        # Mark safe cells from the left and right borders.
        for row in range(rows):
            self.markSafe(row, 0, board)
            self.markSafe(row, cols - 1, board)

        # Mark safe cells from the top and bottom borders.
        for col in range(cols):
            self.markSafe(0, col, board)
            self.markSafe(rows - 1, col, board)

        # Flip captured cells and restore safe cells.
        for row in range(rows):
            for col in range(cols):
                # Captured cells are still marked as 'O'.
                if board[row][col] == 'O':
                    board[row][col] = 'X'

                # Safe cells were temporarily marked as '#'.
                elif board[row][col] == '#':
                    board[row][col] = 'O'


# Prints the board.
def printBoard(board: List[List[str]]) -> None:
    for row in board:
        print(*row)


# Driver code.
if __name__ == "__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    sol = Solution()

    sol.solve(board)

    printBoard(board)

# Approach 3
# Disjoint Set Union represents every board cell using a unique node and introduces one additional virtual boundary node. Every boundary O joins the virtual node, forming a common set for all safe cells.

# Adjacent O cells join the same DSU set. After all unions finish, an O cell outside the virtual boundary set has no path to any border and therefore belongs to a surrounded region.

# Algorithm
# Initialize a DSU structure containing R×C+1 nodes. The first R×C nodes represent board cells, while the final node represents the virtual boundary.

# Map the cell at row r and column c to node identifier r×C+c, allowing board coordinates to be managed through one-dimensional DSU arrays.

# Traverse the board using an outer loop for rows and an inner loop for columns, ensuring that every cell is examined.

# Process only cells containing O, since X cells do not participate in region connectivity.

# Merge every boundary O with the virtual boundary node, allowing all border-connected safe regions to share a common representative.

# Merge each O with adjacent O cells. Checking only the right and downward neighbors avoids processing the same undirected connection twice.

# Find the representative of the virtual boundary node after all unions finish.

# Traverse the board again and compare every O cell’s representative with the virtual boundary representative. Convert the cell to X when the representatives differ, as no connection to a border exists.

from typing import List

class Solution:
    # Finds the parent representative using path compression.
    def findParent(self, node: int, parent: List[int]) -> int:
        # Base case: the node is its own parent.
        if parent[node] == node:
            return node

        # Compress the path for faster future lookup.
        parent[node] = self.findParent(parent[node], parent)

        # Return the ultimate parent.
        return parent[node]

    # Merges two groups using union by size.
    def unite(self, first: int, second: int, parent: List[int], size: List[int]) -> None:
        # Find the parent of the first node.
        parentFirst = self.findParent(first, parent)

        # Find the parent of the second node.
        parentSecond = self.findParent(second, parent)

        # If both nodes are already in one group, stop.
        if parentFirst == parentSecond:
            return

        # Keep the larger group as the main parent.
        if size[parentFirst] < size[parentSecond]:
            parentFirst, parentSecond = parentSecond, parentFirst

        # Attach the smaller group to the larger group.
        parent[parentSecond] = parentFirst

        # Update the size of the merged group.
        size[parentFirst] += size[parentSecond]

    # Captures surrounded regions using DSU.
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        total = rows * cols

        # This extra node represents all boundary-connected 'O' cells.
        boundary = total

        parent = [0] * (total + 1)
        size = [1] * (total + 1)

        deltaRow = [-1, 1, 0, 0]
        deltaCol = [0, 0, -1, 1]

        # Initially, every node is its own parent.
        for node in range(total + 1):
            parent[node] = node

        # Merge all connected 'O' cells.
        for row in range(rows):
            for col in range(cols):
                # Skip blocked cells.
                if board[row][col] != 'O':
                    continue

                current = row * cols + col

                # Connect boundary 'O' cells to the virtual boundary node.
                if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                    self.unite(current, boundary, parent, size)

                # Check all four adjacent directions.
                for direction in range(4):
                    nextRow = row + deltaRow[direction]
                    nextCol = col + deltaCol[direction]

                    # Check if the next cell is inside the board.
                    if 0 <= nextRow < rows and 0 <= nextCol < cols:
                        # Merge only adjacent 'O' cells.
                        if board[nextRow][nextCol] == 'O':
                            self.unite(current, nextRow * cols + nextCol, parent, size)

        # Find the parent of the virtual boundary node.
        boundaryParent = self.findParent(boundary, parent)

        # Flip 'O' cells outside the boundary group.
        for row in range(rows):
            for col in range(cols):
                # Captured 'O' cells are not connected to the boundary.
                if board[row][col] == 'O' and self.findParent(row * cols + col, parent) != boundaryParent:
                    board[row][col] = 'X'


# Prints the board.
def printBoard(board: List[List[str]]) -> None:
    for row in board:
        print(*row)


# Driver code.
if __name__ == "__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    sol = Solution()

    sol.solve(board)

    printBoard(board)