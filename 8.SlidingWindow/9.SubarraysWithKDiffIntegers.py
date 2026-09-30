# Given an integer array nums and an integer k, return the number of good subarrays.

# A good subarray is a continuous subarray that contains exactly k different integers.

# A subarray is a continuous part of the array.

# Example 1
# Input: nums = [1, 2, 1, 2, 3], k = 2

# Output: 7

# Explanation: The good subarrays are [1, 2], [1, 2, 1], [1, 2, 1, 2], [2, 1], [2, 1, 2], [1, 2], and [2, 3].

# Brute Force Approach
# Every possible subarray can be checked independently. For each selected range, use a set to count how many distinct values it contains.

# If the set size equals k, that range is a good subarray. This guarantees that every possible answer is examined, but overlapping subarrays repeatedly process the same elements.

# Algorithm
# The size of the array is stored in n. If n is 0 or k is less than or equal to 0, 0 is returned because no non-empty good subarray can be formed in such cases.

# A helper function is created to count distinct integers inside a subarray from start to end. A set is used inside this helper because a set stores only unique values.

# The helper function traverses the subarray from start to end and inserts each element into the set. After the traversal ends, the size of the set gives the number of distinct integers in that subarray.

# A variable count is initialized with 0. This stores the total number of good subarrays found so far.

# Two loops are used to generate every possible subarray. The first loop chooses the starting index start, and the second loop chooses the ending index end.

# For every subarray from start to end, the helper function is called. If the distinct count is exactly equal to k, count is increased by 1. After all subarrays are checked, count is returned.

class Solution:

    # Counts distinct values
    # inside the selected range.
    def count_distinct(
        self,
        nums: list[int],
        start: int,
        end: int
    ) -> int:
        distinct = set()

        # Scan the selected subarray.
        for i in range(start, end + 1):
            distinct.add(nums[i])

        return len(distinct)

    # Counts subarrays containing
    # exactly k distinct integers.
    def subarrays_with_k_distinct(
        self,
        nums: list[int],
        k: int
    ) -> int:
        n = len(nums)

        # No valid non-empty subarray
        # can exist in these cases.
        if n == 0 or k <= 0:
            return 0

        count = 0

        # Try every possible start.
        for start in range(n):

            # Try every possible end
            # for the current start.
            for end in range(start, n):
                distinct_count = self.count_distinct(
                    nums,
                    start,
                    end
                )

                # Count ranges having
                # exactly k distinct values.
                if distinct_count == k:
                    count += 1

        return count


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 3]
    k = 2

    solution = Solution()

    print(
        solution.subarrays_with_k_distinct(
            nums,
            k
        )
    )

# Complexity Analysis
# Time Complexity: O(N³), where N is the size of the array. There are O(N²) possible subarrays, and counting distinct integers in each subarray can take O(N) time.

# Space Complexity: O(N), because the set used inside the helper function may store distinct integers from the current subarray.

# Better Approach
# Instead of rebuilding the distinct set for every range, fix start and expand end while maintaining a frequency map.

# The map size directly gives the number of distinct integers. Once it becomes greater than k, further expansion from the same start cannot make it valid again because adding elements cannot reduce the distinct count.

# Algorithm
# The size of the array is stored in n. If n is 0 or k is less than or equal to 0, 0 is returned because no good subarray can exist.

# A variable count is initialized with 0. This stores the number of subarrays containing exactly k distinct integers.

# The array is traversed using start as the starting index. For every start, a fresh frequency map is created because a new subarray is being built from that position.

# The end pointer moves from start to the end of the array. Whenever nums[end] is included in the current subarray, its frequency is increased in the map.

# The size of the map tells how many distinct integers are currently present in the subarray. If the map size becomes exactly k, count is increased.

# If the map size becomes greater than k, the loop stops for the current start. This is safe because adding more elements cannot decrease the number of distinct integers. After all starting positions are checked, count is returned.

class Solution:

    # Expands from every start
    # while tracking frequencies.
    def subarrays_with_k_distinct(
        self,
        nums: list[int],
        k: int
    ) -> int:
        n = len(nums)

        # No valid non-empty subarray
        # can exist in these cases.
        if n == 0 or k <= 0:
            return 0

        count = 0

        # Try every possible start.
        for start in range(n):
            frequency = {}

            # Expand the current subarray.
            for end in range(start, n):
                value = nums[end]

                frequency[value] = (
                    frequency.get(value, 0) + 1
                )

                # Count the range when it
                # has exactly k distinct values.
                if len(frequency) == k:
                    count += 1

                # Further expansion cannot
                # reduce the distinct count.
                if len(frequency) > k:
                    break

        return count


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 3]
    k = 2

    solution = Solution()

    print(
        solution.subarrays_with_k_distinct(
            nums,
            k
        )
    )

# Optimal Approach
# Counting exactly k distinct values directly is inconvenient because several starting positions may form valid subarrays for the same ending position.

# Instead, count subarrays with at most k distinct integers and subtract those with at most k - 1 distinct integers. Their difference leaves exactly the subarrays containing k distinct values.

# A sliding window efficiently finds the valid left boundary for each right, while a frequency map ensures a value is removed from the distinct count only after its last occurrence leaves the window.

# Algorithm
# A helper function countAtMost is created to count subarrays with at most limit distinct integers. If limit is less than or equal to 0, 0 is returned because no non-empty useful subarray can have at most 0 distinct integers.

# Inside the helper function, a frequency map is used to store how many times each integer appears in the current window. This is needed because an integer should be removed from the distinct count only when its frequency becomes 0.

# Two variables are initialized: left is set to 0 to represent the left boundary of the window, and count is set to 0 to store the number of valid subarrays.

# The right pointer moves from 0 to n - 1. At every step, nums[right] is added to the frequency map because it becomes part of the current window.

# If the size of the frequency map becomes greater than limit, the window is shrunk from the left. While shrinking, the frequency of nums[left] is decreased. If its frequency becomes 0, that integer is removed from the map. Then left is moved one step forward.

# Once the window contains at most limit distinct integers, every subarray ending at right and starting from any index between left and right is valid. Therefore, right - left + 1 is added to count. Finally, the answer is returned as countAtMost(k) - countAtMost(k - 1).

class Solution:

    # Counts subarrays having
    # at most limit distinct values.
    def count_at_most(
        self,
        nums: list[int],
        limit: int
    ) -> int:
        # No non-empty subarray
        # can satisfy this limit.
        if limit <= 0:
            return 0

        frequency = {}

        left = 0
        count = 0

        # Expand the window with right.
        for right in range(len(nums)):
            value = nums[right]

            frequency[value] = (
                frequency.get(value, 0) + 1
            )

            # Shrink until the window
            # has at most limit values.
            while len(frequency) > limit:
                left_value = nums[left]
                frequency[left_value] -= 1

                # Remove the value only
                # after its last copy leaves.
                if frequency[left_value] == 0:
                    del frequency[left_value]

                left += 1

            # Every start from left to right
            # forms a valid subarray.
            count += right - left + 1

        return count

    # Counts subarrays containing
    # exactly k distinct integers.
    def subarrays_with_k_distinct(
        self,
        nums: list[int],
        k: int
    ) -> int:
        # Exactly k distinct values
        # require a positive k.
        if k <= 0:
            return 0

        return (
            self.count_at_most(nums, k)
            - self.count_at_most(nums, k - 1)
        )


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 3]
    k = 2

    solution = Solution()

    print(
        solution.subarrays_with_k_distinct(
            nums,
            k
        )
    )