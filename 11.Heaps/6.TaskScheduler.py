# Given an array tasks containing uppercase English letters and a non-negative integer n, schedule every task in any order. Each CPU interval can execute one task or remain idle. Two executions with the same label must have at least n intervals between both executions.

# Return the minimum number of CPU intervals needed to finish every task, including any required idle intervals.

# Example 1
# Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
# Output: 8
# Explanation: One shortest schedule is A, B, idle, A, B, idle, A, B. Every pair of equal tasks has two intervening intervals.

# Example 2
# Input: tasks = ["A", "A", "B"], n = 0
# Output: 3
# Explanation: A zero cooldown permits consecutive equal tasks, so A, A, B finishes without idle time.

# Brute Force Approach
# A direct simulation can build the schedule one interval at a time. A frequency array records unfinished copies, while an availability array records the earliest legal interval for every task label.

# Every interval scans all 26 labels and selects the ready label with the largest remaining frequency. Giving early positions to frequent labels spreads repeated copies across the schedule and avoids unnecessary idle time.

# Algorithm
# Begin with a frequency array of size 26 so every unfinished task copy remains visible during the simulation.

# Keep an availableAt array initialized to interval 1, allowing every present label to run at the first simulated interval.

# Scan all task labels at every interval so only unfinished and legally available work can compete for the next position.

# Select the ready label with the largest remaining frequency because frequent labels need the most future cooldown gaps.

# Execute the selected label and move the next legal time forward by n + 1, so the required cooldown remains protected.

# Advance one interval without executing a task if no label is ready, because the cooldown restriction forces an idle position.

# Keep the elapsed interval count as the answer because every task and forced idle position contributes one interval.

from typing import List


class Solution:
    # Finds the minimum schedule length
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Store unfinished copies for every task label
        frequency = [0] * 26

        # Count each task before schedule simulation
        for task in tasks:
            frequency[ord(task) - ord("A")] += 1

        # Store the next legal interval for each label
        available_at = [0] * 26
        time = 0
        remaining = len(tasks)

        # Continue until every task copy is scheduled
        while remaining > 0:
            chosen = -1

            # Inspect every label for a ready frequent task
            for index in range(26):
                # A ready label can enter the current interval
                if (frequency[index] > 0 and
                        available_at[index] <= time):
                    # Larger remaining work receives priority
                    if (chosen == -1 or
                            frequency[index] > frequency[chosen]):
                        chosen = index

            # No ready label forces one idle interval
            if chosen == -1:
                time += 1
                continue

            # Execute one copy during the current interval
            frequency[chosen] -= 1
            remaining -= 1

            # Reuse becomes legal after n full intervals
            available_at[chosen] = time + n + 1
            time += 1

        # Elapsed intervals include every forced idle slot
        return time


# Driver code
def main() -> None:
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    obj = Solution()
    print(obj.leastInterval(tasks, n))


if __name__ == "__main__":
    main()

# Better Approach
# The repeated 26-label scan can be replaced by a max heap. The largest remaining frequency stays at the top, so the next useful task becomes available without a full search.

# A group of n + 1 intervals forms one safe cycle because any label can appear at most once inside the group. Unfinished frequencies return to the heap only after the cycle ends, preventing an early repeat.

# Algorithm
# Begin with a frequency array and place every positive count in a max heap so the largest remaining workload stays immediately accessible.

# Start a cycle with n + 1 available slots because equal labels placed in consecutive cycles receive the required separation.

# Remove up to n + 1 heap entries and save unfinished counts outside the heap so one label cannot run twice inside the same cycle.

# Keep removed counts away from the heap until the current cycle ends, preventing the same label from entering one cycle twice.

# Restore every unfinished count after the cycle so the next cycle again starts with the largest remaining workload.

# Add only the used slot count for the final cycle because no idle suffix is needed after all tasks finish.

# Add the full n + 1 cycle length while more work remains because unused positions inside an unfinished schedule are forced idle intervals.

# Keep the accumulated interval count as the answer because every completed cycle contributes task slots and forced idle slots.

import heapq
from typing import List


class Solution:
    # Finds the minimum schedule length
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count every task label before heap creation
        frequency = [0] * 26
        for task in tasks:
            frequency[ord(task) - ord("A")] += 1

        # Negative counts create max-heap behavior
        max_heap = []
        for count in frequency:
            # Only present task labels belong in the heap
            if count > 0:
                heapq.heappush(max_heap, -count)

        time = 0

        # Process one safe cooldown cycle at a time
        while max_heap:
            pending = []
            slots = n + 1
            used = 0

            # Execute distinct labels inside the cycle
            while slots > 0 and max_heap:
                count = -heapq.heappop(max_heap)

                # One execution removes one unfinished copy
                count -= 1
                used += 1
                slots -= 1

                # Positive counts need a later cycle
                if count > 0:
                    pending.append(count)

            # Restore labels only after the cycle closes
            for count in pending:
                heapq.heappush(max_heap, -count)

            # A final cycle needs no idle suffix
            if not max_heap:
                time += used
            else:
                time += n + 1

        # Accumulated cycles contain tasks and forced idles
        return time


# Driver code
def main() -> None:
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    obj = Solution()
    print(obj.leastInterval(tasks, n))


if __name__ == "__main__":
    main()

# Optimal Approach
# Heap simulation can be skipped after identifying the labels responsible for forced gaps. A label with maximum frequency maxFrequency creates maxFrequency - 1 complete blocks, and every complete block needs n + 1 positions.

# Several labels can share the maximum frequency. Every such label contributes one position after the complete blocks. A schedule with enough different tasks needs no idle time, so the larger value between the block length and the task count gives the answer.

# Algorithm
# Begin with a frequency array of size 26 so the workload of every task label can be counted in one pass.

# Find maxFrequency among all counts because the most repeated labels create the strongest cooldown restriction.

# Count maxFrequencyTasks, the number of labels reaching maxFrequency, because every tied label occupies the final block.

# Form maxFrequency - 1 complete blocks because the last occurrence of each most frequent label needs no following cooldown.

# Give every complete block n + 1 positions so consecutive copies of a most frequent label receive n intervening intervals.

# Add maxFrequencyTasks for the tied final occurrences so every busiest label receives a valid ending position.

# Compare the block-driven length with the total task count so plentiful distinct tasks can replace all potential idle positions.

from typing import List


class Solution:
    # Finds the minimum schedule length
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count every task label
        frequency = [0] * 26
        for task in tasks:
            frequency[ord(task) - ord("A")] += 1

        # Find the strongest cooldown bottleneck
        max_frequency = max(frequency)

        # Count labels sharing the strongest bottleneck
        max_frequency_tasks = 0
        for count in frequency:
            # Every tied label needs a final position
            if count == max_frequency:
                max_frequency_tasks += 1

        # Complete blocks preserve all cooldown gaps
        block_length = (
            (max_frequency - 1) * (n + 1) +
            max_frequency_tasks
        )

        # Total tasks dominate after all idle gaps fill
        return max(len(tasks), block_length)


# Driver code
def main() -> None:
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    obj = Solution()
    print(obj.leastInterval(tasks, n))


if __name__ == "__main__":
    main()