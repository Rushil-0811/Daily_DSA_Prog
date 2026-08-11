# Solution class containing removeDuplicates method
# brute force approach we using a set
class Solution:
    # Removes duplicates using set and returns count of unique elements
    def removeDuplicates(self, nums):
        # Set to store seen unique elements
        seen = set()

        # Position to overwrite next unique element
        index = 0

        # Iterate over each number in nums
        for num in nums:
            # If num is not in seen, it is unique
            if num not in seen:
                # Add num to set
                seen.add(num)

                # Overwrite nums[index] with this num
                nums[index] = num

                # Move index forward
                index += 1

        # Return number of unique elements
        return index

# added this question cause we using set for the first time


# Driver code
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k = sol.removeDuplicates(nums)

print("k =", k)
print("Array after removing duplicates:", nums[:k])

# Optimal method
# Class to hold the solution logic
class Solution:
    # Function to remove duplicates from sorted array in-place
    def removeDuplicates(self, nums):
        # If list is empty, return 0
        if not nums:
            return 0

        # Pointer for last unique element
        i = 0

        # Traverse list starting from second element
        for j in range(1, len(nums)):
            # If current element is different from last unique one
            if nums[j] != nums[i]:
                # Move pointer forward
                i += 1
                # Place the unique element in next position
                nums[i] = nums[j]

        # i is last index of unique element, count = i + 1
        return i + 1


# Example usage
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k = sol.removeDuplicates(nums)
print("Unique count =", k)
print("Array after removing duplicates:", nums[:k])
