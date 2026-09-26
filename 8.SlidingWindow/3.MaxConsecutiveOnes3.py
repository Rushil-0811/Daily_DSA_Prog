# Given a binary array nums and an integer k, return the maximum number of consecutive 1s in the array if at most k zeroes can be flipped.

# Flipping a zero means changing it from 0 to 1.

# Example 1
# Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2

# Output: 6

# Explanation: We can flip two zeros in the subarray [0, 0, 1, 1, 1, 1]. After flipping them, we get 6 consecutive ones.

# Brute Force Approach
# Every contiguous subarray represents a possible group of consecutive 1s after flipping the zeroes present inside the range. A subarray remains valid as long as the zero count does not exceed k.

# Starting from every index and expanding toward the right examines every possible candidate. Expansion from one start can stop immediately after the zero count exceeds k because adding more elements cannot reduce the number of zeroes already present.

# Algorithm
# Store the array size in n and initialize maxLength with 0 for tracking the longest valid subarray found so far.

# Select every index start as a possible beginning and initialize zeroCount with 0 for the new subarray.

# Move end from start toward the final index, increasing zeroCount whenever nums[end] equals 0.

# Stop the current expansion when zeroCount > k, because every longer subarray from the same start will still require more than k flips.

# Update maxLength with end - start + 1 whenever zeroCount remains at most k.

# Return maxLength after expansion from every starting position has finished.

class Solution:

    # Finds the longest valid subarray by expanding from every start.
    def longest_ones(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_length = 0

        # Try every index as the beginning of the subarray.
        for start in range(n):
            zero_count = 0

            # Expand until the current range requires too many flips.
            for end in range(start, n):

                # Count every zero that would need to be flipped.
                if nums[end] == 0:
                    zero_count += 1

                # No longer range from this start can become valid again.
                if zero_count > k:
                    break

                max_length = max(
                    max_length,
                    end - start + 1
                )

        return max_length


if __name__ == "__main__":
    nums = [
        1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0
    ]
    k = 2

    solution = Solution()

    print(solution.longest_ones(nums, k))

# Complexity Analysis
# Time Complexity: O(N²), where N represents the array size. Expansion from every starting index may traverse most of the remaining array.

# Space Complexity: O(1), because only index variables, zeroCount, and maxLength require auxiliary storage.

# Better Approach
# The Brute Force Approach counts zeroes repeatedly across overlapping subarrays. A prefix-zero array stores the total number of zeroes appearing before every position, allowing any subarray zero count to be calculated through subtraction.

# For a fixed start, the zero count never decreases as end moves toward the right. Such monotonic behaviour allows binary search for the farthest end containing at most k zeroes. The farthest valid end produces the longest valid subarray for the selected start.

# Algorithm
# Build prefixZero with size n + 1, where prefixZero[i] stores the number of zeroes present before index i.

# Traverse nums and set prefixZero[i + 1] = prefixZero[i] + 1 when nums[i] is 0; otherwise, keep prefixZero[i + 1] = prefixZero[i]. This stores the total number of zeroes seen before each position.

# Select every start index and binary-search the range from start to n - 1 for the farthest valid end.

# Calculate the zero count from start through mid as prefixZero[mid + 1] - prefixZero[start].

# Move the search toward the right when the zero count is at most k; otherwise, move toward the left because the selected range contains too many zeroes.

# Update maxLength using the farthest valid end for every start, then return maxLength.

class Solution:

    # Finds the longest valid range using prefix counts and binary search.
    def longest_ones(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_zero = [0] * (n + 1)

        # Store the number of zeroes before every position.
        for i in range(n):
            prefix_zero[i + 1] = (
                prefix_zero[i] + (1 if nums[i] == 0 else 0)
            )

        max_length = 0

        # Try every index as the beginning of the subarray.
        for start in range(n):
            low = start
            high = n - 1
            farthest = start - 1

            # Find the farthest end containing at most k zeroes.
            while low <= high:
                mid = low + (high - low) // 2

                zero_count = (
                    prefix_zero[mid + 1]
                    - prefix_zero[start]
                )

                # A valid midpoint allows searching farther right.
                if zero_count <= k:
                    farthest = mid
                    low = mid + 1

                # Too many zeroes require a shorter range.
                else:
                    high = mid - 1

            # Update only when a valid ending exists.
            if farthest >= start:
                max_length = max(
                    max_length,
                    farthest - start + 1
                )

        return max_length


if __name__ == "__main__":
    nums = [
        1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0
    ]
    k = 2

    solution = Solution()

    print(solution.longest_ones(nums, k))

# Complexity Analysis
# Time Complexity: O(N log N), where N represents the array size. Prefix construction requires O(N) time, while binary search for every starting index requires O(log N) time.

# Space Complexity: O(N), because prefixZero stores N + 1 zero counts.

# Optimal Approach
# A sliding window can represent the current subarray capable of becoming all 1s. The window remains valid while the number of zeroes stays at most k.

# Pointer right expands the window and explores longer candidates. After the zero count exceeds k, pointer left removes elements until the window becomes valid again. Every pointer moves only forward, eliminating repeated examination of the same subarrays.

# Algorithm
# Initialize left, zeroCount, and maxLength with 0; left marks the current window beginning, while zeroCount records required flips.

# Move right across nums and increase zeroCount whenever nums[right] equals 0.

# If zeroCount becomes greater than k, move left forward until the window becomes valid again. Whenever nums[left] is 0, decrease zeroCount because that zero is leaving the window.

# Once zeroCount <= k, the current range can be converted entirely into 1s, so update maxLength with right - left + 1.

# After restoring validity, calculate the current length as right - left + 1 and update maxLength.

# Return maxLength after right reaches the final array position.

class Solution:

    # Finds the longest window containing at most k zeroes.
    def longest_ones(self, nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        # Expand the right boundary across the complete array.
        for right in range(len(nums)):

            # Count a zero when it enters the active window.
            if nums[right] == 0:
                zero_count += 1

            # Shrink until the window requires at most k flips.
            while zero_count > k:

                # Remove a zero from the count when it leaves the window.
                if nums[left] == 0:
                    zero_count -= 1

                left += 1

            max_length = max(
                max_length,
                right - left + 1
            )

        return max_length


if __name__ == "__main__":
    nums = [
        1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0
    ]
    k = 2

    solution = Solution()

    print(solution.longest_ones(nums, k))