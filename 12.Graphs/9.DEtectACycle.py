# Given an undirected graph with V vertices represented by an adjacency list, determine whether any component contains a cycle.

# A cycle exists when a path starts and ends at the same vertex without reusing an edge. The graph can be disconnected, so every component must be checked.

# Example 1
# Input: V = 4, adj = [[1,2],[0,2],[0,1,3],[2]]

# Output: true

# Explanation: Vertices 0, 1, 2 form a cycle.

# Example 2
# Input: V = 4, adj = [[1],[0,2],[1,3],[2]]

# Output: false

# Explanation: The graph forms a straight chain with no cycle.

# Approach 1
# Depth First Search explores each connected component by following one path as deeply as possible before backtracking. Since every undirected edge appears in both directions, the edge leading back to the immediate parent represents normal traversal and must be ignored.

# Encountering an already visited neighbor different from the parent indicates an alternate route to a previously reached vertex, confirming a cycle. An outer traversal across all vertices ensures coverage of disconnected components.

# Algorithm
# Initialize a visited array of size V with all entries marked false, allowing previously explored vertices to be identified.

# Traverse every vertex and start DFS from each unvisited vertex with parent -1, ensuring that every disconnected component is examined.

# Mark the current vertex as visited upon entering DFS, preventing repeated recursive exploration.

# Examine every adjacent vertex of the current vertex to inspect all edges belonging to the component.

# For an unvisited neighbor, continue DFS with the current vertex as the parent and immediately propagate a detected cycle.

# For a visited neighbor, return true when the neighbor differs from the parent, as an alternate path confirms a cycle.

# Return false after all connected components finish without detecting a cycle.

from typing import List

class Solution:
    # Function to detect a cycle in an undirected graph.
    def isCycle(self, vertices: int, adj: List[List[int]]) -> bool:
        visited = [False] * vertices

        # Function to run DFS with parent tracking.
        def dfs(node: int, parent: int) -> bool:
            visited[node] = True

            # Explore every adjacent vertex.
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True

            # No cycle found through current DFS path.
            return False

        # Start DFS from every component.
        for node in range(vertices):
            if not visited[node]:
                if dfs(node, -1):
                    return True

        # No component contains a cycle.
        return False

# Driver code.
def main() -> None:
    vertices = 4
    adj = [[1, 2], [0, 2], [0, 1, 3], [2]]

    sol = Solution()
    print(str(sol.isCycle(vertices, adj)).lower())

if __name__ == "__main__":
    main()
