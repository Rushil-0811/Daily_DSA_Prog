# Given a binary array nums and an integer goal, return the number of non-empty subarrays with sum equal to goal.

# A subarray is a continuous part of the array.

# Since nums contains only 0s and 1s, the sum of a subarray is simply the number of 1s present inside it.

# Example 1
# Input: nums = [1, 0, 1, 0, 1], goal = 2

# Output: 4

# Explanation: The subarrays with sum 2 are [1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], and [1, 0, 1].

# Brute Force Approach
# Every possible subarray can be checked independently. For each selected range, calculate its sum from scratch and increase the answer whenever the sum equals goal.

# This guarantees that every valid subarray is counted, but overlapping ranges repeatedly calculate the same sums.

# Algorithm
# The size of the array is stored in n. If n is 0, 0 is returned because no non-empty subarray can be formed.

# A variable count is initialized with 0. This stores the number of subarrays whose sum is exactly equal to goal.

# Two loops are used to generate every possible subarray. The first loop chooses the starting index start, and the second loop chooses the ending index end.

# For every subarray from start to end, another loop is used to calculate the sum of all elements in that range.

# If the calculated sum is equal to goal, it means the current subarray is valid, so count is increased by 1.

# After all subarrays are checked, count is returned as the final answer.

class Solution:

    # Counts subarrays whose sum is exactly equal to goal.
    def num_subarrays_with_sum(
        self,
        nums: list[int],
        goal: int
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
                current_sum = 0

                # Calculate the sum of the selected subarray from scratch.
                for i in range(start, end + 1):
                    current_sum += nums[i]

                # Count the subarray when its sum matches the goal.
                if current_sum == goal:
                    count += 1

        return count


if __name__ == "__main__":
    nums = [1, 0, 1, 0, 1]
    goal = 2

    solution = Solution()

    print(solution.num_subarrays_with_sum(nums, goal))

# Complexity Analysis
# Time Complexity: O(N³), where N is the size of the array. There are O(N²) possible subarrays, and calculating the sum of each subarray can take O(N) time.

# Space Complexity: O(1), because no extra data structure is used. Only a few variables are required.

# Better Approach
# Instead of recalculating the sum for every range, fix start and keep a running sum while end moves right.

# Because the array contains only 0s and 1s, the sum never decreases during expansion. Therefore, once it becomes greater than goal, no later ending for that same start can produce the required sum.

# Algorithm
# The size of the array is stored in n. If n is 0, 0 is returned because no subarray can be formed.

# A variable count is initialized with 0 to store the number of subarrays whose sum is exactly equal to goal.

# The array is traversed using start as the starting index of the subarray. For every start, currentSum is initialized with 0 because a new subarray is being built.

# The end pointer moves from start to the end of the array. At every step, nums[end] is added to currentSum.

# If currentSum becomes equal to goal, count is increased because the subarray from start to end has the required sum.

# If currentSum becomes greater than goal, the loop is stopped for this start. This is safe because nums contains only 0s and 1s, so adding more elements cannot reduce the sum. After all starting positions are checked, count is returned.

class Solution:

    # Counts valid subarrays by maintaining a running sum from each start.
    def num_subarrays_with_sum(
        self,
        nums: list[int],
        goal: int
    ) -> int:
        n = len(nums)

        # No non-empty subarray can be formed.
        if n == 0:
            return 0

        count = 0

        # Choose every possible starting index.
        for start in range(n):
            current_sum = 0

            # Extend the subarray while maintaining its running sum.
            for end in range(start, n):
                current_sum += nums[end]

                # Count every range whose sum matches the goal.
                if current_sum == goal:
                    count += 1

                # Further expansion cannot reduce the sum in a binary array.
                if current_sum > goal:
                    break

        return count


if __name__ == "__main__":
    nums = [1, 0, 1, 0, 1]
    goal = 2

    solution = Solution()

    print(solution.num_subarrays_with_sum(nums, goal))

# Complexity Analysis
# Time Complexity: O(N²), where N is the size of the array. For every starting index, the ending index may move toward the right until the sum becomes greater than goal.

# Space Complexity: O(1), because only variables like currentSum and count are used.

# Optimal Approach
# Counting exact-sum windows directly is difficult because zeros can create multiple valid starting positions. Instead, count subarrays with sum at most a limit.

# countAtMost(goal) contains sums up to goal, while countAtMost(goal - 1) contains all smaller sums. Their difference therefore leaves exactly the subarrays whose sum is goal.

# Since every value is non-negative, a sliding window can count each at-most group in linear time.

# Algorithm
# A helper function countAtMost is created to count the number of subarrays whose sum is less than or equal to a given limit. If limit is less than 0, 0 is returned because a binary subarray cannot have a negative sum.

# Inside countAtMost, three variables are initialized: left is set to 0 to represent the left boundary of the window, currentSum is set to 0 to store the sum of the current window, and count is set to 0 to store valid subarrays.

# The right pointer moves from 0 to n - 1. At every step, nums[right] is added to currentSum because it is now included in the window.

# If currentSum becomes greater than limit, the window is shrunk from the left. nums[left] is subtracted from currentSum and left is moved forward until the window sum becomes less than or equal to limit again.

# Once the window is valid, all subarrays ending at right and starting from any index between left and right are valid. So, right - left + 1 is added to count.

# Finally, the answer is calculated as countAtMost(goal) - countAtMost(goal - 1), which gives the number of subarrays with sum exactly equal to goal.

class Solution:

    # Counts subarrays whose sum is at most the given limit.
    def count_at_most(
        self,
        nums: list[int],
        limit: int
    ) -> int:

        # A binary subarray cannot have a negative sum.
        if limit < 0:
            return 0

        left = 0
        current_sum = 0
        count = 0

        # Expand the window using each index as the right boundary.
        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink until the window sum becomes valid again.
            while current_sum > limit:
                current_sum -= nums[left]
                left += 1

            # Every start from left to right forms a valid subarray.
            count += right - left + 1

        return count

    # Counts subarrays whose sum is exactly equal to goal.
    def num_subarrays_with_sum(
        self,
        nums: list[int],
        goal: int
    ) -> int:
        return (
            self.count_at_most(nums, goal)
            - self.count_at_most(nums, goal - 1)
        )


if __name__ == "__main__":
    nums = [1, 0, 1, 0, 1]
    goal = 2

    solution = Solution()

    print(solution.num_subarrays_with_sum(nums, goal))