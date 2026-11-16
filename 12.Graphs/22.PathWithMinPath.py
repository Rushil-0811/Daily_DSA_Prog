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

# Better Approach
# Threshold feasibility is monotonic: once a destination becomes reachable under an effort limit, every larger limit also remains feasible. Binary search uses such monotonicity to avoid testing every value.

# Each middle value runs a BFS reachability check. A feasible threshold reduces the upper bound, while an infeasible threshold increases the lower bound.

# Algorithm
# Find the minimum and maximum grid heights and define the search range from 0 to their difference H.

# Continue binary search while the lower bound is smaller than the upper bound and calculate the middle effort limit.

# Run BFS with a fresh visited matrix, allowing movement only when the adjacent height difference does not exceed the middle value.

# Set the upper bound to the middle value when BFS reaches the destination, preserving the possibility of a smaller feasible effort.

# Set the lower bound to middle+1 when BFS fails, eliminating all infeasible limits up to the middle value.

# Return the converged lower bound, representing the smallest effort that permits destination reachability.

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

        low = 0
        high = maximum_height - minimum_height

        # Binary search the smallest feasible effort limit.
        while low < high:
            middle = (low + high) // 2
            if can_reach(middle):
                high = middle
            else:
                low = middle + 1

        return low


# Driver code.
def main() -> None:
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    sol = Solution()
    print(sol.minimumEffortPath(heights))


if __name__ == "__main__":
    main()

# Optimal Approach
# Every cell represents a graph vertex, while the absolute height difference between adjacent cells represents an edge weight. Path effort equals the largest edge weight on the path rather than the sum of all weights.

# Dijkstra’s Algorithm adapts through minimax relaxation. A min-heap processes the route having the smallest known bottleneck, making the destination effort final when the destination is removed with a current heap value.

# Algorithm
# Initialize every cell effort as infinity, set the source effort to 0, and insert the source state into a min-heap.

# Continue processing while the heap contains states and remove the cell having the smallest known route effort.

# Skip the removed state when the heap effort differs from the stored effort, as the state represents an outdated route.

# Return the current effort when the destination is removed, since the smallest available bottleneck cannot be improved later.

# Examine all four valid neighbors and calculate the edge effort as the absolute height difference between both cells.

# Calculate the candidate effort as the maximum of the current route effort and edge effort; upon improvement, update the neighbor and insert a fresh heap state.

# Return 0 only as a defensive fallback after heap exhaustion. The fallback is never reached for a valid non-empty rectangular grid, because every cell is reachable through orthogonal moves.

import heapq
from typing import List, Tuple


class Solution:
    # Return minimum possible maximum adjacent height difference.
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        effort = [[float("inf")] * cols for _ in range(rows)]
        min_heap: List[Tuple[int, int, int]] = [(0, 0, 0)]
        effort[0][0] = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Process cells by smallest known route effort.
        while min_heap:
            current_effort, row, col = heapq.heappop(min_heap)

            # Skip an outdated heap state.
            if current_effort != effort[row][col]:
                continue

            # Destination effort is final after extraction.
            if row == rows - 1 and col == cols - 1:
                return current_effort

            # Relax all four neighboring cells.
            for add_row, add_col in directions:
                next_row = row + add_row
                next_col = col + add_col
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue

                edge_effort = abs(
                    heights[row][col] - heights[next_row][next_col]
                )
                candidate = max(current_effort, edge_effort)
                if candidate < effort[next_row][next_col]:
                    effort[next_row][next_col] = candidate
                    heapq.heappush(
                        min_heap, (candidate, next_row, next_col)
                    )

        return 0


# Driver code.
def main() -> None:
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    sol = Solution()
    print(sol.minimumEffortPath(heights))


if __name__ == "__main__":
    main()