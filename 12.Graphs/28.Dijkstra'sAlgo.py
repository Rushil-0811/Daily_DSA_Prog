# A network contains n nodes labeled from 1 to n. Each directed edge [u,v,w] means a signal needs w time units to travel from node u to node v.

# A signal starts from node k. Return the minimum time required for every node to receive the signal. Return -1 if at least one node cannot receive the signal.

# Example 1
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2

# Output: 2

# Explanation: Nodes 1 and 3 receive the signal after 1 time unit. Node 4 receives the signal through node 3 after 2 time units.

# Example 2
# Input: times = [[1,2,1]], n = 2, k = 2

# Output: -1

# Explanation: No directed route reaches node 1 from source node 2.

# Brute Force Approach
# Signal arrival time at a node equals the shortest directed-path distance from source k. Bellman–Ford repeatedly scans every directed edge, allowing each relaxation round to extend known shortest paths by one additional edge.

# A shortest simple path contains at most N-1 edges, so N-1 rounds are sufficient. The largest finite shortest distance represents the time required for the signal to reach the final node.

# Algorithm
# Initialize all distances as infinity and set distance[k] to 0, establishing node k as the signal source.

# Perform at most N-1 relaxation rounds, since no shortest simple path can contain more than N-1 edges.

# At the beginning of every round, initialize an update flag as false to detect whether any shorter route is discovered.

# Traverse every directed edge and skip relaxation when the starting node remains unreachable.

# When distance[source]+travelTime is smaller, update the destination distance and set the update flag to true.

# End the relaxation process when a complete round produces no update, as all shortest distances have stabilized.

# Scan all nodes, return -1 upon finding an infinite distance, and otherwise return the maximum distance as the network delay time.

from typing import List

class Solution:
    # Return minimum time required for every node to receive the signal.
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Infinity marks unreachable nodes.
        INF = float("inf")

        dist = [INF] * (n + 1)

        # Source receives the signal immediately.
        dist[k] = 0

        # Propagate shortest distances through at most n - 1 rounds.
        for _ in range(n - 1):
            changed = False

            # Relax every directed edge.
            for fromNode, toNode, travelTime in times:
                # Skip unreachable starting nodes.
                if dist[fromNode] == INF:
                    continue

                # Record a faster signal arrival.
                if dist[fromNode] + travelTime < dist[toNode]:
                    dist[toNode] = dist[fromNode] + travelTime
                    changed = True

            # Stop after no distance changes.
            if not changed:
                break

        answer = 0

        # Find the last signal arrival among all nodes.
        for node in range(1, n + 1):
            # If any node is unreachable, return -1.
            if dist[node] == INF:
                return -1

            answer = max(answer, dist[node])

            # Stop after processing the last node.
            if node == n:
                break

        # Return the final network delay time.
        return answer


# Driver code.
def main() -> None:
    times = [
        [2, 1, 1], [2, 3, 1], [3, 4, 1]
    ]

    n = 4
    k = 2

    sol = Solution()

    print(sol.networkDelayTime(times, n, k))


if __name__ == "__main__":
    main()