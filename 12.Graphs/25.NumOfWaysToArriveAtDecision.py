# A city contains n intersections numbered from 0 to n - 1. Each road [u, v, time] connects intersections u and v in both directions and requires the stated travel time.

# The road network is connected, meaning every intersection can be reached from every other intersection.

# Return the number of distinct routes from intersection 0 to intersection n - 1 having minimum total travel time. Return the count modulo 109 + 7.

# Example 1
# Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

# Output: 4

# Explanation: Four routes take the minimum time 7: 0->6, 0->4->6, 0->1->2->5->6, and 0->1->3->5->6.

# Example 2
# Input: n = 2, roads = [[1,0,10]]

# Output: 1

# Explanation: The only route from intersection 0 to intersection 1 has travel time 10.

# Approach
# Dijkstra’s Algorithm processes intersections in increasing shortest travel time. A distance array stores the minimum travel time to every intersection, while a ways array stores the number of routes achieving the corresponding minimum.

# A strictly shorter route replaces both the distance and route count because previous routes become non-optimal. An equally short route preserves the distance and adds another group of shortest routes.

# Algorithm
# Build an undirected weighted adjacency list by storing every road in both directions with the corresponding travel time.

# Initialize all distances as infinity and all route counts as 0; set dist[0]=0, ways[0]=1, and insert {0, 0} into a min-heap.

# Continue processing while the heap contains entries and remove the intersection having the smallest travel time.

# Skip the removed entry when the heap time differs from the current stored distance, as the entry represents an outdated route.

# Traverse every adjacent road and calculate the candidate time as currentTime+roadTime.

# For a strictly shorter candidate, replace the neighbor distance, copy ways[current] into ways[neighbor], and insert the updated pair into the heap.

# For an equal candidate, add ways[current] to ways[neighbor] modulo 10^9+7; return ways[N-1] after heap processing finishes.

import heapq
from typing import List, Tuple


class Solution:
    # Return the number of shortest routes from 0 to n - 1.
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        modulo = 1_000_000_007
        adj: List[List[Tuple[int, int]]] = [[] for _ in range(n)]

        # Build an undirected weighted adjacency list.
        for u, v, travel_time in roads:
            adj[u].append((v, travel_time))
            adj[v].append((u, travel_time))

        infinity = float("inf")
        dist: List[float] = [infinity] * n
        ways: List[int] = [0] * n
        min_heap: List[Tuple[int, int]] = []

        # Initialize source distance and route count.
        dist[0] = 0
        ways[0] = 1
        heapq.heappush(min_heap, (0, 0))

        # Process intersections by smallest known travel time.
        while min_heap:
            current_distance, node = heapq.heappop(min_heap)

            # Skip an entry replaced by a shorter route.
            if current_distance != dist[node]:
                continue

            # Relax every road leaving the selected intersection.
            for neighbor, travel_time in adj[node]:
                candidate = current_distance + travel_time

                # Replace distance and inherit every shortest route.
                if candidate < dist[neighbor]:
                    dist[neighbor] = candidate
                    ways[neighbor] = ways[node]
                    heapq.heappush(min_heap, (candidate, neighbor))
                # Add another group of equally short routes.
                elif candidate == dist[neighbor]:
                    ways[neighbor] = (
                        ways[neighbor] + ways[node]
                    ) % modulo

        return ways[n - 1]


# Driver code.
def main() -> None:
    n = 7
    roads = [
        [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3],
        [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
        [0, 4, 5], [4, 6, 2]
    ]
    sol = Solution()
    print(sol.countPaths(n, roads))


if __name__ == "__main__":
    main()