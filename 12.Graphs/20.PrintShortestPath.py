# Given a weighted undirected graph with n vertices numbered from 1 to n and m edges, find a shortest path from vertex 1 to vertex n.

# Each edge appears as [u, v, weight] and every weight is positive. Return a list containing the total shortest-path weight first, followed by path vertices from 1 to n. Return [-1] if no path exists.

# Example 1
# Input: n = 5, m = 6, edges = [[1,2,2],[2,5,5],[2,3,4],[1,4,1],[4,3,3],[3,5,1]]

# Output: [5,1,4,3,5]

# Explanation: Path 1->4->3->5 has total weight 1+3+1=5, which is minimum.

# Example 2
# Input: n = 2, m = 0, edges = []

# Output: [-1]

# Explanation: Vertex 2 is unreachable from vertex 1.

# Approach
# Dijkstra’s Algorithm finds minimum distances from vertex 1 by repeatedly processing the smallest available distance. A min-heap provides efficient minimum selection, while an adjacency list supports traversal of weighted edges.

# A parent array records the predecessor responsible for every successful relaxation. After reaching vertex N, following parent links backward constructs the shortest route from N to 1, and reversal restores the forward path order.

# Algorithm
# Build an undirected weighted adjacency list by storing every edge in both directions with the corresponding weight.

# Initialize all distances as infinity, set parent[i]=i for every vertex, assign dist[1]=0, and insert {0, 1} into a min-heap.

# Continue processing while the heap contains entries and remove the distance–vertex pair having the smallest distance.

# Skip the removed entry when the heap distance differs from dist[current], as the entry represents an outdated route.

# For every adjacent edge, calculate dist[current]+weight; upon finding a smaller distance, update the neighbor’s distance, assign current as the parent, and insert the updated pair.

# Return [-1] when dist[N] remains infinity after heap processing, indicating that no path connects vertices 1 and N.

# Follow parent links from N back to 1, reverse the collected vertices, prepend dist[N], and return the shortest distance followed by the path.

from typing import List
import heapq

class Solution:
    # Return shortest weight followed by the path from 1 to n.
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n + 1)]

        # Build an undirected weighted adjacency list.
        for edge in edges:
            u = edge[0]
            v = edge[1]
            weight = edge[2]

            adj[u].append((v, weight))
            adj[v].append((u, weight))

        INF = float("inf")
        dist = [INF] * (n + 1)
        parent = [0] * (n + 1)

        # Initialize every vertex as its own parent.
        for vertex in range(1, n + 1):
            parent[vertex] = vertex

        minHeap = []

        # Start Dijkstra traversal from vertex 1.
        dist[1] = 0
        heapq.heappush(minHeap, (0, 1))

        # Process vertices in increasing known distance.
        while minHeap:
            currentDistance, node = heapq.heappop(minHeap)

            # Skip an outdated heap entry.
            if currentDistance != dist[node]:
                continue

            # Stop after destination distance becomes final.
            if node == n:
                break

            # Relax every edge leaving the selected vertex.
            for neighbor, weight in adj[node]:
                candidate = currentDistance + weight

                # Record a better distance and predecessor.
                if candidate < dist[neighbor]:
                    dist[neighbor] = candidate
                    parent[neighbor] = node
                    heapq.heappush(minHeap, (candidate, neighbor))

        # Return failure after an unreachable destination.
        if dist[n] == INF:
            return [-1]

        path = []
        node = n

        # Follow predecessor links from destination to source.
        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(1)

        # Reverse path into source-to-destination order.
        path.reverse()

        # Return shortest weight followed by path vertices.
        return [dist[n]] + path


# Driver code.
def main() -> None:
    n = 5
    m = 6

    edges = [
        [1, 2, 2], [2, 5, 5], [2, 3, 4],
        [1, 4, 1], [4, 3, 3], [3, 5, 1]
    ]

    sol = Solution()

    answer = sol.shortestPath(n, m, edges)

    print(*answer)


if __name__ == "__main__":
    main()
    