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

from typing import List, Tuple, Deque


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

# BFS Approach
# In a directed acyclic graph, every edge goes from an earlier vertex to a later vertex in some topological ordering. That ordering is the key reason shortest paths can be found without repeatedly revisiting vertices.

# Kahn's algorithm creates this ordering using indegree counts. Vertices with no remaining incoming dependency are processed first, and removing them gradually exposes the next safe vertices.

# After the order is ready, the distance of each vertex is finalized enough to pass its value forward. Every outgoing edge can then improve the neighbor's distance. Since edges only move forward in the ordering, a later vertex never needs to affect an earlier one.

# Algorithm
# Build an adjacency list from the edge list, and store each outgoing neighbor with its edge weight.

# Compute the indegree of every vertex, then place all zero-indegree vertices into a queue.

# Repeatedly remove a vertex from the queue, append it to the topological order, reduce the indegree of its outgoing neighbors, and enqueue any neighbor whose indegree becomes zero.

# Initialize all distances as unreachable, then set the distance of source vertex 0 to 0; if no other vertex can be reached, these unreachable markers remain unchanged.

# Traverse the topological order and skip vertices that are still unreachable; for every reachable vertex, relax all outgoing edges.

# Convert every remaining unreachable distance to -1 and return the final distance array.

from typing import Deque

class Solution:
    # Returns shortest distances from source vertex 0.
    def shortest_path(self, V: int, E: int, edges: list[list[int]]) -> list[int]:
        adjacency: list[list[tuple[int, int]]] = [[] for _ in range(V)]
        indegree: list[int] = [0] * V

        # Build adjacency list and indegree values from the directed edges.
        for index in range(E):
            u: int = edges[index][0]
            v: int = edges[index][1]
            weight: int = edges[index][2]

            adjacency[u].append((v, weight))
            indegree[v] += 1

        nodes: Deque[int] = Deque()

        # Add every vertex that has no incoming edge.
        for node in range(V):
            # Zero-indegree vertices can start the topological ordering.
            if indegree[node] == 0:
                nodes.append(node)

        topo: list[int] = []

        # Remove vertices in BFS order while their outgoing edges reduce indegrees.
        while nodes:
            node: int = nodes.popleft()
            topo.append(node)

            for next_node, _ in adjacency[node]:
                indegree[next_node] -= 1

                # A neighbor becomes ready when all incoming dependencies are removed.
                if indegree[next_node] == 0:
                    nodes.append(next_node)

        INF: int = 10**18
        dist: list[int] = [INF] * V
        dist[0] = 0

        # Relax edges only after the source distance to a vertex is known.
        for node in topo:
            # Unreachable vertices cannot improve any neighbor.
            if dist[node] == INF:
                continue

            for next_node, weight in adjacency[node]:
                # A shorter path through the current vertex replaces the old distance.
                if dist[node] + weight < dist[next_node]:
                    dist[next_node] = dist[node] + weight

        answer: list[int] = [-1] * V

        for node in range(V):
            # Reachable vertices keep their computed shortest distance.
            if dist[node] != INF:
                answer[node] = dist[node]

        return answer


# Returns values as a space-separated string.
def join_values(values: list[int]) -> str:
    return " ".join(str(value) for value in values)


# Driver code
def main() -> None:
    V: int = 6
    E: int = 7
    edges: list[list[int]] = [
        [0, 1, 2],
        [0, 4, 1],
        [1, 2, 3],
        [4, 2, 2],
        [4, 5, 4],
        [2, 3, 6],
        [5, 3, 1],
    ]

    # instance for class Solution
    sol: Solution = Solution()
    answer: list[int] = sol.shortest_path(V, E, edges)
    print(join_values(answer))


if __name__ == "__main__":
    main()