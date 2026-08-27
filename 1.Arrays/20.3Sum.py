#  Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.
# nums = [-1,0,1,2,-1,-4]
# Output:
#  [[-1,-1,2],[-1,0,1]]
# brute
# check every group of 3 using 3 nums and check their sum
# Use a set because we need only unique triplets.
# Run the first loop from the start to the end of the array.
# Inside it, run the second loop from the next position to the end.
# Then run the third loop from the next position after the second loop to the end.
# For every three numbers, check if their sum equals 0. If yes, sort the triplet and add it to the set.
# At the end, return all triplets from the set.
# Class to solve 3-sum problem
class Solution:
    # Function to find triplets with sum zero
    def threeSum(self, arr, n):
        # Store unique triplets
        st = set()

        # First loop for first element
        for i in range(n):
            # Second loop for second element
            for j in range(i + 1, n):
                # Third loop for third element
                for k in range(j + 1, n):
                    # If triplet sum is zero
                    if arr[i] + arr[j] + arr[k] == 0:
                        # Store sorted triplet to avoid duplicates
                        triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                        st.add(triplet)

        # Convert set to list of lists
        return [list(triplet) for triplet in st]

# Driver code
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    obj = Solution()
    res = obj.threeSum(arr, n)
    for triplet in res:
        print(triplet)
# Time Complexity: O(N3 * log(no. of unique triplets)),
# Space Complexity: O(2 * no. of the unique triplets)

# better
# Earlier, we used three loops to find triplets that sum to zero. But now, we aim to do the same using just two loops. To do this, we will calculate the third number needed to complete the triplet instead of looping to find it.

# The idea is simple: if we already have two numbers, we can figure out what the third number should be to make the sum zero. Instead of checking all possible third numbers, we just check if this required number is already present using a set, which helps us search quickly.

# But we have to be careful. We cannot put all numbers in the set from the beginning. If we do that, we might accidentally use the same number again from the same position, which is not allowed. That’s why we only put numbers into the set after using them in the second loop.

# Start by creating a set to store the final unique triplets.
# Use the first loop to go through each number one by one.
# Before starting the second loop, create another set to help find the third number.
# Now run the second loop, picking another number after the current one from the first loop.
# Check what number is needed to complete the triplet so that the total is zero.
# If this number is already present in the set, it means we found a valid triplet. Sort it and add it to the answer set.
# After checking, add the current number to the set so it can be used in future checks.
# Finally, after both loops finish, return all the triplets collected in the set.
# Class to solve 3-sum problem
class Solution:
    # Function to find triplets with sum zero
    def threeSum(self, arr, n):
        # Store unique triplets
        ans = set()

        # First loop for first element
        for i in range(n):
            # Set to store elements seen in this iteration
            hashset = set()

            # Second loop for second element
            for j in range(i + 1, n):
                # Calculate third element needed
                third = -(arr[i] + arr[j])

                # If third already in set, we found a triplet
                if third in hashset:
                    triplet = tuple(sorted([arr[i], arr[j], third]))
                    ans.add(triplet)

                # Add current element to set
                hashset.add(arr[j])

        # Convert set to list of lists
        return [list(triplet) for triplet in ans]

# Driver code
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    obj = Solution()
    res = obj.threeSum(arr, n)
    for triplet in res:
        print(triplet)

# Time Complexity: O(N2 * log(no. of unique triplets)),
# Space Complexity: O(2 * no. of the unique triplets) + O(N)

# optimal
# This is an improved version of the previous solution. We remove the extra set (used for unique triplets) and HashSet (used for quick searching).

# By sorting the array first, we can:

# Easily skip repeated numbers by checking if the current number is the same as the previous one.
# Ensure all triplets are unique without storing them in a set.
# Instead of using a HashSet to find triplets, we use the two-pointer method:

# One pointer moves forward from the left, the other backward from the right.
# We adjust their positions depending on whether the total is greater than, less than, or equal to the target.
# Sort the array first.
# Fix the first number using a loop from the beginning to the end of the array.
# Skip the number if it is the same as the previous one (to avoid duplicates).
# Use two pointers:
# Left: starts right after the fixed number.
# Right: starts from the last element of the array.
# While the left pointer is before the right pointer:
# If the total is greater than 0 → move the right pointer one step left.
# If the total is less than 0 → move the left pointer one step right.
# If the total equals 0 → store the triplet, then move both pointers while skipping duplicates.
# Class to solve 3-sum problem
class Solution:
    # Function to find triplets with sum zero
    def threeSum(self, arr, n):
        # Sort the array
        arr.sort()
        # Store final result
        ans = []

        # First loop for first element
        for i in range(n):
            # Skip duplicates for first element
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # Two pointers
            left, right = i + 1, n - 1

            # Find pairs for current arr[i]
            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == 0:
                    ans.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return ans

# Driver code
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    obj = Solution()
    res = obj.threeSum(arr, n)
    for triplet in res:
        print(triplet)
