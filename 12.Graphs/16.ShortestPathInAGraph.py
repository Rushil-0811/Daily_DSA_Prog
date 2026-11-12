# Given an undirected graph with V vertices numbered from 0 to V - 1, E edges, and a source vertex src, return the shortest distance from source to every vertex.

# Every edge has unit weight. If a vertex cannot be reached from source, store -1 for the unreachable vertex.

# Example 1
# Input: V = 9, E = 10, edges = [[0,1],[0,3],[1,2],[3,4],[4,5],[2,6],[5,6],[6,7],[6,8],[7,8]], src = 0

# Output: [0,1,2,1,2,3,3,4,4]

# Explanation: BFS from vertex 0 reaches vertices by levels. Distances become 0 for source, 1 for vertices 1 and 3, 2 for vertices 2 and 4, and so on.

# Example 2
# Input: V = 4, E = 2, edges = [[0,3],[1,3]], src = 3

# Output: [1,1,-1,0]

# Explanation: Vertices 0 and 1 are one edge away from source 3. Vertex 2 is unreachable, so distance remains -1.

# Approach
# In a unit-weight graph, every edge contributes exactly one step to the path length. Breadth First Search explores vertices level by level, processing all vertices at distance d before any vertex at distance d+1.

# The first visit to a vertex therefore provides the minimum number of edges from the source. A distance array initialized with -1 stores shortest distances while also identifying unvisited and unreachable vertices.

# Algorithm
# Initialize an adjacency list for V vertices, providing efficient access to every neighboring vertex.

# Traverse all edges and add both directions to the adjacency list, since each undirected edge permits movement between both endpoints.

# Create a distance array filled with -1, where -1 indicates that no path from the source has been discovered.

# Set the source distance to 0 and add the source to a queue, establishing the first BFS level.

# Continue processing while the queue contains vertices, ensuring level-by-level exploration of all reachable vertices.

# For every neighbor having distance -1, set the distance to distance[current]+1 and add the neighbor to the queue, recording the shortest path during the first visit.

# Return the distance array after BFS finishes, leaving every unreachable vertex marked as -1.

from collections import deque
from typing import List


class Solution:
    # Return shortest distance from source to every vertex.
    def shortestPath(self, edges: List[List[int]], V: int, E: int, src: int) -> List[int]:
        adj: List[List[int]] = [[] for _ in range(V)]

        # Build undirected adjacency list.
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist: List[int] = [-1] * V
        q = deque()

        # Source distance is always zero.
        dist[src] = 0
        q.append(src)

        # BFS visits vertices level by level.
        while q:
            node = q.popleft()

            # Visit every adjacent vertex.
            for neighbor in adj[node]:
                # First visit gives shortest unit-weight distance.
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)

        return dist


# Driver code.
def main() -> None:
    V = 9
    E = 10
    edges = [
        [0, 1], [0, 3], [1, 2], [3, 4], [4, 5],
        [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]
    ]
    src = 0
    sol = Solution()
    print(sol.shortestPath(edges, V, E, src))


if __name__ == "__main__":
    main()