# Given an N x N matrix isConnected, where isConnected[row][col] = 1 means city row and city col have a direct connection, return the total number of provinces.

# A province is a group of cities connected directly or indirectly. The matrix is symmetric, and isConnected[city][city] = 1 for every city. Counting provinces is equivalent to counting connected components in an undirected graph represented by an adjacency matrix.

# Example 1
# Input: isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# Output: 2

# Explanation: Cities 0 and 1 form one province. City 2 forms another province.

# Example 2
# Input: isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Output: 3

# Explanation: No direct connection exists between different cities, so every city forms a separate province.

# pproach 1
# Depth First Search explores every city reachable from a selected starting city before returning to examine another unvisited city. A complete DFS traversal covers one connected component, representing one province.

# An outer loop examines every city, while a visited array prevents repeated processing. Every DFS call started from an unvisited city indicates the discovery of a new province.

# Algorithm
# Initialize a visited array of size N with all entries marked as unvisited. The array records whether a city has already been included in a discovered province.

# Initialize provinceCount to 0. The variable stores the number of connected components found during traversal.

# Traverse all cities using a loop. Encountering an unvisited city indicates the beginning of a new connected component, so increment provinceCount and start DFS from the city.

# Mark the current city as visited inside DFS, preventing repeated processing through cyclic or bidirectional connections.

# Scan the complete adjacency-matrix row of the current city. An entry equal to 1 represents a direct connection, so start a recursive DFS call for every directly connected unvisited city.

# Return provinceCount after every city has been examined, as each DFS initiation represents exactly one province.

from typing import List

class Solution:
    # Marks all cities that belong to the same province.
    def dfs(self, city: int, isConnected: List[List[int]], visited: List[int]) -> None:
        # Mark the current city as visited.
        visited[city] = 1

        n = len(isConnected)

        # Check every city connected to the current city.
        for nextCity in range(n):
            # If there is a connection and the city is not visited, visit it.
            if isConnected[city][nextCity] == 1 and visited[nextCity] == 0:
                self.dfs(nextCity, isConnected, visited)

    # Counts the total number of provinces using DFS.
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        provinces = 0

        # Try to start DFS from every city.
        for city in range(n):
            # A new unvisited city means a new province starts.
            if visited[city] == 0:
                provinces += 1

                # Visit all cities in this province.
                self.dfs(city, isConnected, visited)

        # Return the total province count.
        return provinces


# Driver code.
if __name__ == "__main__":
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

    sol = Solution()

    print(sol.findCircleNum(isConnected))

# Approach 2
# Breadth First Search uses a queue to explore all cities belonging to one province iteratively. Starting from an unvisited city, BFS processes every directly or indirectly connected city before the outer traversal continues.

# The queue avoids recursive call-stack usage and processes connected cities level by level. Since connectivity is stored in an adjacency matrix, removing a city from the queue requires scanning the complete corresponding row to locate connected neighbors.

# Algorithm
# Initialize a visited array of size N with all entries marked as unvisited. The array prevents cities belonging to an already discovered province from starting another BFS traversal.

# Initialize provinceCount to 0. The variable records the number of connected components discovered.

# Traverse all cities using a loop. An unvisited city represents the starting point of a new province, so increment provinceCount and add the city to a queue.

# Mark the starting city as visited before queue processing. Early marking prevents the same city from being inserted into the queue multiple times.

# Continue processing until the queue becomes empty. For every removed city, scan the corresponding adjacency-matrix row to examine all possible connections.

# Add every directly connected unvisited city to the queue and mark the city as visited. Queue insertion extends the current BFS traversal to all cities belonging to the same province.

# Return provinceCount after all cities have been examined, as each BFS initiation corresponds to one complete province.

from typing import List
from collections import deque

class Solution:
    # Counts the total number of provinces using BFS.
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        provinces = 0

        # Try to start BFS from every city.
        for start in range(n):
            # Skip the city if it already belongs to a province.
            if visited[start] == 1:
                continue

            # A new unvisited city means a new province starts.
            provinces += 1

            q = deque()

            # Mark the starting city as visited.
            visited[start] = 1

            # Push the starting city into the queue.
            q.append(start)

            # Process all cities in the current province.
            while q:
                city = q.popleft()

                # Check every city connected to the current city.
                for nextCity in range(n):
                    # If connected and unvisited, add it to the same province.
                    if isConnected[city][nextCity] == 1 and visited[nextCity] == 0:
                        visited[nextCity] = 1
                        q.append(nextCity)

        # Return the total province count.
        return provinces


# Driver code.
if __name__ == "__main__":
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    sol = Solution()

    print(sol.findCircleNum(isConnected))

# Approach 3
# Disjoint Set Union initially treats every city as an independent province. The parent array stores the representative of each set, while the size array supports efficient merging by attaching the smaller set below the larger set.

# A direct connection between two cities requires merging the corresponding sets. Every successful merge combines two previously separate provinces and reduces the province count by one. Since the adjacency matrix is symmetric, scanning only entries above the main diagonal avoids processing every undirected connection twice.

# Algorithm
# Initialize a DSU structure containing parent and size arrays of size N. Every city initially acts as a separate set representative with a set size of 1.

# Initialize provinceCount to N, as N disconnected cities initially represent N separate provinces.

# Traverse the upper triangle of the adjacency matrix. The outer loop selects a city i, while the inner loop examines cities j satisfying j > i, ensuring that every undirected city pair is checked only once.

# Check whether matrix[i][j] equals 1. A value of 1 signifies a direct connection between cities i and j.

# Find the ultimate representatives of cities i and j using path compression. Different representatives indicate two separate provinces.

# Merge sets having different representatives using union by size. A successful merge combines two provinces, so decrement provinceCount.

# Skip the merge when both cities already have the same representative, as both cities already belong to the same province.

# Return provinceCount after all relevant city pairs have been processed, as the remaining DSU sets represent the final provinces.

from typing import List

class Solution:
    # Finds the ultimate parent of a node.
    def findParent(self, node: int, parent: List[int]) -> int:
        # Base case: the node is its own parent.
        if parent[node] == node:
            return node

        # Compress the path while finding the parent.
        parent[node] = self.findParent(parent[node], parent)

        # Return the ultimate parent.
        return parent[node]

    # Merges two city groups using union by size.
    def unite(self, u: int, v: int, parent: List[int], size: List[int]) -> bool:
        # Find the ultimate parent of both cities.
        pu = self.findParent(u, parent)
        pv = self.findParent(v, parent)

        # If both cities already have the same parent, no merge is needed.
        if pu == pv:
            return False

        # Keep the larger group as the main parent.
        if size[pu] < size[pv]:
            pu, pv = pv, pu

        # Attach the smaller group to the larger group.
        parent[pv] = pu

        # Update the size of the merged group.
        size[pu] += size[pv]

        # Return true because a merge happened.
        return True

    # Counts the total number of provinces using DSU.
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [0] * n
        size = [1] * n
        provinces = n

        # Initially, every city is its own parent.
        for city in range(n):
            parent[city] = city

        # Scan only the upper triangle because the matrix is symmetric.
        for row in range(n):
            for col in range(row + 1, n):
                # If two cities are connected and merged, one province reduces.
                if isConnected[row][col] == 1 and self.unite(row, col, parent, size):
                    provinces -= 1

        # Return the remaining province count.
        return provinces


# Driver code.
if __name__ == "__main__":
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

    sol = Solution()

    print(sol.findCircleNum(isConnected))