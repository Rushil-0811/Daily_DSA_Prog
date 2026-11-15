# Given an N×M matrix of heights, find a path from the top-left cell to the bottom-right cell with minimum effort.

# Movement is allowed in four directions. Path effort equals the maximum absolute height difference between consecutive cells along the route. Return the minimum possible path effort.

# Example 1
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]

# Output: 2

# Explanation: Route 1->3->5->3->5 has adjacent differences [2,2,2,2], so effort is 2.

# Example 2
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]

# Output: 1

# Explanation: Route 1->2->3->4->5 has maximum adjacent difference 1.

# Brute Force Approach
# An effort limit converts the weighted grid into a reachability problem. Movement between adjacent cells is allowed only when the absolute height difference does not exceed the selected limit.

# Testing limits from 0 upward guarantees that the first feasible value is optimal. Repeated BFS traversals, however, make the approach expensive when the height range is large.

# Algorithm
# Find the minimum and maximum grid heights and define H as their difference, providing a guaranteed upper bound for the required effort.

# Test every effort limit from 0 to H in increasing order, ensuring that the first feasible limit is the minimum possible effort.

# For each limit, initialize a fresh visited matrix and add the source cell to a BFS queue.

# Process the queue and examine all four neighbors of every removed cell.

# Add an unvisited neighbor when the absolute height difference does not exceed the current limit, preserving only allowed movements.

# Return the current limit upon reaching the destination; the range ending at H guarantees a feasible value for a non-empty grid.

from collections import deque
from typing import List


class Solution:
    # Return minimum possible maximum adjacent height difference.
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        minimum_height = min(min(row) for row in heights)
        maximum_height = max(max(row) for row in heights)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Check destination reachability under an effort limit.
        def can_reach(limit: int) -> bool:
            visited = [[False] * cols for _ in range(rows)]
            queue = deque([(0, 0)])
            visited[0][0] = True

            # Explore every cell reachable within the limit.
            while queue:
                row, col = queue.popleft()
                if row == rows - 1 and col == cols - 1:
                    return True

                # Check all four neighboring cells.
                for add_row, add_col in directions:
                    next_row = row + add_row
                    next_col = col + add_col
                    if not (0 <= next_row < rows and 0 <= next_col < cols):
                        continue
                    if visited[next_row][next_col]:
                        continue

                    difference = abs(
                        heights[row][col] - heights[next_row][next_col]
                    )
                    if difference <= limit:
                        visited[next_row][next_col] = True
                        queue.append((next_row, next_col))

            return False

        # Test effort limits from smallest to largest.
        for limit in range(maximum_height - minimum_height + 1):
            if can_reach(limit):
                return limit

        return 0


# Driver code.
def main() -> None:
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    sol = Solution()
    print(sol.minimumEffortPath(heights))


if __name__ == "__main__":
    main()