# Problem Statement: Given an integer array nums, which can have duplicate entries, provide the power set. Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.
# Input: array[] = [1,2,2]
# Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]
# Explanation: We can have subsets ranging from  length 0 to 3. which are listed above. Also the subset [1,2] appears twice but is printed only once as we require only unique subsets.

# To find all unique subsets from an array like [1, 2, 2], the most direct way is to first generate every possible combination of elements (subsets). We can do this with a "pick" or "don't pick" choice for each element. This process, however, will create duplicates, like generating [1, 2] twice. To solve this, we can store all the generated subsets in a special container, a Set, which automatically discards any duplicates. After generating all possibilities, we just copy the unique subsets from the Set to a list for the final answer.
# Define a recursive function to generate subsets.
# The base case for the recursion is when all elements of the input array have been considered.
# When the base case is reached, the currently formed subset is complete.
# Insert this complete subset into a Set data structure to automatically handle uniqueness.
# For each element in the array, make two recursive calls: one where the element is included in the subset, and another where it is not included.
# The main function will initialize a Set to store the unique results.
# It will then start the recursion from the first element.
# Finally, it will convert the Set of unique subsets into a list and return it.

from typing import List

class Solution:
    # Recursive helper function to generate subsets
    def findSubsets(self, ind: int, nums: List[int], ds: List[int], ans_set: set):
        # Base case: if all elements are considered, add the current subset to the set
        if ind == len(nums):
            # Tuples are hashable and can be added to a set
            ans_set.add(tuple(ds))
            return

        # Choice 1: Include the current element
        ds.append(nums[ind])
        self.findSubsets(ind + 1, nums, ds, ans_set)
        # Backtrack to explore the other choice
        ds.pop()

        # Choice 2: Do not include the current element
        self.findSubsets(ind + 1, nums, ds, ans_set)

    # Main function to find all unique subsets
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans_set = set()
        ds = []
        # Sort the input array
        nums.sort()
        
        self.findSubsets(0, nums, ds, ans_set)
        
        # Convert the set of tuples back to a list of lists
        return [list(subset) for subset in ans_set]

# Driver code to test the solution
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 2]
    ans = sol.subsetsWithDup(nums)
    print(ans)

# optimal
# Instead of generating all subsets and then removing duplicates, we can avoid creating duplicates in the first place. This is done by sorting the input array first so that all duplicate numbers are adjacent. While generating subsets through backtracking, if we encounter a number that is the same as the previous one and it’s not the first in the current recursive call, we skip it. This pruning step ensures we only generate unique subsets without extra storage for duplicate removal.

# Sorting is essential here because without sorting, duplicates would be scattered and hard to skip correctly. This method is efficient and avoids unnecessary subset generation, making it better in both runtime and memory usage compared to the brute force approach.
# Sort the input array so that duplicates are adjacent.
# Initialize a list to store the current subset and a list of lists to store all unique subsets.
# Use a recursive backtracking function that:
# Adds the current subset to the list of results.
# Iterates from the current index to the end of the array.
# If the current element is the same as the previous one and not at the starting index of this recursion, skip it.
# Include the current element in the subset and recurse for the next index.
# Backtrack by removing the last added element.
# Return the list of all unique subsets.

class Solution:
    # Function to generate all unique subsets
    def backtrack(self, start, nums, current, result):
        # Add a copy of current subset
        result.append(list(current))

        # Iterate from 'start' index
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue

            # Include nums[i]
            current.append(nums[i])

            # Recurse
            self.backtrack(i + 1, nums, current, result)

            # Backtrack
            current.pop()

    def subsetsWithDup(self, nums):
        nums.sort()  # Sort to handle duplicates
        result = []
        self.backtrack(0, nums, [], result)
        return result


# Driver code
if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    for subset in ans:
        print(subset, end=" ")
    print()
