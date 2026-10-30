# An integer array nums and a positive integer k are given. Every distinct value has a frequency equal to the number of occurrences in nums.

# Return exactly k distinct values having the highest frequencies. Result order does not matter, and a unique answer is guaranteed.

# Example 1
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
# Explanation: Value 1 appears 3 times, value 2 appears 2 times, and value 3 appears once. Values 1 and 2 have the two highest frequencies.

# Example 2
# Input: nums = [4], k = 1
# Output: [4]
# Explanation: Value 4 is the only distinct value, so the single required result is 4.

# Brute Force Approach
# The frequency of each value must be known before deciding which elements appear most often. A hash map makes this easy by storing one count for every distinct value. After counting, sorting the distinct values by decreasing frequency places the most frequent values first.

# Only the first k values are required after sorting. This approach is simple and easy to understand, but it sorts all distinct values even though only the top k are needed.

# Algorithm
# Create a hash map named frequency to store the occurrence count of every distinct value.

# Traverse nums and increase the corresponding count, because the most frequent values can only be identified after their frequencies are known.

# Copy all distinct values from the hash map into a list named values, so they can be sorted using their stored frequencies.

# Sort values in decreasing order of frequency, because higher-frequency values must appear first.

# Keep any order among values with equal frequency because the result may be returned in any order.

# Take the first k values from the sorted list, because they have the highest frequencies.

# Return these k values as the result.

from typing import Dict, List


class Solution:
    # Finds top k values by sorting distinct values.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency: Dict[int, int] = {}

        # Save one occurrence count for every value.
        for value in nums:
            frequency[value] = frequency.get(value, 0) + 1

        # Place larger saved frequencies first.
        values = sorted(
            frequency.keys(),
            key=lambda value: frequency[value],
            reverse=True,
        )

        answer: List[int] = []

        # Copy only the first k sorted values.
        for index in range(k):
            answer.append(values[index])

        return answer


# Driver code
def main() -> None:
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    obj = Solution()
    print(obj.topKFrequent(nums, k))


if __name__ == "__main__":
    main()

# Better Approach
# Sorting all distinct values is unnecessary because only the top k frequencies matter. A min-heap of size k keeps only the strongest candidates, with the smallest frequency among them always available at the root.

# Each distinct value is inserted once. Whenever the heap grows beyond k, remove the root because that value cannot remain among the current top k frequencies. After all values are processed, the heap contains exactly the required candidates.

# Algorithm
# Create a hash map named frequency to store the occurrence count of every distinct value.

# Traverse nums and update the count of each value, because heap comparisons need the complete frequencies.

# Create an empty min-heap to store (frequency, value) pairs, so the weakest retained candidate stays at the root.

# Insert every distinct value with its frequency into the heap, allowing each value to compete for a top-k position.

# If the heap size becomes greater than k, remove the root because the smallest frequency is no longer needed.

# After processing all distinct values, extract the remaining heap values into the result.

# Return the result because the heap now contains exactly the k most frequent values.

import heapq
from typing import Dict, List, Tuple


class Solution:
    # Finds top k values with a bounded min-heap.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency: Dict[int, int] = {}

        # Save one occurrence count for every value.
        for value in nums:
            frequency[value] = frequency.get(value, 0) + 1

        min_heap: List[Tuple[int, int]] = []

        # Let every distinct value compete for the heap.
        for value, count in frequency.items():
            heapq.heappush(min_heap, (count, value))

            # An overflow contains one weak candidate.
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        answer: List[int] = []

        # Extract every retained top-frequency value.
        while min_heap:
            count, value = heapq.heappop(min_heap)
            answer.append(value)

        return answer


# Driver code
def main() -> None:
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    obj = Solution()
    print(obj.topKFrequent(nums, k))


if __name__ == "__main__":
    main()

# Optimal Approach
# The largest possible frequency equals the array length. A bucket array can therefore use frequency as an index, placing every distinct value directly into the matching occurrence-count group.

# Scanning buckets from high frequency to low frequency visits the most popular groups first. Collection stops after k values, removing all comparison sorting and heap maintenance.

# Algorithm
# Begin with a hash map named frequency, so every distinct value receives a complete occurrence count.

# Scan all values in nums once and increase matching counts, allowing direct bucket placement after counting ends.

# Create n + 1 buckets because a value frequency ranges from 1 through the array length n.

# Place every distinct value into the bucket indexed by the saved frequency, so bucket position represents popularity without comparisons.

# Scan bucket indices from n down to 1, ensuring larger frequencies contribute result values before smaller frequencies.

# Append values from each visited bucket and stop at result size k, avoiding unnecessary scans through lower-frequency groups.

# Return the collected values because descending bucket traversal selects exactly the highest-frequency groups.

from typing import Dict, List


class Solution:
    # Finds top k values with frequency buckets.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency: Dict[int, int] = {}

        # Save one occurrence count for every value.
        for value in nums:
            frequency[value] = frequency.get(value, 0) + 1

        n = len(nums)
        buckets: List[List[int]] = [[] for count in range(n + 1)]

        # Group values by exact occurrence count.
        for value, count in frequency.items():
            buckets[count].append(value)

        answer: List[int] = []

        # Visit larger frequencies before smaller ones.
        for count in range(n, 0, -1):
            # Collect every value from the current group.
            for value in buckets[count]:
                answer.append(value)

                # Exactly k values complete the result.
                if len(answer) == k:
                    return answer

        return answer


# Driver code
def main() -> None:
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    obj = Solution()
    print(obj.topKFrequent(nums, k))


if __name__ == "__main__":
    main()