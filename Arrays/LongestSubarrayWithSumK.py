# brute u gonna use two loops

class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums) 
        maxLength = 0

        # starting index
        for startIndex in range(n):
            # ending index
            for endIndex in range(startIndex, n):
                # add all the elements of 
                # subarray = nums[startIndex...endIndex]
                currentSum = 0
                for i in range(startIndex, endIndex + 1):
                    currentSum += nums[i]

                if currentSum == k:
                    maxLength = max(maxLength, endIndex - startIndex + 1)

        return maxLength

if __name__ == "__main__":
    nums = [-1, 1, 1]
    k = 1

    # Create an instance of the Solution class
    solution = Solution()
    # Function call to get the result
    length = solution.longestSubarray(nums, k)
    
    print("The length of the longest subarray is:", length)

# optimal is a two pointer approach, rules for arrays apply
# two pointer will probably your best option
class Solution:
    # Function to find the length of longest subarray having sum k
    def longestSubarray(self, nums, k):
        n = len(nums)
        
        # To store the maximum length of the subarray
        maxLen = 0
        
        # Pointers to mark the start and end of window
        left = 0
        right = 0
        
        # To store the sum of elements in the window
        sum = nums[0]
        
        # Traverse all the elements
        while right < n:
            
            # If the sum exceeds K, shrink the window
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1
            
            # Store the maximum length
            if sum == k:
                maxLen = max(maxLen, right - left + 1)
            
            right += 1
            if right < n:
                sum += nums[right]
        
        return maxLen


nums = [10, 5, 2, 7, 1, 9]
k = 15

# Creating an object of Solution class
sol = Solution()

# Function call to find the length
# of longest subarray having sum k
ans = sol.longestSubarray(nums, k)

print(f"The length of longest subarray having sum k is: {ans}")
