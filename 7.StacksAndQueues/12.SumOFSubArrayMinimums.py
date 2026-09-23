# Given an integer array arr, consider every contiguous, non-empty subarray. Find the minimum value in each subarray and return the sum of all such minimum values modulo 109 + 7.

# Example 1
# Input: arr = [3, 1, 2, 4]
# Output: 17
# Explanation: The subarrays and their minimum values are:

# [3] → 3
# [3, 1] → 1
# [3, 1, 2] → 1
# [3, 1, 2, 4] → 1
# [1] → 1
# [1, 2] → 1
# [1, 2, 4] → 1
# [2] → 2
# [2, 4] → 2
# [4] → 4

# Therefore, the sum of all subarray minimums is 3 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 + 4 = 17.

# Brute Force Approach
# Every subarray can be formed by choosing a starting index and extending the ending index toward the right. As the subarray grows, only the newly added value can change its minimum.

# Instead of scanning the complete subarray again, maintain a running minimum during each extension. This avoids an extra loop and allows the minimum of every subarray to be added immediately.

# Algorithm
# Initialize answer = 0 and store modulo 109 + 7, because the total sum can become very large.

# Select every array index as the starting position of a subarray.

# Set currentMinimum to the starting value, because the first subarray contains only that element.

# Extend the ending index from the starting position to the end of the array, generating every subarray with the selected start.

# Update currentMinimum using the smaller value between the existing minimum and the newly added element.

# Add currentMinimum to answer after every extension, because each ending index forms one new subarray.

# Apply modulo after every addition to keep the result within the required range.

# Return the final value of answer after processing all subarrays.

from typing import List


class Solution:
    # Return the sum of all subarray minimums
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 1_000_000_007
        answer = 0
        n = len(arr)

        # Choose every possible starting index
        for start in range(n):
            current_minimum = arr[start]

            # Extend the current subarray to the right
            for end in range(start, n):
                # Keep the smallest value in the range
                current_minimum = min(current_minimum, arr[end])

                # Add the minimum for the current subarray
                answer = (answer + current_minimum) % mod

        # Return the required modular result
        return answer


# Driver code
def main() -> None:
    arr = [3, 1, 2, 4]
    obj = Solution()
    print(obj.sumSubarrayMins(arr))


if __name__ == "__main__":
    main()

# Complexity Analysis
# Time Complexity: O(N2), two nested loops visit every possible start-and-end pair once.

# Space Complexity: O(1), only a few scalar variables are stored outside the input array.

# Optimal Approach
# Instead of finding the minimum separately for every subarray, consider each arr[i] and calculate how many subarrays have arr[i] as their minimum. Once this frequency is known, its total contribution becomes arr[i] × frequency.

# For an element at index i, find how far it can extend toward the left and right while remaining the minimum. Let the previous strictly smaller element be the left boundary and the next smaller-or-equal element be the right boundary. Using a strict condition on one side and a non-strict condition on the other ensures that subarrays containing duplicate values are not counted more than once. Monotonic stacks allow both boundaries to be found efficiently.

# If leftChoices starting positions and rightChoices ending positions are available, every left choice can be paired with every right choice. Therefore, the number of subarrays where arr[i] is the selected minimum is:

# frequency = leftChoices × rightChoices

# Its contribution to the final answer is then arr[i] × leftChoices × rightChoices.

# Algorithm
# Initialize previousLess with -1 and nextLessOrEqual with N, where N is the size of the array. These values represent the absence of a valid boundary.

# Find the previous smaller elements for all indices:

# Traverse the array from left to right using a monotonic stack of indices.

# Remove indices while the stack-top value is greater than or equal to the current value, because the required left boundary must be strictly smaller.

# If the stack is not empty, store its top as previousLess[currentIndex]; otherwise, keep -1.

# Push the current index into the stack.

# Find the next smaller or equal elements for all indices:

# Clear the stack and traverse the array from right to left.

# Remove indices while the stack-top value is greater than the current value, because the required right boundary may be smaller or equal.

# If the stack is not empty, store its top as nextLessOrEqual[currentIndex]; otherwise, keep N.

# Push the current index into the stack.

# For every index, calculate:

# leftChoices = currentIndex - previousLess[currentIndex]

# rightChoices = nextLessOrEqual[currentIndex] - currentIndex

# Calculate frequency = leftChoices × rightChoices, because each valid starting position can be paired with each valid ending position.

# Add arr[currentIndex] × frequency to the answer and apply modulo 10^9 + 7.

# Return the final answer after processing every element.

from typing import List


class Solution:
    # Finds the previous strictly smaller index for every element.
    def _find_previous_less(self, arr: List[int]) -> List[int]:
        n = len(arr)
        previous_less = [-1] * n
        indices = []

        # Scan from left to right for previous boundaries.
        for i in range(n):
            # Remove values that are not strictly smaller.
            while indices and arr[indices[-1]] >= arr[i]:
                indices.pop()

            # A remaining index is the previous smaller boundary.
            if indices:
                previous_less[i] = indices[-1]

            # Save the current index for later elements.
            indices.append(i)

        return previous_less

    # Finds the next smaller-or-equal index for every element.
    def _find_next_less_or_equal(
        self, arr: List[int]
    ) -> List[int]:
        n = len(arr)
        next_less_or_equal = [n] * n
        indices = []

        # Scan from right to left for next boundaries.
        for i in range(n - 1, -1, -1):
            # Remove values that are strictly greater.
            while indices and arr[indices[-1]] > arr[i]:
                indices.pop()

            # A remaining index is the next valid boundary.
            if indices:
                next_less_or_equal[i] = indices[-1]

            # Save the current index for earlier elements.
            indices.append(i)

        return next_less_or_equal

    # Returns the sum of all subarray minimums.
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 1000000007

        previous_less = self._find_previous_less(arr)
        next_less_or_equal = self._find_next_less_or_equal(arr)

        answer = 0

        # Calculate each element's contribution as the minimum.
        for i in range(n):
            left_choices = i - previous_less[i]
            right_choices = next_less_or_equal[i] - i

            # Count all subarrays where arr[i] owns the minimum.
            contribution = (
                arr[i] * left_choices * right_choices
            ) % mod

            # Add the current contribution to the answer.
            answer = (answer + contribution) % mod

        return answer


# Driver code
def main():
    arr = [3, 1, 2, 4]

    obj = Solution()
    print(obj.sumSubarrayMins(arr))


if __name__ == "__main__":
    main()