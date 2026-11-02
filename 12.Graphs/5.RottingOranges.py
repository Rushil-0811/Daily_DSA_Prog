# Given an R×C grid where 0 represents an empty cell, 1 represents a fresh orange, and 2 represents a rotten orange, return the minimum minutes required until no fresh orange remains.

# Every minute, a rotten orange spreads rot to fresh oranges in four directions: up, down, left, and right. Return -1 when at least one fresh orange cannot become rotten.

# Example 1
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]

# Output: 4

# Explanation: Rot spreads level by level and reaches every fresh orange after four minutes.

# Example 2
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]

# Output: -1

# Explanation: The bottom-left fresh orange never touches any rotting chain through four-direction movement.

# Brute Force Approach
# Minute-by-minute simulation repeatedly scans the complete grid. During each minute, every rotten orange marks adjacent fresh oranges with a temporary value, preventing newly affected oranges from spreading before the next minute.

# After a complete scan, temporary oranges become rotten and the minute counter increases. Repeated grid scans accurately simulate simultaneous spreading but produce a high time complexity.

# Algorithm
# Count all fresh oranges and initialize minutes to 0, allowing the simulation to stop after every fresh orange becomes rotten.

# Continue the simulation while fresh oranges remain and initialize newlyRotten to 0 for the current minute.

# Scan the grid using nested loops and mark every fresh neighbor of a rotten orange with a temporary value, preventing same-minute spreading while counting each newly affected orange once.

# Return -1 when newlyRotten remains 0, as the remaining fresh oranges cannot be reached.

# Scan the grid again to convert all temporary cells into rotten oranges and reduce the fresh-orange count accordingly.

# Increment minutes after completing a successful spread round, since one full round represents one elapsed minute.

# Return minutes after no fresh orange remains.

from typing import List

class Solution:
    # Function to find minimum minutes using grid simulation.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        minutes = 0

        # Count all fresh oranges before simulation starts.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Repeat minute-by-minute until no fresh orange remains.
        while fresh > 0:
            changed = False

            # Mark oranges becoming rotten during current minute.
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] != 2:
                        continue

                    # Check four neighboring cells.
                    for add_row, add_col in directions:
                        next_row = row + add_row
                        next_col = col + add_col

                        if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 1:
                            grid[next_row][next_col] = 3
                            fresh -= 1
                            changed = True

            # No new orange rotted, so remaining fresh oranges are unreachable.
            if not changed:
                return -1

            # Commit all oranges marked for next minute.
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 3:
                        grid[row][col] = 2

            minutes += 1

        # Return total elapsed minutes.
        return minutes

# Driver code.
def main() -> None:
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

    sol = Solution()
    print(sol.orangesRotting(grid))

if __name__ == "__main__":
    main()


# Optimal Approach
# Multi-source Breadth First Search begins from all initially rotten oranges simultaneously. Every BFS level contains oranges capable of spreading rot during the same minute.

# Fresh oranges are marked rotten before queue insertion, ensuring that each orange enters the queue only once. Level-by-level processing eliminates repeated full-grid scans.

# Algorithm
# Scan the grid, add every initially rotten orange to a queue, and count all fresh oranges, creating the initial multi-source BFS frontier.

# Return 0 when no fresh orange exists, as no spreading time is required.

# Initialize minutes to 0 and continue BFS while the queue contains cells and fresh oranges remain.

# Store the current queue size and process exactly that many oranges, ensuring that one BFS level represents one minute.

# For every removed orange, inspect the four neighboring cells and convert each fresh neighbor to rotten before queue insertion, preventing duplicate processing.

# Decrease freshCount for every newly rotten orange and increment minutes after the complete BFS level has been processed.

# Return minutes when freshCount becomes 0; otherwise, return -1 because some fresh oranges are unreachable.

from collections import deque
from typing import Deque, List, Tuple

class Solution:
    # Function to find minimum minutes using multi-source BFS.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        minutes = 0
        queue: Deque[Tuple[int, int]] = deque()

        # Collect all rotten oranges as BFS sources.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Process BFS level by level while fresh oranges remain.
        while queue and fresh > 0:
            level_size = len(queue)

            # Process all oranges rotting during current minute.
            for _ in range(level_size):
                row, col = queue.popleft()

                # Spread rot to adjacent fresh oranges.
                for add_row, add_col in directions:
                    next_row = row + add_row
                    next_col = col + add_col

                    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        fresh -= 1
                        queue.append((next_row, next_col))

            minutes += 1

        # Return -1 when unreachable fresh oranges remain.
        if fresh > 0:
            return -1

        # Return minimum elapsed minutes.
        return minutes

# Driver code.
def main() -> None:
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

    sol = Solution()
    print(sol.orangesRotting(grid))

if __name__ == "__main__":
    main()
