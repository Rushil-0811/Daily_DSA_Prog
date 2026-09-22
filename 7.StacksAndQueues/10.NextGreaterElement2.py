# An integer array nums is treated as circular, so traversal continues from the first position after the final position. For every array position, find the first value encountered later in circular order with a strictly greater value.

# Store -1 when a full circular search contains no greater value. Return all answers in the original position order.

# Example 1
# Input: nums = [1, 2, 1]
# Output: [2, -1, 2]
# Explanation: The first 1 reaches 2 directly. Value 2 has no greater value. The final 1 wraps around and reaches 2.

# Brute Force Approach
# Since the array is circular, the search for the Next Greater Element can continue from the beginning after reaching the last index. Modulo indexing allows this wraparound without creating another array.

# For each element, check only the next N - 1 positions, because the element should not be compared with itself. The first strictly greater value encountered is its Next Greater Element. If no such value is found, the answer remains -1.

# Algorithm
# Create an answer array of size N and initialize every position with -1, because some elements may not have a greater value in circular order.

# Consider each array index as the current starting position.

# Check offsets from 1 to N - 1, so every other position is visited exactly once.

# Calculate the candidate index using (currentIndex + offset) % N, so the search wraps back to index 0 after reaching the end.

# Compare the candidate value with the current value.

# When a strictly greater value is found:

# Store that value in the corresponding answer position.

# Stop searching because the first greater value encountered is the nearest one in circular order.

# Keep -1 if no greater value is found.

# Return the completed answer array.

from typing import List


class Solution:
    # Finds next greater values by circular scanning.
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n

        # Process every position independently.
        for i in range(n):
            # Check one round after the starting position.
            for offset in range(1, n):
                next_index = (i + offset) % n

                # A larger value ends the nearest search.
                if nums[next_index] > nums[i]:
                    answer[i] = nums[next_index]
                    break

        return answer


# Driver code
def main() -> None:
    nums = [2, 1, 2, 4, 3]
    obj = Solution()
    print(obj.nextGreaterElements(nums))


if __name__ == "__main__":
    main()

# Complexity Analysis
# Time Complexity: O(N2), because every position may inspect the other N - 1 positions during a full circular search.

# Space Complexity: O(N), because the returned answer array stores one result per position; auxiliary space apart from the returned array is O(1).

# Optimal Approach
# The efficient way to find the Next Greater Element is already discussed in the Next Greater Element problem using a monotonic stack. The only additional challenge here is handling the circular nature of the array.

# Handling circular arrays:
# One way is to copy the array and append it again, but this uses extra space. Instead, we can hypothetically double the array using the modulus operator. Traverse from 2 * N - 1 to 0 and access elements using index % N.

# In the first pass, only prepare the stack. In the second pass, use the stack top as the Next Greater Element if available; otherwise, store -1. After processing each element, push it into the stack for future comparisons.

# Algorithm
# Initialize an answer array of size N with -1 and an empty stack to store possible next-greater candidates.

# Traverse virtual indices from 2 * N - 1 down to 0, simulating two reverse passes for circular array coverage.

# Map each virtual index using index % N, allowing access to valid array positions after crossing the first index.

# Remove stack values smaller than or equal to nums[index], because such values cannot become a next greater answer for the current position or any farther-left position.

# Store the stack top in answer[index] only during the real pass when a greater candidate remains available.

# Push nums[index] after processing the current position, allowing the current value to become a candidate for positions farther left.

# Return the completed answer array after both virtual passes finish.

from typing import List


class Solution:
    # Finds next greater values with a monotonic stack.
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        candidates: List[int] = []

        # Two reverse passes simulate circular order.
        for i in range(2 * n - 1, -1, -1):
            index = i % n

            # Blocked values cannot be strictly greater.
            while candidates and candidates[-1] <= nums[index]:
                candidates.pop()

            # Only the real pass writes final answers.
            if i < n and candidates:
                answer[index] = candidates[-1]

            candidates.append(nums[index])

        return answer


# Driver code
def main() -> None:
    nums = [2, 1, 2, 4, 3]
    obj = Solution()
    print(obj.nextGreaterElements(nums))


if __name__ == "__main__":
    main()