# similar to 3 sum only, 3 loops will be used in optimal tho
# brute
# Create a set to keep only unique groups of four numbers.
# Use the first loop from the start of the array to the end to choose the first number.
# Inside it, run a second loop starting from the next position to choose the second number.
# Then, run a third loop starting from the next position after the second number to choose the third number.
# Finally, run a fourth loop starting from the next position after the third number to choose the fourth number.
# Check if the total of these four numbers equals the target value.
# If yes, arrange the four numbers in order and add them to the set.
# Once all loops are done, return the set as a list of unique groups of four numbers.
class Solution:
    # Function to find quadruplets with sum = target
    def fourSum(self, arr, target):
        # Get size of array
        n = len(arr)
        # Use set to store unique quadruplets
        st = set()

        # First loop - pick first element
        for i in range(n):
            # Second loop - pick second element
            for j in range(i + 1, n):
                # Third loop - pick third element
                for k in range(j + 1, n):
                    # Fourth loop - pick fourth element
                    for l in range(k + 1, n):
                        # If sum equals target
                        if arr[i] + arr[j] + arr[k] + arr[l] == target:
                            # Store sorted quadruplet as tuple
                            temp = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                            st.add(temp)

        # Convert set to list of lists
        return [list(quad) for quad in st]


# Driver code
arr = [1, 0, -1, 0, -2, 2]
target = 0

obj = Solution()
ans = obj.fourSum(arr, target)
print(ans)

# better
# Create a set to keep only unique groups of four numbers.
# Run the first loop from the start to the end of the array to pick the first number.
# Inside it, run the second loop from the next position to pick the second number.
# Before starting the third loop, make a HashSet to keep track of numbers between the second and third positions.
# Run the third loop from the next position after the second number to the end of the array to pick the third number.
# Find the fourth number by subtracting the total of the first three numbers from the target value.
# If this fourth number is already in the HashSet, arrange all four numbers in order and add them to the set.
# Add the current third number to the HashSet (only numbers between the second and third loops are stored).
# After all loops finish, return the set as a list of unique groups of four numbers.
class Solution:
    # Function to find all unique quadruplets
    def fourSum(self, arr, target):
        n = len(arr)
        st = set()  # To keep unique quadruplets

        # First loop - pick first number
        for i in range(n):
            # Second loop - pick second number
            for j in range(i + 1, n):
                seen = set()  # Store numbers between j and k

                # Third loop - pick third number
                for k in range(j + 1, n):
                    # Find required fourth number
                    required = target - arr[i] - arr[j] - arr[k]

                    # If found in seen → valid quadruplet
                    if required in seen:
                        temp = tuple(sorted([arr[i], arr[j], arr[k], required]))
                        st.add(temp)

                    # Add current number to seen
                    seen.add(arr[k])

        # Convert set to list of lists
        return [list(quad) for quad in st]


# Driver code
arr = [1, 0, -1, 0, -2, 2]
target = 0

obj = Solution()
ans = obj.fourSum(arr, target)
print(ans)

# optimal
# Sort the array first.
# Use the first loop to pick the first number. Skip it if it is the same as the previous one to avoid duplicates.
# Inside it, use the second loop to pick the second number. Also skip it if it repeats the previous one.
# Set two pointers: one just after the second number (left pointer) and one at the end of the array (right pointer).
# While the left pointer is before the right pointer, calculate the total of the four chosen numbers.
# If the total equals the target, save the quadruplet, then move both pointers while skipping duplicate numbers.
# If the total is less than the target, move the left pointer one step forward to increase the total.
# If the total is greater than the target, move the right pointer one step backward to reduce the total.
# After all loops finish, return the list of unique groups of four numbers.
class Solution:
    # Function to find all unique quadruplets
    def fourSum(self, arr, target):
        n = len(arr)
        arr.sort()
        ans = []

        # Step 1: First loop for first number
        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # Step 2: Second loop for second number
            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                # Step 3: Two pointers
                left, right = j + 1, n - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]

                    if total == target:
                        ans.append([arr[i], arr[j], arr[left], arr[right]])

                        while left < right and arr[left] == arr[left + 1]:
                            left += 1
                        while left < right and arr[right] == arr[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return ans


# Driver code
arr = [1, 0, -1, 0, -2, 2]
target = 0

obj = Solution()
print(obj.fourSum(arr, target))
