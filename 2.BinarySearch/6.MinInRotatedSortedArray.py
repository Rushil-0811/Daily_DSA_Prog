# brute for most bs problems going to be linear search, assume that when I dont have brute sols written up
# In a rotated sorted array, the smallest element represents the point of rotation. It is the only element that is smaller than its previous element. Since the array is sorted in two segments, we can use binary search to efficiently find this pivot point. By comparing the middle element with the rightmost element in the current search space, we can determine which half of the array contains the minimum element.
# Initialize pointers to the start and end of the array.
# While start is less than end, calculate the middle index.
# If the middle element is greater than the rightmost element, move the start to mid + 1.
# Else, move the end to mid (because mid can be the minimum).
# When the loop ends, start will point to the minimum element.
class Solution:
    # Function to find the minimum element using binary search
    def findMin(self, nums):

        # Initialize low and high pointers
        low, high = 0, len(nums) - 1

        # Binary search loop
        while low < high:

            # Calculate mid index
            mid = low + (high - low) // 2

            # Check which half to discard
            if nums[mid] > nums[high]:

                # Minimum lies in right half
                low = mid + 1

            else:

                # Minimum lies in left half (including mid)
                high = mid

        # Return the minimum element
        return nums[low]

# Input array
nums = [4, 5, 6, 7, 0, 1, 2]

# Create object of Solution
sol = Solution()

# Call function and store result
result = sol.findMin(nums)

# Output the result
print("Minimum element is", result)
