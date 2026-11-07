# Given a directed graph represented by an adjacency list, return all eventual safe nodes in ascending order.

# A terminal node has no outgoing edges. A safe node is a node from which every possible directed path eventually reaches a terminal node instead of getting trapped in a cycle.

# Example 1
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]

# Output: [2,4,5,6]

# Explanation: Nodes 2, 4, 5, and 6 cannot reach a directed cycle.

# Example 2
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]

# Output: [4]

# Explanation: Only node 4 is guaranteed to end at a terminal node.

# Approach 1
# Depth First Search tracks globally visited nodes, nodes in the active recursion path, and nodes proven safe. Reaching an active node confirms a directed cycle, while reaching a previously identified unsafe node confirms a path leading to a cycle.

# A node becomes safe only after every outgoing path reaches a safe node or a terminal node. Scanning the final safe array from index 0 to V-1 produces ascending output.

# Algorithm
# Initialize visited, pathVisited, and safe arrays of size V to track explored nodes, active-path nodes, and proven safe nodes.

# Traverse every node and start DFS from each unvisited node, ensuring coverage of all disconnected directed components.

# Mark the current node as visited and active in pathVisited before exploring outgoing edges.

# Return an unsafe result upon reaching an active neighbor, as an edge to the current recursion path confirms a directed cycle.

# Continue DFS for every unvisited neighbor; an unsafe recursive result or a previously visited unsafe neighbor also makes the current node unsafe.

# Remove the current node from pathVisited and mark the node safe only after every outgoing neighbor is proven safe.

# Scan nodes from 0 to V-1, collect all nodes marked safe, and return the resulting ascending list.

from typing import List

class Solution:
    # Checks whether a node is safe using DFS.
    def dfs(self, node: int, visited: List[int], pathVisited: List[int],
            safe: List[int], graph: List[List[int]]) -> bool:
        # Mark node as visited.
        visited[node] = 1

        # Mark node in active DFS path.
        pathVisited[node] = 1

        # Explore all outgoing neighbors.
        for neighbor in graph[node]:
            # Visit unvisited neighbor first.
            if not visited[neighbor]:
                # Unsafe neighbor makes current node unsafe.
                if not self.dfs(neighbor, visited, pathVisited, safe, graph):
                    return False

            # Active-path neighbor confirms a cycle.
            elif pathVisited[neighbor]:
                return False

            # Previously visited unsafe neighbor makes current node unsafe.
            elif not safe[neighbor]:
                return False

        # Remove node from active DFS path.
        pathVisited[node] = 0

        # Mark node as safe after all paths pass.
        safe[node] = 1

        # Return safe status for current node.
        return True

    # Returns all eventual safe nodes in ascending order.
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vertices = len(graph)

        visited = [0] * vertices
        pathVisited = [0] * vertices
        safe = [0] * vertices

        # Start DFS from every unvisited node.
        for node in range(vertices):
            if not visited[node]:
                self.dfs(node, visited, pathVisited, safe, graph)

        answer = []

        # Collect safe nodes in ascending order.
        for node in range(vertices):
            if safe[node]:
                answer.append(node)

        # Return all safe nodes.
        return answer


# Driver code.
def main() -> None:
    graph = [
        [1, 2],
        [2, 3],
        [5],
        [0],
        [5],
        [],
        []
    ]

    sol = Solution()

    print(*sol.eventualSafeNodes(graph))


if __name__ == "__main__":
    main()

# Complexity Analysis
# Time Complexity: O(V+E), where V and E are the numbers of nodes and directed edges; DFS processes every node and edge once.

# Space Complexity: O(V), where the state arrays and recursive DFS stack store a number of entries proportional to V.

# Approach 2
# Reverse Kahn’s Algorithm begins from terminal nodes, which are safe because no outgoing paths exist. Reversing every directed edge allows safe-state propagation from terminal nodes toward predecessors.

# The outdegree of a predecessor decreases whenever one outgoing neighbor is proven safe. An outdegree of 0 confirms that every outgoing path leads to a safe node.

# Algorithm
# Build a reverse adjacency list and compute the original outdegree of every node, allowing safe states to propagate toward predecessors.

# Add all nodes having outdegree 0 to a queue, since terminal nodes are safe by definition.

# Initialize a safe array to record every node proven to have no path leading to a directed cycle.

# Continue processing while the queue contains nodes, removing the front node and marking the node safe.

# Traverse every predecessor in the reverse graph and decrease the predecessor’s outdegree, representing one outgoing path proven safe.

# Add a predecessor to the queue when the outdegree becomes 0, as all outgoing paths now lead to safe nodes.

# Scan nodes from 0 to V-1, collect all marked nodes, and return the resulting ascending list.

from collections import deque
from typing import Deque, List

class Solution:
    # Function to find safe nodes using reverse Kahn BFS.
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vertices = len(graph)
        reverse_graph = [[] for _ in range(vertices)]
        outdegree = [0] * vertices

        # Reverse edges and count original outgoing edges.
        for node in range(vertices):
            outdegree[node] = len(graph[node])
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)

        queue: Deque[int] = deque()

        # Terminal nodes are safe starting points.
        for node in range(vertices):
            if outdegree[node] == 0:
                queue.append(node)

        safe: List[int] = []

        # Remove safe terminal paths from predecessors.
        while queue:
            node = queue.popleft()
            safe.append(node)

            for predecessor in reverse_graph[node]:
                outdegree[predecessor] -= 1
                if outdegree[predecessor] == 0:
                    queue.append(predecessor)

        safe.sort()
        return safe

# Driver code.
def main() -> None:
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]

    sol = Solution()
    print(sol.eventualSafeNodes(graph))

if __name__ == "__main__":
    main()
