# Given an N×N binary grid, return the size of the largest island possible after changing at most one 0 cell into 1.

# An island is a group of 1 cells connected horizontally or vertically. Diagonal cells are not connected. If the grid already contains only land, return N×N.

# Example 1
# Input: grid = [[1,0],[0,1]]

# Output: 3

# Explanation: Flipping either zero connects two diagonal land cells through the flipped cell, forming an island of size 3.

# Example 2
# Input: grid = [[1,1],[1,0]]

# Output: 4

# Explanation: Flipping the only zero makes the entire grid one island.

# Brute Force Approach
# Every water cell is temporarily converted into land, followed by a complete island-area calculation using DFS. The largest area obtained across all possible flips becomes the final answer.

# A fresh visited matrix keeps every trial independent, while restoring the flipped cell preserves the original grid for the next candidate. Repeated full-grid exploration makes the approach computationally expensive.

# Algorithm
# Compute the largest existing island using DFS and store the area as the initial answer, covering cases where no beneficial flip exists.

# Traverse the grid using an outer loop for rows and an inner loop for columns, ensuring that every water cell is considered as a candidate.

# Temporarily change the current water cell to land, simulating the allowed single conversion.

# Create a fresh visited matrix and scan the modified grid, using DFS to calculate the area of every island formed during the current trial.

# Update the maximum answer with the largest island area obtained from the temporary conversion.

# Restore the candidate cell to water, ensuring that the next trial begins with the original grid.

# Return N×N when no water cell exists; otherwise, return the maximum area found across all trials.

from typing import List

class Solution:
    # Function to find largest island by trying every zero flip.
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Function to count one island after a candidate flip.
        def dfs(row: int, col: int, visited: List[List[bool]]) -> int:
            # Stop for invalid cells, water cells, and already counted cells.
            if row < 0 or col < 0 or row >= n or col >= n or grid[row][col] == 0 or visited[row][col]:
                return 0

            # Mark current land cell as counted.
            visited[row][col] = True

            # Count current cell and four neighboring directions.
            area = 1
            area += dfs(row - 1, col, visited)
            area += dfs(row + 1, col, visited)
            area += dfs(row, col - 1, visited)
            area += dfs(row, col + 1, visited)

            # Return island area for current DFS.
            return area

        # Function to compute largest island for the current grid.
        def largestCurrentIsland() -> int:
            best = 0
            visited = [[False for col in range(n)] for row in range(n)]

            # Traverse every cell and count unvisited islands.
            for row in range(n):
                for col in range(n):
                    if grid[row][col] == 1 and not visited[row][col]:
                        best = max(best, dfs(row, col, visited))

            # Return largest island found.
            return best

        answer = largestCurrentIsland()
        hasZero = False

        # Try every zero as a flip candidate.
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    hasZero = True
                    grid[row][col] = 1
                    answer = max(answer, largestCurrentIsland())
                    grid[row][col] = 0

        # Return full grid size for all-land grid.
        if not hasZero:
            return n * n

        # Return best area after at most one flip.
        return answer

# Driver code.
def main() -> None:
    grid = [[1, 0], [0, 1]]

    sol = Solution()
    print(sol.largestIsland(grid))

if __name__ == "__main__":
    main()
