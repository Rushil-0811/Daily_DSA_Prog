# Given a directed graph with V vertices represented by an adjacency list, determine whether any directed cycle exists.

# A directed cycle exists when traversal follows edge directions and returns to a vertex already present in the same active path. The graph can be disconnected, so every component must be checked.

# Example 1
# Input: V = 4, adj = [[1],[2],[0,3],[]]

# Output: true

# Explanation: Directed edges 0 -> 1 -> 2 -> 0 form a cycle.

# Example 2
# Input: V = 4, adj = [[1,2],[2],[3],[]]

# Output: false

# Explanation: All directed paths move forward without returning to an active vertex.

# Approach 1
# Depth First Search maintains two states: vertices visited during the complete traversal and vertices present in the current active recursion path. Reaching a vertex already present in the active path indicates a back edge and confirms a directed cycle.

# After all outgoing edges of a vertex are processed, removal from the active path allows later DFS branches to visit the vertex without incorrectly reporting a cycle.

# Algorithm
# Initialize visited and pathVisited arrays of size V, separating globally processed vertices from vertices in the active DFS path.

# Traverse every vertex and start DFS from each unvisited vertex, ensuring that all disconnected components are examined.

# Mark the current vertex in both arrays, recording global visitation and active-path membership.

# Examine every outgoing neighbor of the current vertex to inspect all possible directed paths.

# For an unvisited neighbor, continue DFS and immediately propagate true when a deeper recursive call detects a cycle.

# Return true when a neighbor is already marked in pathVisited, as an edge to an active-path vertex confirms a directed cycle.

# Remove the current vertex from pathVisited after processing all neighbors, and return false when every component finishes without detecting a cycle.

from typing import List

class Solution:
    # Detects a back edge using DFS.
    def dfs(self, node: int, visited: List[int], pathVisited: List[int], adj: List[List[int]]) -> bool:
        # Mark the node as visited.
        visited[node] = 1

        # Mark the node in the current DFS path.
        pathVisited[node] = 1

        # Explore all outgoing edges.
        for neighbor in adj[node]:
            # Visit the neighbor if it is not visited.
            if not visited[neighbor]:
                # If a cycle is found deeper, return true.
                if self.dfs(neighbor, visited, pathVisited, adj):
                    return True

            # If neighbor is in the current path, a cycle exists.
            elif pathVisited[neighbor]:
                return True

        # Remove current vertex from active DFS path.
        pathVisited[node] = 0

        # No cycle found from this path.
        return False

    # Detects a cycle in a directed graph.
    def isCyclic(self, vertices: int, adj: List[List[int]]) -> bool:
        visited = [0] * vertices
        pathVisited = [0] * vertices

        # Start DFS from every unvisited vertex.
        for node in range(vertices):
            # Only unvisited nodes can start a new DFS.
            if not visited[node]:
                # If any DFS finds a cycle, return true.
                if self.dfs(node, visited, pathVisited, adj):
                    return True

        # No back edge exists in any component.
        return False


# Driver code.
if __name__ == "__main__":
    vertices = 4

    adj = [
        [1],
        [2],
        [0, 3],
        []
    ]

    sol = Solution()

    print(str(sol.isCyclic(vertices, adj)).lower())

# Complexity Analysis
# Time Complexity: O(V+E), where V and E are the numbers of vertices and directed edges; DFS processes every vertex and edge once.

# Space Complexity: O(V), where both visited arrays and the recursive DFS stack store a number of entries proportional to V.

# Approach 2
# Kahn’s Algorithm applies topological-sorting logic to detect a cycle. In a directed acyclic graph, repeated removal of vertices having indegree 0 eventually processes every vertex.

# Vertices belonging to a directed cycle never reach indegree 0 because every cycle vertex retains an incoming edge. A processed count smaller than V therefore confirms a cycle.

# Algorithm
# Initialize an indegree array of size V, where each entry stores the number of incoming edges for a vertex.

# Scan every directed edge and increment the indegree of the destination vertex, preparing the dependency count required by Kahn’s Algorithm.

# Add all vertices having indegree 0 to a queue, since such vertices have no unresolved incoming dependencies.

# Initialize processedCount to 0 and continue processing while the queue contains vertices.

# Remove the front vertex and increment processedCount, recording successful removal from the topological ordering.

# Decrease the indegree of every outgoing neighbor and add a neighbor to the queue when the indegree becomes 0.

# Return true when processedCount differs from V; otherwise, return false because all vertices formed a valid topological order.

from typing import List
from collections import deque

class Solution:
    # Detects a cycle using Kahn's Algorithm.
    def isCyclic(self, vertices: int, adj: List[List[int]]) -> bool:
        indegree = [0] * vertices

        # Compute indegree for every vertex.
        for node in range(vertices):
            for neighbor in adj[node]:
                indegree[neighbor] += 1

        q = deque()

        # Add all vertices with zero indegree.
        for node in range(vertices):
            # Zero indegree means this node can be processed first.
            if indegree[node] == 0:
                q.append(node)

        processed = 0

        # Remove zero-indegree vertices one by one.
        while q:
            node = q.popleft()

            # Count this node as processed.
            processed += 1

            # Reduce indegree of outgoing neighbors.
            for neighbor in adj[node]:
                indegree[neighbor] -= 1

                # If indegree becomes zero, add it to the queue.
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # If some vertices remain unprocessed, a cycle exists.
        return processed != vertices


# Driver code.
if __name__ == "__main__":
    vertices = 4

    adj = [
        [1, 2],
        [2],
        [3],
        []
    ]

    sol = Solution()

    print(str(sol.isCyclic(vertices, adj)).lower())