# Given an integer array nums and an integer k, return the number of nice subarrays.

# A nice subarray is a contiguous subarray that contains exactly k odd numbers.

# A subarray is a contiguous part of the array.

# Example 1
# Input: nums = [1, 1, 2, 1, 1], k = 3

# Output: 2

# Explanation: The nice subarrays are [1, 1, 2, 1] and [1, 2, 1, 1]. Both contain exactly 3 odd numbers.

# Brute Force Approach
# Every possible subarray can be checked independently. For each selected range, count its odd elements from scratch and increase the answer when that count equals k.

# This guarantees that every nice subarray is found, but overlapping ranges repeatedly process the same elements.

# Algorithm
# The size of the array is stored in n. If n is 0, 0 is returned because no subarray can be formed from an empty array.

# A helper function is used to count odd numbers inside a subarray from start to end. This keeps the brute force logic clear because every subarray is checked separately.

# Inside the helper function, the elements from start to end are traversed. Whenever an element is odd, the odd count is increased.

# A variable count is initialized with 0. This stores the total number of nice subarrays found so far.

# Two loops are used to generate every possible subarray. The first loop chooses the starting index start, and the second loop chooses the ending index end.

# For every subarray, the helper function returns the number of odd elements. If this odd count is exactly equal to k, count is increased by 1. After all subarrays are checked, count is returned.

class Solution:

    # Counts odd numbers inside the selected subarray.
    def count_odds(
        self,
        nums: list[int],
        start: int,
        end: int
    ) -> int:
        odd_count = 0

        # Check every element inside the selected range.
        for i in range(start, end + 1):

            # Increase the count when the current value is odd.
            if nums[i] % 2 != 0:
                odd_count += 1

        return odd_count

    # Counts subarrays containing exactly k odd numbers.
    def number_of_subarrays(
        self,
        nums: list[int],
        k: int
    ) -> int:
        n = len(nums)

        # No non-empty subarray can be formed.
        if n == 0:
            return 0

        count = 0

        # Choose every possible starting index.
        for start in range(n):

            # Choose every possible ending index for the current start.
            for end in range(start, n):
                odd_count = self.count_odds(
                    nums,
                    start,
                    end
                )

                # Count the subarray when it contains exactly k odd values.
                if odd_count == k:
                    count += 1

        return count


if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 3

    solution = Solution()

    print(solution.number_of_subarrays(nums, k))

# Complexity Analysis
# Time Complexity: O(N³), where N is the size of the array. There are O(N²) possible subarrays, and counting odd numbers inside each subarray can take O(N) time.

# Space Complexity: O(1), because only a few variables are used and no extra data structure is required.

# Better Approach
# Instead of recounting odd elements for every range, fix start and maintain oddCount while end moves right.

# Because extending a subarray can never decrease its number of odd elements, expansion can stop once oddCount > k.

# Algorithm
# The size of the array is stored in n. If n is 0, 0 is returned because no subarray can exist.

# A variable count is initialized with 0. This stores the number of subarrays that contain exactly k odd numbers.

# The array is traversed using start as the starting index of the subarray. For every start, oddCount is initialized with 0 because a new subarray is being built.

# The end pointer moves from start to the end of the array. If nums[end] is odd, oddCount is increased.

# If oddCount becomes exactly equal to k, the current subarray from start to end is nice, so count is increased by 1.

# If oddCount becomes greater than k, the loop stops for this start. This is safe because adding more elements can only keep the odd count same or increase it, never decrease it. After all starting positions are checked, count is returned.

class Solution:

    # Counts nice subarrays using a running odd count from every start.
    def number_of_subarrays(
        self,
        nums: list[int],
        k: int
    ) -> int:
        n = len(nums)

        # No non-empty subarray can be formed.
        if n == 0:
            return 0

        count = 0

        # Choose every possible starting index.
        for start in range(n):
            odd_count = 0

            # Extend the current subarray while maintaining its odd count.
            for end in range(start, n):

                # Include the current value when it is odd.
                if nums[end] % 2 != 0:
                    odd_count += 1

                # Count the range when exactly k odd values are present.
                if odd_count == k:
                    count += 1

                # Further expansion cannot reduce the number of odd values.
                if odd_count > k:
                    break

        return count


if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 3

    solution = Solution()

    print(solution.number_of_subarrays(nums, k))

# Complexity Analysis
# Time Complexity: O(N²), where N is the size of the array. For every starting index, the ending index may move toward the right until the odd count becomes greater than k.

# Space Complexity: O(1), because only variables like oddCount and count are used.

# Optimal Approach
# Counting exactly k odd elements directly is inconvenient because even values can create several valid starting positions.

# Instead, count subarrays with at most k odds and subtract those with at most k - 1 odds. A sliding window can count each at-most group efficiently because shrinking from the left reduces or preserves the odd count.

# Algorithm
# A helper function countAtMost is created to count the number of subarrays that contain at most limit odd numbers. If limit is less than 0, 0 is returned because a subarray cannot contain a negative number of odd elements.

# Inside countAtMost, three variables are initialized: left is set to 0 to represent the left boundary of the window, oddCount is set to 0 to store the number of odd numbers in the current window, and count is set to 0 to store valid subarrays.

# The right pointer moves from 0 to n - 1. If nums[right] is odd, oddCount is increased because this odd number is now included in the window.

# If oddCount becomes greater than limit, the window is shrunk from the left. While shrinking, if nums[left] is odd, oddCount is decreased. Then left is moved forward.

# After the window becomes valid, every subarray ending at right and starting from any index between left and right contains at most limit odd numbers. So, right - left + 1 is added to count.


class Solution:

    # Counts subarrays containing at most the given number of odd values.
    def count_at_most(
        self,
        nums: list[int],
        limit: int
    ) -> int:

        # A subarray cannot contain a negative number of odd values.
        if limit < 0:
            return 0

        left = 0
        odd_count = 0
        count = 0

        # Expand the window using each index as the right boundary.
        for right in range(len(nums)):

            # Count the new value when it is odd.
            if nums[right] % 2 != 0:
                odd_count += 1

            # Shrink until the window contains at most limit odd values.
            while odd_count > limit:

                # Remove an odd value from the count when it leaves.
                if nums[left] % 2 != 0:
                    odd_count -= 1

                left += 1

            # Every start from left to right forms a valid subarray.
            count += right - left + 1

        return count

    # Counts subarrays containing exactly k odd numbers.
    def number_of_subarrays(
        self,
        nums: list[int],
        k: int
    ) -> int:
        return (
            self.count_at_most(nums, k)
            - self.count_at_most(nums, k - 1)
        )


if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 3

    solution = Solution()

    print(solution.number_of_subarrays(nums, k))
