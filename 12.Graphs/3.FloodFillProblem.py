# Given a 2D image represented by a matrix of integers, a starting cell (sr, sc) in the grid, and a new color, recolor the entire connected region containing the starting cell.

# A cell belongs to the connected region if it has the same original color as the starting cell and can be reached from (sr, sc) by moving up, down, left, or right. Diagonal movement is not allowed.

# Here, sr represents the starting row and sc represents the starting column of the cell in the grid.

# Example 1
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

# Output: [[2,2,2],[2,2,0],[2,0,1]]

# Explanation: The starting cell has color 1. All horizontally or vertically connected cells with color 1 are recolored to 2.

# Example 2
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 2

# Output: [[2,2,2],[2,2,2]]

# Explanation: Every cell belongs to the same connected region, so every cell becomes 2.

# Approach 1
# Depth First Search begins from the given cell and recursively explores adjacent cells in the four directions. A neighboring cell belongs to the connected region only when the cell lies within the matrix boundaries and contains the original color.

# Recoloring a cell before visiting neighboring cells also marks the cell as processed. An early return when oldColor == newColor prevents repeated recursive visits because recoloring would otherwise produce no visible state change.

# Algorithm
# Store the color of the starting cell in oldColor, allowing every connected cell with the original color to be identified.

# Compare oldColor with newColor. Equal values require no modification, so return the original image and avoid unnecessary recursive traversal.

# Start DFS from the given row and column to explore the connected region containing the starting cell.

# End the current DFS call when the row or column lies outside the matrix or when the current cell does not contain oldColor, since such a cell cannot belong to the required region.

# Change the current cell to newColor before exploring adjacent cells. Early recoloring marks the cell as processed and prevents repeated visits.

# Continue DFS in the upward, downward, left, and right directions to recolor every connected cell containing oldColor.

# Return the modified image after the DFS traversal finishes.

from typing import List

class Solution:
    # Recolors all connected cells having the original color.
    def dfs(self, row: int, col: int, image: List[List[int]], oldColor: int, newColor: int) -> None:
        rows = len(image)
        cols = len(image[0])

        # Base case: stop if the cell is outside the image.
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return

        # Base case: stop if the cell does not have the old color.
        if image[row][col] != oldColor:
            return

        # Recolor the current cell.
        image[row][col] = newColor

        # Move to the upper cell.
        self.dfs(row - 1, col, image, oldColor, newColor)

        # Move to the lower cell.
        self.dfs(row + 1, col, image, oldColor, newColor)

        # Move to the left cell.
        self.dfs(row, col - 1, image, oldColor, newColor)

        # Move to the right cell.
        self.dfs(row, col + 1, image, oldColor, newColor)

    # Applies flood fill starting from the given cell.
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldColor = image[sr][sc]

        # If the new color is the same, no change is needed.
        if oldColor == color:
            return image

        # Start DFS from the given cell.
        self.dfs(sr, sc, image, oldColor, color)

        # Return the updated image.
        return image


# Driver code.
if __name__ == "__main__":
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    sr = 1
    sc = 1
    color = 2

    sol = Solution()

    result = sol.floodFill(image, sr, sc, color)

    # Print the updated image.
    for row in result:
        print(*row)

# Approach 2
# Breadth First Search expands the connected region iteratively using a queue. The starting cell enters the queue first, followed by every valid neighboring cell containing the original color.

# Recoloring each eligible cell before queue insertion prevents duplicate entries. An early return when oldColor == newColor avoids repeated processing when recoloring cannot mark cells as visited.

# Algorithm
# Store the color of the starting cell in oldColor, allowing connected cells belonging to the original region to be recognized.

# Compare oldColor with newColor. Equal values require no modification, so return the original image and avoid unnecessary queue processing.

# Recolor the starting cell and add the corresponding coordinates to a queue. Recoloring before insertion marks the cell as processed.

# Continue processing while the queue contains cells, ensuring that the complete connected region is explored.

# Remove the front cell and examine the neighboring cells in the upward, downward, left, and right directions.

# For every in-bounds neighbor containing oldColor, change the color to newColor before adding the coordinates to the queue. Early recoloring prevents duplicate queue entries.

# Return the modified image after the queue becomes empty.    
from typing import List
from collections import deque

class Solution:
    # Applies flood fill starting from the given cell using BFS.
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        oldColor = image[sr][sc]

        # If the new color is the same, no change is needed.
        if oldColor == color:
            return image

        deltaRow = [-1, 1, 0, 0]
        deltaCol = [0, 0, -1, 1]
        q = deque()

        # Recolor the starting cell.
        image[sr][sc] = color

        # Push the starting cell into the queue.
        q.append((sr, sc))

        # Recolor all connected cells having the original color.
        while q:
            row, col = q.popleft()

            # Explore all four adjacent directions.
            for direction in range(4):
                nextRow = row + deltaRow[direction]
                nextCol = col + deltaCol[direction]

                # Check if the next cell is inside the image.
                if 0 <= nextRow < rows and 0 <= nextCol < cols:
                    # Recolor only cells that have the old color.
                    if image[nextRow][nextCol] == oldColor:
                        image[nextRow][nextCol] = color
                        q.append((nextRow, nextCol))

        # Return the updated image.
        return image


# Driver code.
if __name__ == "__main__":
    image = [
        [0, 0, 0],
        [0, 0, 0]
    ]

    sr = 0
    sc = 0
    color = 2

    sol = Solution()

    result = sol.floodFill(image, sr, sc, color)

    # Print the updated image.
    for row in result:
        print(*row)