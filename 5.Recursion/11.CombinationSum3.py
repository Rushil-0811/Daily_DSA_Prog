# Problem Statement: Determine all possible set of k numbers that can be added together to equal n while meeting the following requirements:
# 1. There is only use of numerals 1 through 9.
# 2. A single use is made of each number.
# Return list of every feasible combination that is allowed. The combinations can be returned in any order, but the list cannot have the same combination twice.
# Example 1:
# Input:
#  k = 3, n = 7
# Output:
#  [[1, 2, 4]]
# Explanation:

# 1 + 2 + 4 = 7
# There are no other valid combinations.

# Use backtracking to explore all possible number combinations that sum up to a target.
# Track the current combination and remaining target as you build solutions incrementally.
# If a valid combination meets both the target sum and required size, store it in the results.
# Prune the path early if the sum goes negative or the combination exceeds the allowed size.
# Explore the search space by trying each number, then undoing the choice to backtrack and try alternatives.

class Solution:
    def func(self, sum, last, nums, k, ans):
        # If the sum is zero and the number of elements is k
        if sum == 0 and len(nums) == k:
            # Add the current combination to the answer
            ans.append(list(nums))
            return
        # If the sum is less than or equal to zero or the number of elements exceeds k
        if sum <= 0 or len(nums) > k:
            return

        # Iterate from the last number to 9
        for i in range(last, 10):
            # If the current number is less than or equal to the sum
            if i <= sum:
                # Add the number to the current combination
                nums.append(i)
                # Recursive call with updated sum and next number
                self.func(sum - i, i + 1, nums, k, ans)
                # Remove the last number to backtrack
                nums.pop()
            else:
                # If the number is greater than the sum, break the loop
                break

    def combinationSum3(self, k, n):
        ans = []
        nums = []
        # Call the recursive function with initial parameters
        self.func(n, 1, nums, k, ans)
        return ans

# Example usage
sol = Solution()
k = 3  # Number of elements in the combination
n = 7  # Target sum
result = sol.combinationSum3(k, n)

# Print the result
for combination in result:
    print(combination)
