# Given an array arr containing N positive multipliers, a starting value start, and a target value end, one operation selects any multiplier and replaces the current value with (current×multiplier)%100000.

# Return the minimum number of operations required to reach end from start. Return -1 when no multiplication sequence reaches the target.

# Constraints 0 ≤ start < 100000, 0 ≤ end < 100000
# Both start and end are valid modulo-100000 residues, allowing direct indexing in the distance array.

# Example 1
# Input: arr = [2,5,7], start = 3, end = 30

# Output: 2

# Explanation: Multiplication by 2 changes 3 into 6, and multiplication by 5 changes 6 into 30.

# Example 2
# Input: arr = [3,4,65], start = 7, end = 66175

# Output: 4

# Explanation: A shortest sequence is 7->21->63->4095->66175, using multipliers 3,3,65,65.

# Approach
# Modulo 100000 restricts every generated value to M=100000 possible residues. Every residue represents a graph node, while multiplication by an allowed value creates a directed edge to (current×multiplier)%M.

# Every edge represents one operation, so Breadth First Search explores residues in increasing operation count. A distance array marks each residue during first discovery, preventing repeated processing and preserving the shortest distance.

# Algorithm
# Return 0 when start equals end, since no multiplication is required.

# Initialize a distance array of size M=100000 with -1, where -1 represents an unvisited residue.

# Set distance[start]=0 and add start to a queue, establishing the initial BFS state.

# Continue BFS while the queue contains residues and remove the front residue.

# For every multiplier, calculate next=(current×multiplier)%M using a sufficiently wide integer type.

# For every unvisited next, assign distance[current]+1; return immediately upon reaching end, or add next to the queue.

# Return -1 when the queue becomes empty without discovering the target residue.

from collections import deque
from typing import Deque, List


class Solution:
    # Return the minimum multiplication count from start to end.
    def minimumMultiplications(
        self,
        arr: List[int],
        start: int,
        end: int,
    ) -> int:
        modulo = 100000

        # Handle the zero-operation case before BFS.
        if start == end:
            return 0

        distance = [-1] * modulo
        pending: Deque[int] = deque()

        # Mark and enqueue the initial residue.
        distance[start] = 0
        pending.append(start)

        # Explore residues in increasing multiplication count.
        while pending:
            current = pending.popleft()

            # Generate every residue reachable in one operation.
            for multiplier in arr:
                next_value = (current * multiplier) % modulo

                # Skip residues already reached with fewer operations.
                if distance[next_value] != -1:
                    continue

                # Record the first and therefore shortest distance.
                distance[next_value] = distance[current] + 1

                # Return immediately after the first target discovery.
                if next_value == end:
                    return distance[next_value]

                pending.append(next_value)

        # Report an unreachable target after BFS exhaustion.
        return -1


# Driver code.
def main() -> None:
    arr = [2, 5, 7]
    start = 3
    end = 30
    sol = Solution()
    print(sol.minimumMultiplications(arr, start, end))


if __name__ == "__main__":
    main()