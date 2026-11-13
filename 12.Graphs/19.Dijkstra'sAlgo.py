# Given an undirected weighted graph with V vertices numbered from 0 to V - 1, an edge list, and a source vertex, find the shortest distance from source to every vertex.

# Every edge appears as [u, v, weight] and every weight is non-negative. Return -1 for each vertex unreachable from source.

# Example 1
# Input: V = 5, edges = [[0,1,4],[0,2,1],[2,1,2],[1,3,1],[2,3,5],[3,4,3]], source = 0

# Output: [0,3,1,4,7]

# Explanation: Minimum routes from source are 0, 0->2->1, 0->2, 0->2->1->3, and 0->2->1->3->4.

# Example 2
# Input: V = 4, edges = [[0,1,2],[1,2,3]], source = 0

# Output: [0,2,5,-1]

# Explanation: Vertex 2 has minimum distance 5 through vertex 1. Vertex 3 is disconnected from source.

# Brute Force Approach
# Dijkstra’s Algorithm expands the shortest-path region from the source. With non-negative edge weights, the unsettled vertex having the smallest known distance cannot later receive a shorter path through another unsettled vertex.

# A distance array stores the best discovered costs, while a settled array records finalized vertices. Linear minimum selection preserves the greedy logic but scans all vertices repeatedly.

# Algorithm
# Build an undirected weighted adjacency list, storing every edge in both directions with the corresponding weight.

# Initialize all distances as infinity, all settled states as false, and the source distance as 0.

# Repeat up to V times and scan all vertices to select the unsettled vertex having the smallest current distance.

# End processing when no selectable vertex exists or the smallest distance is infinity, since all remaining vertices are unreachable.

# Mark the selected vertex as settled because non-negative weights guarantee finality of the smallest available distance.

# Examine every adjacent edge and update the neighbor distance when distance[current]+weight produces a smaller value.

# Replace remaining infinity values with -1 and return the distance array, explicitly identifying unreachable vertices.

from typing import List

class Solution:
    # Return shortest distances with linear minimum selection.
    def dijkstra(self, V: int, edges: List[List[int]], source: int) -> List[int]:
        adj = [[] for _ in range(V)]

        # Build an undirected weighted adjacency list.
        for edge in edges:
            u = edge[0]
            v = edge[1]
            weight = edge[2]

            adj[u].append((v, weight))
            adj[v].append((u, weight))

        INF = float("inf")
        dist = [INF] * V
        settled = [0] * V

        # Set the source distance to zero.
        dist[source] = 0

        # Settle at most one vertex during each pass.
        for _ in range(V):
            node = -1

            # Find the unsettled vertex with minimum distance.
            for vertex in range(V):
                if not settled[vertex] and (node == -1 or dist[vertex] < dist[node]):
                    node = vertex

            # Stop after all reachable vertices are settled.
            if node == -1 or dist[node] == INF:
                break

            # Finalize the selected shortest distance.
            settled[node] = 1

            # Relax every edge leaving the selected vertex.
            for neighbor, weight in adj[node]:
                candidate = dist[node] + weight

                # Update only unsettled neighbors with shorter distance.
                if not settled[neighbor] and candidate < dist[neighbor]:
                    dist[neighbor] = candidate

        answer = [-1] * V

        # Convert finite distances to the required answer format.
        for vertex in range(V):
            if dist[vertex] != INF:
                answer[vertex] = dist[vertex]

        # Return all shortest distances.
        return answer


# Driver code.
def main() -> None:
    V = 5

    edges = [
        [0, 1, 4], [0, 2, 1], [2, 1, 2],
        [1, 3, 1], [2, 3, 5], [3, 4, 3]
    ]

    source = 0

    sol = Solution()

    answer = sol.dijkstra(V, edges, source)

    print(*answer)


if __name__ == "__main__":
    main()