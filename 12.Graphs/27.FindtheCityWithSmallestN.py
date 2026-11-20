# Find the City with the Smallest Number of Neighbors at a Threshold Distance
# 201.7k
# Last Updated: 28 October 2026
# 0
# Given N cities numbered from 0 to N-1, an array of bidirectional weighted roads [first, second, weight], and a positive distanceThreshold, count the other cities reachable from every city with shortest-path distance at most the threshold.

# Every road has a positive weight. Positive road weights ensure that Dijkstra’s Algorithm and threshold-based pruning remain valid.

# Return the city having the smallest reachable-city count. Return the greatest city index when multiple cities share the minimum count.

# Example 1
# Input: N = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4

# Output: 3

# Explanation: Cities 0 and 3 each reach two other cities within the threshold. The greater tied index is 3.

# Example 2
# Input: N = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2

# Output: 0

# Explanation: City 0 reaches only city 1, producing the unique minimum count of one.

# Approach 1
# Floyd–Warshall computes shortest distances between every ordered pair of cities in a single matrix. A small city count makes cubic all-pairs processing practical, while the completed matrix supports direct threshold counting.

# Cities are checked in ascending index order. Updating the answer for an equal reachable-city count ensures selection of the greatest city index.

# Algorithm
# Initialize an N×N distance matrix with infinity and set every diagonal entry to 0.

# Store each undirected road in both matrix directions, retaining the minimum weight when multiple roads connect the same city pair.

# Run Floyd–Warshall using an outer loop for intermediate cities and inner loops for source and destination cities.

# Skip a transition when either required segment remains unreachable, preventing invalid infinity calculations.

# Update each source-to-destination distance with the smaller of the existing value and the route passing through the intermediate city.

# For every source city, count all other cities having a shortest distance less than or equal to the threshold.

# Update the answer when the count is smaller than or equal to the best count, then return the final city index.

from typing import List


class Solution:
    # Return the greatest-index city among minimum reachable counts.
    def findTheCity(
        self,
        n: int,
        edges: List[List[int]],
        distanceThreshold: int,
    ) -> int:
        infinity = 10**9
        dist = [[infinity] * n for _ in range(n)]

        # Set every zero-length self distance.
        for city in range(n):
            dist[city][city] = 0

        # Build the symmetric direct-distance matrix.
        for first, second, weight in edges:
            dist[first][second] = min(dist[first][second], weight)
            dist[second][first] = min(dist[second][first], weight)

        # Allow each city as an intermediate vertex.
        for middle in range(n):
            for source in range(n):
                for destination in range(n):
                    # Skip a route containing an unreachable segment.
                    if (
                        dist[source][middle] == infinity
                        or dist[middle][destination] == infinity
                    ):
                        continue

                    dist[source][destination] = min(
                        dist[source][destination],
                        dist[source][middle]
                        + dist[middle][destination],
                    )

        best_count = n
        answer = -1

        # Count threshold-reachable neighbors for every city.
        for city in range(n):
            count = 0
            for neighbor in range(n):
                if (
                    neighbor != city
                    and dist[city][neighbor] <= distanceThreshold
                ):
                    count += 1

            # Replace equal counts to preserve the greatest index.
            if count <= best_count:
                best_count = count
                answer = city

        return answer


# Driver code.
def main() -> None:
    n = 4
    edges = [
        [0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]
    ]
    sol = Solution()
    print(sol.findTheCity(n, edges, 4))


if __name__ == "__main__":
    main()

# Approach 2
# Positive road weights allow Dijkstra’s Algorithm to run independently from every source city. An adjacency list avoids an all-pairs matrix and improves efficiency for sparse graphs.

# Routes exceeding the threshold require no further expansion because additional positive edges cannot reduce the distance. Processing cities in ascending order with equal-count replacement preserves the greatest index.

# Algorithm
# Build an undirected weighted adjacency list, storing every road in both directions.

# Initialize bestCount as infinity and traverse every city in ascending order as a Dijkstra source.

# For each source, initialize all distances as infinity, set the source distance to 0, and insert the source into a min-heap.

# Remove minimum-distance states, skip stale entries, stop when the smallest distance exceeds the threshold, and count every finalized city except the source.

# Relax an adjacent edge only when the candidate distance is smaller and does not exceed the threshold, avoiding irrelevant heap states.

# Update bestCount and the answer when the current reachable-city count is smaller than or equal to the best count.

# Return the final answer after all source cities have been processed.

