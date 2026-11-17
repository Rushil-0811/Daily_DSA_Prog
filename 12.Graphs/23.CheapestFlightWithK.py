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