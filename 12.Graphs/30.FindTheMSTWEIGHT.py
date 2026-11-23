# Given a connected, undirected, weighted graph with V vertices numbered from 0 to V - 1 and E edges, find the sum of edge weights in a minimum spanning tree.

# Every edge is represented as [source, destination, weight]. A minimum spanning tree connects every vertex, contains no cycle, uses exactly V - 1 edges, and has the smallest possible total edge weight.

# Example 1
# Input: V = 4, edges = [[0,1,1],[1,2,2],[2,3,3],[0,3,4]]

# Output: 6

# Explanation: Edges (0,1), (1,2), and (2,3) connect all vertices with total weight 1 + 2 + 3 = 6.

# Example 2
# Input: V = 3, edges = [[0,1,5],[1,2,10],[2,0,15]]

# Output: 15

# Explanation: Edges (0,1) and (1,2) connect all vertices with total weight 5 + 10 = 15.

# Approach 1
# Prim's algorithm grows one connected tree from an arbitrary starting vertex. A min-heap stores candidate edges crossing from selected vertices to unselected vertices, so the lightest available connection is processed first.

# A visited array prevents duplicate heap entries from adding the same vertex more than once. The cut property guarantees safety for every accepted minimum crossing edge. Prerequisite concepts include adjacency lists, priority queues, greedy selection, and the cut property.

# Algorithm
# Build an undirected adjacency list so every vertex can access all of its connected edges.

# Initialize a min-heap with vertex 0 and weight 0 because Prim's algorithm can begin from any vertex.

# Remove the minimum-weight entry because the lightest available connection is the best candidate for extending the MST.

# Skip the entry when its vertex is already visited because that vertex has already been included in the MST.

# Mark the vertex as visited, add its edge weight to the MST weight, and increase the included-vertex count.

# Push every edge connecting the selected vertex to an unvisited neighbor because these edges become candidates for the next selection.

# Continue selecting the minimum-weight valid edge until all V vertices are included.

# Return the accumulated MST weight.

import heapq
from typing import List, Tuple


class Solution:
    # Function to compute MST weight using a binary min-heap.
    def spanningTree(self, vertices: int, edges: List[List[int]]) -> int:
        # Build an undirected adjacency list.
        adjacency: List[List[Tuple[int, int]]] = [
            [] for _ in range(vertices)
        ]
        for source, destination, weight in edges:
            adjacency[source].append((destination, weight))
            adjacency[destination].append((source, weight))

        # Store pairs as (connection weight, destination vertex).
        min_heap: List[Tuple[int, int]] = [(0, 0)]
        in_mst = [False] * vertices
        total_weight = 0
        included_vertices = 0

        # Grow one tree until every vertex becomes part of the MST.
        while min_heap and included_vertices < vertices:
            weight, node = heapq.heappop(min_heap)

            # Ignore stale entries for vertices already selected.
            if in_mst[node]:
                continue

            # Accept the cheapest edge crossing the current cut.
            in_mst[node] = True
            total_weight += weight
            included_vertices += 1

            # Add candidate edges leading outside the growing tree.
            for neighbor, edge_weight in adjacency[node]:
                if not in_mst[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

        # Return the total MST weight.
        return total_weight


# Driver function with a hard-coded graph.
def main() -> None:
    vertices = 4
    edges = [
        [0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 4]
    ]

    solution = Solution()
    print(solution.spanningTree(vertices, edges))


if __name__ == "__main__":
    main()