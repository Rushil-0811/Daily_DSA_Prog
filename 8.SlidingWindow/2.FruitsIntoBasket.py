# Given an integer array fruits, where fruits[i] represents the type of fruit on the ith tree, return the maximum number of fruits you can collect.

# You have two baskets, and each basket can hold only one type of fruit.

# You must pick fruits from a continuous section of trees.

# Return the length of the longest continuous subarray that contains at most two distinct fruit types.

# Example 1
# Input: fruits = [1, 2, 1]

# Output: 3

# Explanation: We can collect all fruits because there are only two fruit types: 1 and 2.

# Brute Force Approach
# A valid collection can begin and end at any pair of tree positions. Therefore, every possible continuous section must receive examination.

# For each selected section, a fresh set records distinct fruit types. A section remains valid when the set contains at most two types. Complete checking guarantees the correct answer, but repeated scanning of overlapping sections creates considerable extra work.

# Algorithm
# Store the array size in n and return 0 when n == 0, because no fruit can be collected from an empty array.

# Initialize maxFruits = 0 to store the longest valid section found so far.

# Select every start index and consider each end from start onward so every possible continuous section can be examined.

# For every selected range fruits[start...end], use a fresh set and scan the range to count its distinct fruit types.

# If the set grows beyond two types, break the current end traversal, because every longer section beginning at the same start will still contain those three fruit types.

# Otherwise, update maxFruits with end - start + 1, then return it after all starting positions are processed.

class Solution:

    # Finds the longest valid section by checking every possible range.
    def total_fruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        max_fruits = 0

        # Try every tree as the beginning of a collection.
        for start in range(n):

            # Try every possible ending position for the current start.
            for end in range(start, n):
                types = set()

                # Count distinct fruit types inside the selected range.
                for i in range(start, end + 1):
                    types.add(fruits[i])

                    # More than two types makes this range invalid.
                    if len(types) > 2:
                        break

                # Longer ranges from this start will also remain invalid.
                if len(types) > 2:
                    break

                max_fruits = max(
                    max_fruits,
                    end - start + 1
                )

        return max_fruits


if __name__ == "__main__":
    fruits = [1, 2, 1, 2, 3]

    solution = Solution()

    print(solution.total_fruit(fruits))

# Complexity Analysis
# Time Complexity: O(N³), where N represents the array size. O(N²) continuous sections exist, and validation of one section may scan up to N elements.

# Space Complexity: O(1), because the validation set stores at most three fruit types before detecting an invalid section. The basket limit remains fixed at two.

# Better Approach
# The Brute Force Approach creates a section first and scans the complete section afterward. A better method builds each section gradually and remembers fruit frequencies during expansion.

# For every starting index, the end index moves toward the right while a frequency map tracks fruit types already included. Expansion stops immediately after a third type appears because every longer section from the same start will still contain at least three types.

# Algorithm
# Store the array size in n and return 0 when n equals 0.

# Initialize maxFruits with 0 for storing the best valid length found so far.

# Select every start index and create a fresh frequency map, because each new starting position represents an independent growing section.

# Move end from start toward the final index and increase the frequency of fruits[end] after adding the current fruit.

# Stop expansion when the map contains more than two fruit types, because every longer section from the same start will remain invalid.

# Update maxFruits with end - start + 1 for every valid expansion, then return maxFruits after processing all starting positions.

class Solution:

    # Finds the longest valid section by growing from every start.
    def total_fruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        max_fruits = 0

        # Try every tree as the beginning of a collection.
        for start in range(n):
            frequency = {}

            # Expand the section while at most two fruit types remain.
            for end in range(start, n):
                fruit = fruits[end]

                frequency[fruit] = (
                    frequency.get(fruit, 0) + 1
                )

                # A third type makes every later extension invalid.
                if len(frequency) > 2:
                    break

                max_fruits = max(
                    max_fruits,
                    end - start + 1
                )

        return max_fruits


if __name__ == "__main__":
    fruits = [1, 2, 1, 2, 3]

    solution = Solution()

    print(solution.total_fruit(fruits))

# Complexity Analysis
# Time Complexity: O(N²), where N represents the array size. Expansion from every starting index may process many later elements before a third fruit type appears.

# Space Complexity: O(1), because the frequency map stores at most three fruit types before expansion stops.

# Optimal Approach
# Starting a fresh expansion from every index repeats earlier work. A sliding window keeps one active section and allows both boundaries to move only forward.

# The right pointer adds fruits to the section. After a third type appears, a single left-side fruit is removed during the same iteration. A single if condition may leave the window temporarily invalid, but an invalid window never grows beyond the best valid length because one fruit enters and one fruit leaves together. The answer changes only after the window contains at most two fruit types again.

# Algorithm
# Initialize left and maxFruits with 0, and create a frequency map for tracking fruit counts inside the current window.

# Move right from 0 to n - 1 and increase the frequency of fruits[right], because the current fruit enters the window.

# When the map contains more than two fruit types, decrease the frequency of fruits[left], erase a zero-frequency entry, and move left one position forward.

# Allow temporary invalidity after the single left movement; equal addition and removal keep the current window length from increasing during an invalid state.

# Update maxFruits with right - left + 1 only when the map contains at most two fruit types.

# Return maxFruits after the right pointer processes every tree.

class Solution:

    # Finds the longest valid section using one forward sliding window.
    def total_fruit(self, fruits: list[int]) -> int:
        frequency = {}

        left = 0
        max_fruits = 0

        # Expand the window by adding each fruit from the right.
        for right in range(len(fruits)):
            fruit = fruits[right]

            frequency[fruit] = (
                frequency.get(fruit, 0) + 1
            )

            # Remove one left fruit when more than two types are present.
            if len(frequency) > 2:
                left_fruit = fruits[left]
                frequency[left_fruit] -= 1

                # Remove a type after its final fruit leaves the window.
                if frequency[left_fruit] == 0:
                    del frequency[left_fruit]

                left += 1

            # Only valid windows can contribute to the final answer.
            if len(frequency) <= 2:
                max_fruits = max(
                    max_fruits,
                    right - left + 1
                )

        return max_fruits


if __name__ == "__main__":
    fruits = [1, 2, 1, 2, 3]

    solution = Solution()

    print(solution.total_fruit(fruits))