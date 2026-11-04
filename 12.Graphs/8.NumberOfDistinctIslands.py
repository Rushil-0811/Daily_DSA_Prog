# Given an R×C binary grid where 1 represents land and 0 represents water, return the number of distinct island shapes.

# An island is formed by horizontal and vertical connections between land cells. Two islands are equal only when one island can be shifted up, down, left, or right to match the other island exactly. Rotation and reflection do not create equality.

# Example 1
# Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

# Output: 1

# Explanation: Both islands form the same 2×2 square shape after shifting to a common origin.

# Example 2
# Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]

# Output: 3

# Explanation: The grid contains multiple islands, and only repeated translated shapes collapse into one distinct shape.

# Approach 1
# Depth First Search explores an entire island from the first unvisited land cell encountered during row-major traversal. The starting cell acts as the base position, and every island cell is recorded using an offset from the base.

# Relative coordinates remove positional differences between translated islands. A fixed traversal order creates consistent signatures for identical shapes, while a hash set retains only unique signatures.

# Algorithm
# Initialize an empty hash set to store unique island signatures.

# Traverse the grid using an outer loop for rows and an inner loop for columns, ensuring every cell is examined.

# Upon finding a land cell, store the current position as the base and start DFS to explore the complete island.

# During DFS, mark each visited land cell as water to prevent repeated processing.

# Record each visited cell as (row-baseRow, col-baseCol), removing positional differences while preserving the island shape.

# Explore neighboring land cells in a fixed directional order and convert all collected coordinates into an unambiguous signature.

# Insert the signature into the hash set and return the set size after the complete grid traversal.

from typing import List

class Solution:
    # Function to count distinct islands using DFS.
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        uniqueShapes = set()

        # Function to collect one island signature using DFS.
        def dfs(row: int, col: int, baseRow: int, baseCol: int, shape: List[str]) -> None:
            # Stop for invalid cells and water cells.
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return

            # Mark current land cell as visited.
            grid[row][col] = 0

            # Store relative position from island start.
            shape.append(f"{row - baseRow}:{col - baseCol}")

            # Visit all four neighboring cells.
            dfs(row - 1, col, baseRow, baseCol, shape)
            dfs(row + 1, col, baseRow, baseCol, shape)
            dfs(row, col - 1, baseRow, baseCol, shape)
            dfs(row, col + 1, baseRow, baseCol, shape)

        # Scan every cell using nested loops.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    shape = []
                    dfs(row, col, row, col, shape)

                    # Store only unique signatures.
                    uniqueShapes.add("|".join(shape))

        # Return count of unique shapes.
        return len(uniqueShapes)

# Driver code.
def main() -> None:
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
    ]

    sol = Solution()
    print(sol.countDistinctIslands(grid))

if __name__ == "__main__":
    main()

# Approach 2
# Breadth First Search explores an entire island iteratively using a queue. The first land cell encountered during row-major traversal becomes the base position for normalizing all coordinates in the island.

# Every dequeued cell contributes a relative coordinate to the island signature. A fixed neighbor order produces consistent signatures, while queue-based traversal avoids recursive call-stack usage.

# Algorithm
# Initialize an empty hash set for unique island signatures and define the four movement directions in a fixed order.

# Traverse the grid using nested row and column loops to locate every unvisited land cell.

# Upon finding a land cell, store the position as the base, mark the cell as water, and add the coordinates to a queue.

# Process the queue and record each removed cell as (row-baseRow, col-baseCol), preserving shape while removing absolute position.

# Examine all four neighbors and add every valid land neighbor after marking the cell as water, preventing duplicate queue entries.

# Convert the collected relative coordinates into an unambiguous signature and insert the signature into the hash set.

# Return the hash-set size after all cells have been processed, as every stored signature represents one distinct island shape.

from collections import deque
from typing import List

class Solution:
    # Function to count distinct islands using BFS.
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        uniqueShapes = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Scan every cell using nested loops.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue

                shape = []
                q = deque([(row, col)])
                grid[row][col] = 0

                # Process one complete island.
                while q:
                    currentRow, currentCol = q.popleft()

                    # Store relative position from island start.
                    shape.append(f"{currentRow - row}:{currentCol - col}")

                    # Visit all four neighboring cells.
                    for addRow, addCol in directions:
                        nextRow = currentRow + addRow
                        nextCol = currentCol + addCol

                        if 0 <= nextRow < rows and 0 <= nextCol < cols and grid[nextRow][nextCol] == 1:
                            grid[nextRow][nextCol] = 0
                            q.append((nextRow, nextCol))

                # Store only unique signatures.
                uniqueShapes.add("|".join(shape))

        # Return count of unique shapes.
        return len(uniqueShapes)

# Driver code.
def main() -> None:
    grid = [
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
    ]

    sol = Solution()
    print(sol.countDistinctIslands(grid))

if __name__ == "__main__":
    main()
