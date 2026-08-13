# brute we keep track of 0s,1s,2s, we finally overwrite the array with 0 1 and 2 based on the frequency
class Solution:
    # Function to sort the array containing only 0s, 1s and 2s
    def sortZeroOneTwo(self, nums):
        # Initialize count variables for 0s, 1s, and 2s
        count0 = count1 = count2 = 0

        # Count the frequency of 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Overwrite the array with sorted values
        index = 0

        # Fill with 0s
        for _ in range(count0):
            nums[index] = 0
            index += 1

        # Fill with 1s
        for _ in range(count1):
            nums[index] = 1
            index += 1

        # Fill with 2s
        for _ in range(count2):
            nums[index] = 2
            index += 1

# Driver code
nums = [1, 0, 2, 1, 0]
obj = Solution()
obj.sortZeroOneTwo(nums)
print(nums)

# better
# kinda similar to brute only, its the same complexity so it dont matter

# optimal 
# dutch national flag algorithm
# We divide the array into three partitions using three pointers – low, mid, and high.
# From 0 to low-1, we’ll keep only 0s
# From low to mid-1, only 1s
# From high+1 to n-1, only 2
# The range from mid to high is the unsorted zone we’re scanning and fixing. At each step:
# If arr[mid] == 0, it belongs to the left section → swap with low, move both low and mid.
# If arr[mid] == 1, it’s already in the middle section → just move mid.
# If arr[mid] == 2, it belongs to the right section → swap with high, only move high.
# When you swap with high, you don’t move mid because the incoming value might still be 0 or 2 which needs processing.This ensures we sort the array in one single pass without using extra space.
# Start with three pointers at the beginning, middle, and end of the array.
# Iterate while the middle pointer is less than or equal to the end pointer.
# If the current element belongs to the front section:
# Swap it with the element at the front boundary.
# Move both front and middle boundaries forward.
# If the current element belongs to the middle section:
# Move the middle boundary forward.
# If the current element belongs to the end section:
# Swap it with the element at the end boundary.
# Move the end boundary backward.
# Repeat until all elements are in their correct zones.
class Solution:
    # Function to sort list containing 0s, 1s, and 2s using Dutch National Flag Algorithm
    def sortZeroOneTwo(self, nums):
        # Initialize three pointers: low and mid at 0, high at end
        low, mid, high = 0, 0, len(nums) - 1

        # Traverse until mid crosses high
        while mid <= high:
            # If element is 0, swap with low, move both low and mid forward
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            # If element is 1, just move mid forward
            elif nums[mid] == 1:
                mid += 1
            # If element is 2, swap with high, move only high backward
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Driver code
nums = [2, 0, 2, 1, 1, 0]
obj = Solution()
obj.sortZeroOneTwo(nums)
print(nums)
