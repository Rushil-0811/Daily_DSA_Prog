# brute - find all possible permutations adn look for next
from itertools import permutations

class Solution:
    # Function to find the next permutation
    def nextPermutation(self, nums):
        # Generate all unique permutations
        perms = sorted(set(permutations(nums)))

        # Convert list to tuple for comparison
        current = tuple(nums)

        # Traverse the list
        for i in range(len(perms)):
            if perms[i] == current:
                # If last permutation, return first
                if i == len(perms) - 1:
                    return list(perms[0])
                # Else return next
                return list(perms[i + 1])

        return nums

# Driver code
sol = Solution()
nums = [1, 2, 3]
result = sol.nextPermutation(nums)
print(" ".join(map(str, result)))

# optimal
# To find this next permutation with minimal change, we need to find a digit that can be increased slightly to make the number bigger and then rearrange the remaining part to be the smallest possible.
# Traverse from the end and find the first index where the current digit is smaller than the next one (this is the "breaking point").
# Then again traverse from the end to find the first digit greater than the breaking point digit and swap them.
# Finally, reverse the part of the array to the right of the breaking point to get the smallest next permutation.
# If no such breaking point exists (entire array is descending), just reverse the whole array.
# Solution class
class Solution:
    # Function to find next permutation
    def nextPermutation(self, nums):
        # Set index
        index = -1

        # Find decreasing point
        for i in range(len(nums) - 2, -1, -1):
            # If smaller found
            if nums[i] < nums[i + 1]:
                index = i
                break

        # If no such index
        if index == -1:
            # Reverse whole list
            nums.reverse()
            return

        # Find just greater element
        for i in range(len(nums) - 1, index, -1):
            if nums[i] > nums[index]:
                # Swap them
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Reverse part after index
        nums[index + 1:] = reversed(nums[index + 1:])

# Main driver
def main():
    # Input list
    nums = [1, 2, 3]

    # Create object
    sol = Solution()

    # Call function
    sol.nextPermutation(nums)

    # Print result
    print(" ".join(map(str, nums)))

# Run main
main()
