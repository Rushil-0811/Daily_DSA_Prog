# Problem Statement: Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.
# Input :
#  nums = [4, 9, 2, 5, 1] , k = 10
# Output :
#  2

# Use recursion to explore all combinations of elements that could contribute to the target sum.
# At each step, decide whether to include or exclude the current element.
# If the target becomes exactly zero, a valid subset has been found.
# If the target goes negative or the end of the array is reached without hitting zero, discard that path.
# Sum the results of both choices — inclusion and exclusion — to get the total number of valid subsets.

class Solution:
    def func(self, ind, sum, nums):
        # Base case: if sum is 0, one valid subsequence is found
        if sum == 0:
            return 1
        # Base case: if sum is negative or index exceeds array size
        if sum < 0 or ind == len(nums):
            return 0
        # Recurse by including current number or excluding it from the sum
        return self.func(ind + 1, sum - nums[ind], nums) + self.func(ind + 1, sum, nums)

    def countSubsequenceWithTargetSum(self, nums, target):
        return self.func(0, target, nums)

# Main function to test the solution
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 5
    print(f"Number of subsequences with target sum {target}: {sol.countSubsequenceWithTargetSum(nums, target)}")
