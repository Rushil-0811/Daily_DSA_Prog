# brute force is we just gonna do a linear search
# basically loop and compare with target
# optimal
# In a rotated sorted array, the entire array is no longer fully sorted ,but an important property still holds: in every part of the array you look at, one side will always be sorted. This means either the left portion or the right portion of the array will be in increasing order. That’s the key idea we use to find the target efficiently.
# In normal binary search, we rely on the entire array being sorted to decide whether to go left or right. But in this case, we adapt it slightly we don't require the whole array to be sorted, just identify which part is sorted in the current range. Once we know which part is sorted, we check if the target lies inside that sorted section. If it does, we discard the other half. If not, we discard the sorted half and search the remaining half. No matter how the array was rotated, the sorted structure on at least one side of any middle point always helps us narrow down where to look next. This lets us avoid scanning the whole array like in brute force, and instead bring down the number of checks to logarithmic time.
# Start by looking at the middle element of the array.
# Check if this middle element is the target if yes, return its index immediately.
# Now figure out which half of the array (left side or right side) is sorted.
# If the left part is sorted:
# Check if the target number falls within the range of that sorted part.
# If it does, discard the right half and continue the search in the left part.
# If it doesn’t, discard the left half and search in the right side.
# If the right part is sorted:
# Do the same check if the target is in that sorted part.
# If yes, discard the left side and search in the right.
# If not, discard the right and continue with the left.
# Repeat this process of eliminating half the array until the target is found or the search space is empty.
class Solution:
    # Function to search target in rotated sorted array using binary search
    def search(self, nums, target):
        # Set initial search space
        low = 0
        high = len(nums) - 1

        # Run loop while valid search space exists
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2

            # If target found at mid, return index
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[low] <= nums[mid]:
                # If target lies in left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # Target not found
        return -1

# Driver code
nums = [4,5,6,7,0,1,2]
target = 0

obj = Solution()
result = obj.search(nums, target)

print(result)
