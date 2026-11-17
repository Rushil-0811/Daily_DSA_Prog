# here are n cities and m edges connected by some number of flights. Given an array of flights where flights[i] = [ fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei. Given three integers src, dst, and k, and return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1

# Output: 700

# Explanation: The optimal path with at most 1 stops from city 0 to 3 is marked in red and has cost 100 + 600 = 700.

# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1

# Output: 200

# Explanation:The optimal path with at most 1 stops from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

# Approach 1
# Bounded Bellman–Ford builds cheapest prices by flight count. After round r, the distance array stores the minimum price using at most r flights. Since K stops allow at most K+1 flights, exactly K+1 rounds cover every valid route.

# Each round reads from the previous distance layer and writes into a copy. Separate arrays prevent several flights from chaining within one round.

# Algorithm
# Initialize all city prices as infinity and set the source price to 0, establishing the starting state before taking any flight.

# Perform exactly K+1 rounds, since a route containing at most K intermediate stops can use at most K+1 flights.

# Copy the current distance array at the beginning of every round, preserving prices calculated with fewer flights.

# Traverse every directed flight and skip an edge when the departure city remains unreachable.

# Calculate the candidate price using the previous distance array and update the arrival city only in the copied array.

# Replace the distance array with the completed copy after processing all flights, advancing the allowed flight count by one.

# Return -1 when the destination remains unreachable; otherwise, return the minimum destination price.

from typing import List

class Solution:
    # Returns the cheapest price using at most k stops.
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Infinity marks unreachable states.
        INF = float("inf")

        # Store the cheapest price for each city.
        distance = [INF] * n

        # Set the zero-flight price for the source city.
        distance[src] = 0

        # Build prices using at most k + 1 flights.
        for used in range(k + 1):
            nextDistance = distance[:]

            # Relax every directed flight from the previous layer.
            for flight in flights:
                fromCity = flight[0]
                toCity = flight[1]
                price = flight[2]

                # Skip unreachable departure cities.
                if distance[fromCity] == INF:
                    continue

                # Update only the next flight-count layer.
                nextDistance[toCity] = min(
                    nextDistance[toCity],
                    distance[fromCity] + price
                )

            # Move to the next layer after all flights are relaxed.
            distance = nextDistance

        # Convert an unreachable destination into -1.
        return -1 if distance[dst] == INF else distance[dst]


# Driver code.
def main() -> None:
    n = 4

    flights = [
        [0, 1, 100], [1, 2, 100], [2, 0, 100],
        [1, 3, 600], [2, 3, 200]
    ]

    solution = Solution()

    print(solution.findCheapestPrice(n, flights, 0, 3, 1))


if __name__ == "__main__":
    main()

# Approach 2
# State-aware Dijkstra treats {flightsUsed, city} as the complete state. Reaching the same city with different flight counts creates different remaining possibilities, so a city-only distance array is insufficient.

# A min-heap processes the lowest-cost valid state first. Non-negative flight prices make the first destination state removed from the heap the cheapest valid route.

# Algorithm
# Build a directed weighted adjacency list from all flights, storing each destination city with the corresponding price.

# Initialize a best table with K+2 flight layers and N cities, where every entry initially contains infinity.

# Set best[0][source]=0 and insert {0, source, 0} into a min-heap, representing zero price with no flights used.

# Continue processing while the heap contains states, remove the state having the smallest price, and skip stale entries that differ from the matching table value.

# Return the current price when the removed city is the destination, as no cheaper valid state remains in the min-heap.

# When fewer than K+1 flights have been used, relax every outgoing flight into the next layer and insert each improved state into the heap.

# Return -1 when the heap becomes empty without reaching the destination within the allowed flight count.

from typing import List
import heapq

class Solution:
    # Returns the cheapest price using at most k stops.
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the directed weighted adjacency list.
        adjacency = [[] for _ in range(n)]

        for flight in flights:
            adjacency[flight[0]].append((flight[1], flight[2]))

        # Infinity marks unreachable states.
        INF = float("inf")
        maxFlights = k + 1

        # Store the best price for every flight-count and city state.
        best = [[INF] * n for _ in range(maxFlights + 1)]

        # Process states by increasing total price.
        minHeap = []

        # Start from source with zero flights and zero price.
        best[0][src] = 0
        heapq.heappush(minHeap, (0, src, 0))

        while minHeap:
            cost, city, used = heapq.heappop(minHeap)

            # Skip states replaced by cheaper matching states.
            if cost != best[used][city]:
                continue

            # Destination popped first is the cheapest valid answer.
            if city == dst:
                return cost

            # Stop paths exceeding k + 1 flights.
            if used == maxFlights:
                continue

            # Relax outgoing flights into the next layer.
            for neighbor, price in adjacency[city]:
                nextUsed = used + 1
                nextCost = cost + price

                # Update only when the new price is cheaper.
                if nextCost < best[nextUsed][neighbor]:
                    best[nextUsed][neighbor] = nextCost
                    heapq.heappush(minHeap, (nextCost, neighbor, nextUsed))

        # Return -1 when destination cannot be reached.
        return -1


# Driver code.
def main() -> None:
    n = 4

    flights = [
        [0, 1, 100], [1, 2, 100], [2, 0, 100],
        [1, 3, 600], [2, 3, 200]
    ]

    solution = Solution()

    print(solution.findCheapestPrice(n, flights, 0, 3, 1))


if __name__ == "__main__":
    main()