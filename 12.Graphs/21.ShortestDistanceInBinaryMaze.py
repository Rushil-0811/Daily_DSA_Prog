# Given an N×M binary maze, a source cell, and a destination cell, find the minimum number of moves needed to reach destination from source.

# A cell containing 1 is walkable, while a cell containing 0 is blocked. Movement is allowed one cell at a time in four directions: up, right, down, and left. Return -1 if no valid route exists.

# Example 1
# Input: grid = [[1,1,1,1],[1,1,0,1],[1,1,1,1],[1,1,0,0],[1,0,0,1]], source = [0,1], destination = [2,2]

# Output: 3

# Explanation: A shortest route is (0,1)->(1,1)->(2,1)->(2,2), containing three moves.

# Example 2
# Input: grid = [[1,0,1],[1,0,1],[1,0,1]], source = [0,0], destination = [2,2]

# Output: -1

# Explanation: The blocked middle column separates source from destination.

# Approach
# Every walkable maze cell represents a graph vertex, while each valid orthogonal movement represents a unit-cost edge. Breadth First Search explores cells in increasing move count, so the first discovery and distance assignment of the destination gives the shortest distance.

# A distance matrix initialized with -1 stores both visitation state and shortest distance. Marking neighbors before queue insertion prevents duplicate processing without modifying the maze.

# Algorithm
# Store the maze dimensions and return -1 when the source or destination is blocked, as no valid path can exist.

# Initialize an N×M distance matrix with -1, where -1 represents an unvisited cell.

# Set the source distance to 0, return 0 when source and destination match, and add the source coordinates to a queue.

# Continue processing while the queue contains cells and remove the front coordinates for level-order exploration.

# Examine the four orthogonal neighbors and ignore out-of-bounds, blocked, or previously visited cells.

# Assign distance[current]+1 to every valid neighbor before queue insertion; return the assigned distance immediately after destination discovery.

# Return -1 when the queue becomes empty without discovering the destination.

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    # Return minimum moves from source to destination in a binary maze.
    def shortestPath(
        self,
        grid: List[List[int]],
        source: List[int],
        destination: List[int]
    ) -> int:
        rows = len(grid)
        cols = len(grid[0])
        source_row, source_col = source
        destination_row, destination_col = destination

        # Reject a blocked source or destination.
        if grid[source_row][source_col] == 0 or \
                grid[destination_row][destination_col] == 0:
            return -1

        # Equal endpoints require zero moves.
        if source == destination:
            return 0

        dist: List[List[int]] = [[-1] * cols for _ in range(rows)]
        queue: Deque[Tuple[int, int]] = deque()

        # Start BFS at distance zero.
        dist[source_row][source_col] = 0
        queue.append((source_row, source_col))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Explore walkable cells in increasing distance order.
        while queue:
            row, col = queue.popleft()

            # Check all four orthogonal neighbors.
            for add_row, add_col in directions:
                next_row = row + add_row
                next_col = col + add_col

                # Skip cells outside maze boundaries.
                if next_row < 0 or next_row >= rows or \
                        next_col < 0 or next_col >= cols:
                    continue

                # Skip blocked or previously visited cells.
                if grid[next_row][next_col] == 0 or \
                        dist[next_row][next_col] != -1:
                    continue

                next_distance = dist[row][col] + 1
                dist[next_row][next_col] = next_distance

                # First destination discovery gives minimum distance.
                if next_row == destination_row and \
                        next_col == destination_col:
                    return next_distance

                queue.append((next_row, next_col))

        # Queue exhaustion means destination is unreachable.
        return -1


# Driver code.
def main() -> None:
    grid = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 1]
    ]
    source = [0, 1]
    destination = [2, 2]
    sol = Solution()
    print(sol.shortestPath(grid, source, destination))


if __name__ == "__main__":
    main()