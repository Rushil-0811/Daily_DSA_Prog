# Given a weighted directed acyclic graph with V vertices numbered from 0 to V - 1 and E directed weighted edges, find the shortest distance from source vertex 0 to every vertex.

# Each edge is represented as [u, v, wt], meaning a directed edge from u to v with weight wt. Return -1 for every vertex unreachable from source.

# Example 1
# Input: V = 4, E = 2, edges = [[0,1,2],[0,2,1]]

# Output: [0,2,1,-1]

# Explanation: Vertices 1 and 2 are directly reachable from source. Vertex 3 is unreachable, so distance is -1.

# Example 2
# Input: V = 6, E = 7, edges = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]

# Output: [0,2,3,6,1,5]

# Explanation: Shortest routes are 0->1, 0->4->2, 0->4->5->3, 0->4, and 0->4->5.

# DFS Approach
# A directed acyclic graph has a topological ordering where every edge moves from an earlier vertex to a later vertex. Processing vertices in such order ensures that all possible incoming paths have contributed before outgoing edges are relaxed.

# DFS creates the topological order by adding each vertex after all outgoing paths finish. Distances then propagate from source 0, with every directed edge relaxed exactly once.

# Algorithm
# Build a weighted adjacency list from the edge list, storing every destination vertex with the corresponding edge weight.

# Run DFS from every unvisited vertex and push each vertex onto a stack after processing all outgoing neighbors, producing topological order in reverse finishing time.

# Initialize every distance as infinity and set distance[0] to 0, establishing vertex 0 as the source.

# Remove vertices from the topological stack one by one, ensuring that every predecessor is processed before the corresponding dependent vertex.

# Skip relaxation when the current distance remains infinity, as no path from the source reaches the current vertex.

# For every outgoing edge (current, neighbor, weight), update distance[neighbor] with the smaller of the existing value and distance[current]+weight.

# Replace all remaining infinity values with -1 and return the distance array, marking every unreachable vertex explicitly.

from typing import List, Tuple


class Solution:
    # Return shortest distances from source 0 in a weighted DAG.
    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        adj: List[List[Tuple[int, int]]] = [[] for _ in range(V)]

        # Build directed weighted adjacency list.
        for from_node, to_node, weight in edges:
            adj[from_node].append((to_node, weight))

        visited: List[int] = [0] * V
        topo: List[int] = []

        # Store nodes after exploring outgoing edges.
        def dfs(node: int) -> None:
            # Mark current node visited.
            visited[node] = 1

            # Visit every outgoing neighbor.
            for next_node, _ in adj[node]:
                if not visited[next_node]:
                    dfs(next_node)

            # Append after descendants to create topological order.
            topo.append(node)

        # Run DFS from every component to cover all vertices.
        for node in range(V):
            if not visited[node]:
                dfs(node)

        INF = 10**9
        dist: List[int] = [INF] * V

        # Source vertex is fixed as 0.
        dist[0] = 0

        # Relax edges following topological order.
        while topo:
            node = topo.pop()

            # Skip vertices unreachable from source.
            if dist[node] == INF:
                continue

            # Improve distances of outgoing neighbors.
            for next_node, weight in adj[node]:
                if dist[node] + weight < dist[next_node]:
                    dist[next_node] = dist[node] + weight

        # Convert unreachable vertices from INF to -1.
        for node in range(V):
            if dist[node] == INF:
                dist[node] = -1

        return dist


# Driver code.
def main() -> None:
    V = 6
    E = 7
    edges = [
        [0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2],
        [1, 2, 3], [2, 3, 6], [5, 3, 1]
    ]
    sol = Solution()
    print(sol.shortestPath(V, E, edges))


if __name__ == "__main__":
    main()