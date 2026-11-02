# Given an R × C binary grid where 1 represents land and 0 represents water, return the number of land cells unable to reach the boundary of the grid.

# A land cell can move only to another land cell in four directions: up, down, left, and right. A land cell is an enclave when no path from the cell reaches any boundary cell.

# Example 1
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

# Output: 3

# Explanation: The boundary land cell at (1, 0) can escape. The three middle land cells cannot reach any boundary.

# Example 2
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]

# Output: 0

# Explanation: All land cells connect to boundary land, so no enclave land cell remains.

# Approach 1
# Depth First Search removes every land cell connected to the grid boundary. Boundary-connected land can reach the boundary and therefore cannot form an enclave.

# After all boundary-connected regions are removed, every remaining land cell is enclosed by water. A final grid traversal counts such enclosed cells.

# Algorithm
# Traverse the first and last columns across all rows, followed by the first and last rows across all columns. Such traversal identifies every boundary cell without scanning the entire grid for starting points.

# Start DFS whenever a boundary cell contains land, since the complete connected region containing such a cell cannot contribute to the enclave count.

# End the current DFS call when the row or column falls outside the grid or when the current cell contains water, as further traversal along such a path cannot reach unprocessed land.

# Change the current land cell to water before exploring adjacent cells. Early modification marks the cell as processed and prevents repeated recursive visits.

# Continue DFS in the upward, downward, left, and right directions to remove every land cell connected to the boundary.

# Traverse the complete grid after all DFS calls finish and count cells still containing land, as only enclosed land remains.

# Return the final count of enclosed land cells.

from typing import List

class Solution:
    # Removes all land cells connected to the current boundary land cell.
    def dfs(self, row: int, col: int, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        # Base case: stop if the cell is outside the grid or is water.
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
            return

        # Mark the current land cell as visited by changing it to water.
        grid[row][col] = 0

        # Move to the upper cell.
        self.dfs(row - 1, col, grid)

        # Move to the lower cell.
        self.dfs(row + 1, col, grid)

        # Move to the left cell.
        self.dfs(row, col - 1, grid)

        # Move to the right cell.
        self.dfs(row, col + 1, grid)

    # Counts land cells that cannot reach the boundary.
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Remove boundary-connected land from the left and right edges.
        for row in range(rows):
            self.dfs(row, 0, grid)
            self.dfs(row, cols - 1, grid)

        # Remove boundary-connected land from the top and bottom edges.
        for col in range(cols):
            self.dfs(0, col, grid)
            self.dfs(rows - 1, col, grid)

        enclaves = 0

        # Count the remaining land cells.
        for row in range(rows):
            for col in range(cols):
                enclaves += grid[row][col]

        # Return the number of enclave cells.
        return enclaves


# Driver code.
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    sol = Solution()

    print(sol.numEnclaves(grid))

# Approach 2
# Multi-source Breadth First Search begins from all boundary land cells simultaneously. Every land cell reachable from a boundary source is removed because boundary reachability prevents enclave membership.

# Recoloring boundary land before queue insertion marks each cell as processed. After queue processing finishes, a final traversal counts the land cells that remain enclosed.

# Algorithm
# Initialize an empty queue to store boundary-connected land cells awaiting exploration.

# Traverse all boundary cells and add every land cell to the queue, since every boundary land cell acts as a starting source for BFS.

# Change each boundary land cell to water before queue insertion. Early modification prevents duplicate queue entries, especially at corner cells.

# Continue processing while the queue contains cells, ensuring that every land cell connected to any boundary source is explored.

# Remove the front cell and examine neighboring cells in the upward, downward, left, and right directions.

# For every in-bounds neighbor containing land, change the value to water before adding the coordinates to the queue. Early modification prevents repeated processing through another neighboring cell.

# Traverse the complete grid after BFS finishes and count cells still containing land, as every remaining land cell is enclosed.

# Return the final count of enclosed land cells.

from typing import List
from collections import deque

class Solution:
    # Counts land cells that cannot reach the boundary.
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        deltaRow = [-1, 1, 0, 0]
        deltaCol = [0, 0, -1, 1]

        # Add land cells from the left and right boundaries.
        for row in range(rows):
            for col in [0, cols - 1]:
                # If boundary cell is land, mark and push it.
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    q.append((row, col))

        # Add land cells from the top and bottom boundaries.
        for col in range(cols):
            for row in [0, rows - 1]:
                # If boundary cell is land, mark and push it.
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    q.append((row, col))

        # Remove all land connected to boundary land cells.
        while q:
            row, col = q.popleft()

            # Explore all four adjacent directions.
            for direction in range(4):
                nextRow = row + deltaRow[direction]
                nextCol = col + deltaCol[direction]

                # Check if the next cell is inside the grid.
                if 0 <= nextRow < rows and 0 <= nextCol < cols:
                    # If connected cell is land, mark and push it.
                    if grid[nextRow][nextCol] == 1:
                        grid[nextRow][nextCol] = 0
                        q.append((nextRow, nextCol))

        enclaves = 0

        # Count the remaining land cells.
        for row in range(rows):
            for col in range(cols):
                enclaves += grid[row][col]

        # Return the number of enclave cells.
        return enclaves


# Driver code.
if __name__ == "__main__":
    grid = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]

    sol = Solution()

    print(sol.numEnclaves(grid))

# Approach 3
# Disjoint Set Union represents every grid cell with a unique node and introduces one additional virtual boundary node. Merging boundary land cells with the virtual node places all boundary-connected land cells in the same set as the virtual boundary node.

# Adjacent land cells are merged into common sets. After all unions finish, any land cell outside the set containing the virtual boundary node belongs to an enclave. Union by size may select another node as the set root, so connectivity must be checked using DSU representatives rather than assuming that the virtual node remains the root.

# Algorithm
# Initialize a DSU structure with R×C+1 nodes, where the first R×C nodes represent grid cells and the final node represents the virtual boundary.

# Map the cell at row r and column c to node identifier r×C+c, allowing two-dimensional coordinates to work with one-dimensional DSU arrays.

# Traverse every grid cell and process only land cells, since water cells do not participate in land connectivity.

# Merge every boundary land cell with the virtual boundary node, placing all boundary-connected land components in the same DSU set as the virtual node.

# Merge each land cell with the right and downward land neighbors, avoiding duplicate processing of undirected connections.

# After all unions finish, compare find(cellNode) with find(virtualBoundary) for every land cell, ensuring that connectivity is checked through the current set representatives.

# Increment the enclave count when both representatives differ, then return the final count.

from typing import List

class Solution:
    # Finds the representative parent using path compression.
    def findParent(self, node: int, parent: List[int]) -> int:
        # Base case: the node is its own parent.
        if parent[node] == node:
            return node

        # Compress the path while finding the parent.
        parent[node] = self.findParent(parent[node], parent)

        # Return the ultimate parent.
        return parent[node]

    # Merges two sets using union by size.
    def unite(self, first: int, second: int, parent: List[int], size: List[int]) -> None:
        # Find the parent of the first node.
        pFirst = self.findParent(first, parent)

        # Find the parent of the second node.
        pSecond = self.findParent(second, parent)

        # If both nodes are already in the same set, stop.
        if pFirst == pSecond:
            return

        # Keep the larger set as the main parent.
        if size[pFirst] < size[pSecond]:
            pFirst, pSecond = pSecond, pFirst

        # Attach the smaller set to the larger set.
        parent[pSecond] = pFirst

        # Update the size of the merged set.
        size[pFirst] += size[pSecond]

    # Counts land cells that are not connected to the boundary.
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        total = rows * cols

        # This extra node represents all boundary-connected land.
        boundary = total

        parent = [0] * (total + 1)
        size = [1] * (total + 1)

        # Initially, every node is its own parent.
        for node in range(total + 1):
            parent[node] = node

        deltaRow = [-1, 1, 0, 0]
        deltaCol = [0, 0, -1, 1]

        # Connect land cells using DSU.
        for row in range(rows):
            for col in range(cols):
                # Skip water cells.
                if grid[row][col] == 0:
                    continue

                current = row * cols + col

                # Connect boundary land cells to the virtual boundary node.
                if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                    self.unite(current, boundary, parent, size)

                # Check all four adjacent directions.
                for direction in range(4):
                    nextRow = row + deltaRow[direction]
                    nextCol = col + deltaCol[direction]

                    # Check if the next cell is inside the grid.
                    if 0 <= nextRow < rows and 0 <= nextCol < cols:
                        # Connect the current land cell to adjacent land.
                        if grid[nextRow][nextCol] == 1:
                            self.unite(current, nextRow * cols + nextCol, parent, size)

        enclaves = 0

        # Find the parent of the virtual boundary node.
        boundaryParent = self.findParent(boundary, parent)

        # Count land cells that are not connected to the boundary.
        for row in range(rows):
            for col in range(cols):
                # Count only land cells outside the boundary component.
                if grid[row][col] == 1 and self.findParent(row * cols + col, parent) != boundaryParent:
                    enclaves += 1

        # Return the number of enclave cells.
        return enclaves


# Driver code.
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    sol = Solution()

    print(sol.numEnclaves(grid))