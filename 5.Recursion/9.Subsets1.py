# Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.
# Input: N = 3, arr[] = {5,2,1}
# Output: 0,1,2,3,5,6,7,8
# Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8

# We can solve this more cleanly using recursion without generating all bitmasks. Start from index 0, maintain a running sum, and at each index, make two recursive calls—one including the current element and one excluding it. When we reach the end of the array, store the current sum in our result list. This avoids explicitly storing subsets, reduces unnecessary operations, and still generates all sums in O(2^N) time. Sorting at the end gives the required increasing order.
# Initialize an empty list to store sums
# Create a recursive function taking index and current sum as parameters
# If index equals N, push the current sum into the list and return
# Recursively call the function including the current element (sum + arr[index])
# Recursively call the function excluding the current element (sum remains the same)
# Call the function starting from index 0 and sum 0
# Sort the result list and print it

class Solution:
    # Recursive helper function to find subset sums
    def findSums(self, index, currentSum, arr, sums):
        if index == len(arr):
            sums.append(currentSum)
            return
        # Include current element
        self.findSums(index + 1, currentSum + arr[index], arr, sums)
        # Exclude current element
        self.findSums(index + 1, currentSum, arr, sums)

    def subsetSums(self, arr):
        sums = []
        self.findSums(0, 0, arr, sums)
        sums.sort()
        return sums

# Driver code
if __name__ == "__main__":
    sol = Solution()
    arr = [5, 2, 1]
    result = sol.subsetSums(arr)
    print(*result)
