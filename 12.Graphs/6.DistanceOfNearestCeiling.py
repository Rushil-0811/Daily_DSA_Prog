# Given an N×M binary grid, return a matrix where each cell stores the distance to the nearest cell having value 1.

# Movement is allowed only in four directions: up, down, left, and right. Cells containing 1 have distance 0 from the nearest one-cell.

# Example 1
# Input: grid = [[0,0,0],[0,1,0],[0,0,0]]

# Output: [[2,1,2],[1,0,1],[2,1,2]]

# Explanation: The center cell is the only one-cell, so distances expand outward by one step per layer.

# Example 2
# Input: grid = [[1,0,1],[1,1,0],[1,0,0]]

# Output: [[0,1,0],[0,0,1],[0,1,2]]

# Explanation: Every zero-cell stores the shortest four-direction distance to any one-cell.

# Brute Force Approach
# The direct method stores the coordinates of every cell containing 1. For each grid cell, Manhattan distance is calculated against every stored 1-cell.

# The smallest calculated distance becomes the answer for the current cell. Checking every possible source guarantees correctness but causes repeated comparisons.

# Algorithm
# Initialize a list to store the coordinates of all cells containing 1.

# Traverse the grid using an outer loop for rows and an inner loop for columns, ensuring that every cell is examined.

# Add every 1-cell coordinate to the list, creating the complete collection of possible nearest sources.

# Initialize an N×M distance matrix with large values to store minimum distances.

# For every grid cell, calculate |row-sourceRow|+|col-sourceCol| for each stored source coordinate.

# Store the smallest calculated Manhattan distance in the corresponding matrix position.

# Return the completed distance matrix after all cells have been processed.

from typing import List, Tuple

class Solution:
    # Function to compute nearest-one distances using brute force.
    def nearest(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        ones: List[Tuple[int, int]] = []

        # Store coordinates of every source cell.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    ones.append((row, col))

        dist = [[0 for col in range(cols)] for row in range(rows)]

        # Compute nearest source distance for every grid cell.
        for row in range(rows):
            for col in range(cols):
                best = rows + cols

                # Compare current cell with every source cell.
                for source_row, source_col in ones:
                    value = abs(row - source_row) + abs(col - source_col)
                    best = min(best, value)

                # Store the minimum Manhattan distance.
                dist[row][col] = best

        # Return completed distance matrix.
        return dist

# Driver code.
def main() -> None:
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    sol = Solution()
    ans = sol.nearest(grid)

    # Print resulting distance matrix.
    for row in ans:
        print(row)

if __name__ == "__main__":
    main()


# Optimal Approach
# Multi-source Breadth First Search treats every 1-cell as a source having distance 0. Adding all sources initially allows distances to spread simultaneously across the grid.

# BFS processes cells in increasing distance order, so the first visit to a cell provides the shortest distance to any 1-cell. Marking cells before queue insertion prevents duplicate processing.

# Algorithm
# Initialize an N×M distance matrix with -1 and an empty queue, where -1 represents an unvisited cell.

# Traverse the grid using nested row and column loops to locate every 1-cell.

# Assign distance 0 to every 1-cell and add the coordinates to the queue, creating the initial multi-source BFS level.

# Continue processing while the queue contains cells and remove the front coordinates.

# Examine the four orthogonal neighbors and ignore positions outside the grid or cells having an assigned distance.

# Assign distance[current]+1 to every valid unvisited neighbor before queue insertion, ensuring shortest-distance assignment and preventing duplicates.

# Return the completed distance matrix after the queue becomes empty.

from collections import deque
from typing import Deque, List, Tuple

class Solution:
    # Function to compute nearest-one distances using multi-source BFS.
    def nearest(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        queue: Deque[Tuple[int, int]] = deque()
        dist = [[-1 for col in range(cols)] for row in range(rows)]

        # Add every one-cell as a BFS source.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dist[row][col] = 0
                    queue.append((row, col))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Expand BFS layers from all sources.
        while queue:
            row, col = queue.popleft()

            # Visit four neighboring cells.
            for add_row, add_col in directions:
                next_row = row + add_row
                next_col = col + add_col

                if 0 <= next_row < rows and 0 <= next_col < cols and dist[next_row][next_col] == -1:
                    dist[next_row][next_col] = dist[row][col] + 1
                    queue.append((next_row, next_col))

        # Return completed distance matrix.
        return dist

# Driver code.
def main() -> None:
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    sol = Solution()
    ans = sol.nearest(grid)

    # Print resulting distance matrix.
    for row in ans:
        print(row)

if __name__ == "__main__":
    main()
