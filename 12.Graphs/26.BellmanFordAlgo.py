# Given a directed weighted graph with V vertices numbered from 0 to V-1, an edge list containing entries [from,to,weight], and a source vertex, compute the shortest distance from the source to every vertex.

# Negative edge weights are allowed. Store 100000000 for every unreachable vertex. Return [-1] when a negative-weight cycle is reachable from the source because finite shortest distances do not exist for the affected graph.

# Example 1
# Input: V = 5, edges = [[0,1,5],[1,2,1],[1,3,2],[2,4,1],[4,3,-1]], source = 0

# Output: [0,5,6,6,7]

# Explanation: The shortest distance to vertex 3 is 6 through path 0->1->2->4->3.

# Example 2
# Input: V = 4, edges = [[0,1,4],[1,2,-6],[2,3,5],[3,1,-2]], source = 0

# Output: [-1]

# Explanation: Cycle 1->2->3->1 has total weight -3 and is reachable from the source.

# Approach
# Bellman–Ford computes shortest distances by repeatedly scanning the complete edge list. After V-1 passes, every shortest simple path has propagated through at most V-1 edges.

# An additional edge scan detects reachable negative cycles. Any further improvement after V-1 passes indicates a repeatedly usable cycle having negative total weight.

# Algorithm
# Initialize every distance to 100000000, representing infinity, and set the source distance to 0.

# Perform at most V-1 relaxation passes and initialize an update flag as false before every pass.

# Traverse every edge and skip relaxation when the source endpoint remains unreachable.

# Calculate distance[from]+weight; upon finding a smaller value, update distance[to] and set the update flag to true.

# End the relaxation phase early when a complete pass produces no update, as all reachable shortest distances have stabilized.

# Scan every edge once more and return [-1] when any reachable edge can still be relaxed, confirming a negative cycle reachable from the source.

# Return the final distance array when no reachable negative cycle is detected.

from typing import List

class Solution:
    # Return shortest distances or [-1] for a reachable negative cycle.
    def bellmanFord(self, vertices: int, edges: List[List[int]], source: int) -> List[int]:
        INF = float("inf")
        dist = [INF] * vertices

        # Set the source distance before edge relaxation.
        dist[source] = 0

        # Relax every edge up to vertices - 1 times.
        for _ in range(vertices - 1):
            updated = False

            # Scan the complete directed edge list.
            for edge in edges:
                fromNode = edge[0]
                toNode = edge[1]
                weight = edge[2]

                # Ignore edges leaving unreachable vertices.
                if dist[fromNode] == INF:
                    continue

                # Record a shorter path through the departure vertex.
                if dist[fromNode] + weight < dist[toNode]:
                    dist[toNode] = dist[fromNode] + weight
                    updated = True

            # Stop after a pass with no distance change.
            if not updated:
                break

        # Detect a negative cycle reachable from the source.
        for edge in edges:
            fromNode = edge[0]
            toNode = edge[1]
            weight = edge[2]

            # A further relaxation means a reachable negative cycle exists.
            if dist[fromNode] != INF and dist[fromNode] + weight < dist[toNode]:
                return [-1]

        # Return all shortest distances.
        return dist


# Driver code.
def main() -> None:
    vertices = 5

    edges = [
        [0, 1, 5], [1, 2, 1], [1, 3, 2],
        [2, 4, 1], [4, 3, -1]
    ]

    sol = Solution()

    answer = sol.bellmanFord(vertices, edges, 0)

    print(*answer)


if __name__ == "__main__":
    main()