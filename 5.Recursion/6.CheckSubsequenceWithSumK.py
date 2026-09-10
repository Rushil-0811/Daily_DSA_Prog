# Problem Statement: Given an array nums and an integer k. Return true if there exist subsequences such that the sum of all elements in subsequences is equal to k else false.
# Example 1:
# Input :
#  nums = [1, 2, 3, 4, 5] , k = 8
# Output :
#  Yes
# Explanation :
#  The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.

# Treat the problem as a decision tree where each item has two choices: include it or skip it.
# Recursively apply this decision process to the remaining items while updating the remaining target amount.
# If the target becomes zero, a valid combination has been found.
# If the target becomes negative or all items are exhausted, that path is invalid.
# Explore all possible combinations to determine if any subset matches the exact target.

class Solution:
    # This method recursively checks for the subsequence with the given sum
    def solve(self, i, n, arr, k):
        # Base case: if the sum k is 0, a subsequence is found
        if k == 0:
            return True
        # Base case: if k is negative, no valid subsequence can be found
        if k < 0:
            return False
        # Base case: if all elements are processed, check if k is 0
        if i == n:
            return k == 0
        
        # Recursive call: include the current element in the subsequence
        # or exclude the current element from the subsequence
        return self.solve(i + 1, n, arr, k - arr[i]) or self.solve(i + 1, n, arr, k)

    # This method initiates the recursive process
    def checkSubsequenceSum(self, nums, target):
        n = len(nums) # Get the length of the input array
        return self.solve(0, n, nums, target) # Start the recursive process

# Main function to test the solution
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    target = 5
    print(sol.checkSubsequenceSum(nums, target)) # Expected output: True
