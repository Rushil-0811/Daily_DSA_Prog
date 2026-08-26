# Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.

# Input :mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], target = 8
# Output :True.
# Explanation :The target = 8 exists in the 'mat' at index (1, 3).

# brute 
# The extremely naive approach is to get the answer by checking all the elements of the given matrix. So, we will traverse the matrix and check every element if it is equal to the given ‘target’.
# We will use a loop(say i) to select a particular row at a time.
# Next, for every row, we will use another loop(say j) to traverse each column.
# Inside the loops, we will check if the element i.e. matrix[i][j] is equal to the ‘target’. If we find any matching element, we will return true.
# Otherwise, after completing the traversal, we will return false.

class Solution:
    # Function to search for a target value in the matrix
    def searchMatrix(self, matrix, target):
        # Get number of rows in the matrix
        n = len(matrix)

        # Get number of columns in the matrix
        m = len(matrix[0])

        # Traverse each row
        for i in range(n):
            # Traverse each column in the current row
            for j in range(m):
                # Check if the current element matches the target
                if matrix[i][j] == target:
                    return True

        # Return false if the target is not found
        return False

# Driver code
if __name__ == "__main__":
    # Define a 2D matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # Create an object of the Solution class
    obj = Solution()

    # Call the searchMatrix function and print the result
    if obj.searchMatrix(matrix, 8):
        print("true")
    else:
        print("false")

# Time Complexity: O(n × m), We are traversing the entire matrix with `n` rows and `m` columns. In the worst case, we may end up visiting every cell once if the target is not present. So, the total number of operations is proportional to the number of elements in the matrix.

# Space Complexity: O(1),We are not using any additional space. The algorithm uses a constant amount of extra memory regardless of the size of the matrix just loop variables and the target. Therefore, the space complexity is constant.

# better
# We are going to use the Binary Search algorithm to optimize the approach. The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# The question specifies that each row in the given matrix is sorted. Therefore, to determine if the target is present in a specific row, we don't need to search column by column. Instead, we can efficiently use the binary search algorithm.

# To make the time complexity even better, we won't use binary search on every row. We'll focus only on the particular row where the target might be located.

# How to check if a specific row is containing the target:
# If the target lies between the first and last element of the row, i (i.e. matrix[i][0] <= target && target <= matrix[i][m-1]), we can conclude that the target might be present in that specific row.

# Once we locate the potentially relevant row containing the 'target', we need to confirm its presence. To accomplish this, we will utilize the Binary search algorithm, effectively reducing the time complexity.
# We will use a loop(say i) to select a particular row at a time.
# Next, for every row, i, we will check if it contains the target.
# If matrix[i][0] <= target && target <= matrix[i][m-1]: If this condition is met, we can conclude that row i has the possibility of containing the target.
# So, we will apply binary search on row i, and check if the ‘target’ is present. If it is present, we will return true from this step. Otherwise, we will return false.
# Otherwise, after completing the traversal, we will return false.

class Solution:
    # Function to perform binary search on a list
    def binarySearch(self, nums, target):
        # Get the length of the array
        n = len(nums)

        # Initialize low and high pointers
        low, high = 0, n - 1

        # Binary search loop
        while low <= high:
            # Calculate the middle index
            mid = (low + high) // 2

            # If target is found at mid
            if nums[mid] == target:
                return True

            # If target is greater, search right half
            elif target > nums[mid]:
                low = mid + 1

            # Otherwise, search left half
            else:
                high = mid - 1

        # Return False if not found
        return False

    # Function to search for target in 2D matrix
    def searchMatrix(self, matrix, target):
        # Get number of rows
        n = len(matrix)

        # Get number of columns
        m = len(matrix[0])

        # Traverse each row
        for i in range(n):
            # Check if target can be in this row
            if matrix[i][0] <= target <= matrix[i][m - 1]:
                # Perform binary search on this row
                return self.binarySearch(matrix[i], target)

        # Return False if not found
        return False

# Driver code
if __name__ == "__main__":
    # Define a 2D matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # Create an object of the Solution class
    obj = Solution()

    # Call the searchMatrix method and print the result
    if obj.searchMatrix(matrix, 8):
        print("true")
    else:
        print("false")

# Time Complexity: O(n × log m), We go through each of the `n` rows once. For any valid row where the target can exist, we apply binary search which takes O(log m). So overall time = O(n × log m).

# Space Complexity: O(1), No extra space is used just a few integer variables for looping and binary search. So space complexity is constant.

# optimal 
# If we flatten the given 2D matrix into a 1D array, that 1D array would also be sorted. By running binary search on this flattened version, we could quickly check if the element exists.

# But actually flattening the matrix takes extra time and memory, which makes it inefficient. Instead, we can simulate the flattening without creating a new array. The trick is to directly map a 1D index into the corresponding row and column of the 2D matrix.

# To do this mapping, if there are `m` columns in the matrix and the index is `i`, then:
# Row = i / m, Column = i % m.

# So instead of working on the 2D matrix directly, we pretend it’s a sorted 1D array of length (rows × columns), and apply binary search on this imaginary array.

# Start with two pointers: one at the first index of the imaginary 1D array, and the other at the last index.
# While the first pointer does not cross the last:
# Find the middle index between the two pointers.
# Convert this middle index into a row and column of the original 2D matrix.
# If the element at that position matches the target, return true (element found).
# If the element is smaller than the target, discard the left half and continue searching in the right half.
# If the element is larger than the target, discard the right half and continue searching in the left half.
# If the search ends without finding the element, return false (element not present in the matrix).

class Solution:
    # Function to search target in 2D matrix using binary search
    def searchMatrix(self, matrix, target):
        # Get number of rows and columns
        n = len(matrix)
        m = len(matrix[0])

        # Set initial binary search range
        low = 0
        high = n * m - 1

        # Perform binary search
        while low <= high:
            # Calculate middle index
            mid = (low + high) // 2

            # Convert 1D index to 2D indices
            row = mid // m
            col = mid % m

            # Check if target is found
            if matrix[row][col] == target:
                return True
            # Discard left half
            elif matrix[row][col] < target:
                low = mid + 1
            # Discard right half
            else:
                high = mid - 1

        # Target not found
        return False

# Driver code
if __name__ == "__main__":
    # Define 2D matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # Create object of Solution
    obj = Solution()

    # Call the method and print result
    print("true" if obj.searchMatrix(matrix, 8) else "false")

# Time Complexity: O(log(NxM)), where N = given row number, M = given column number.We are applying binary search on the imaginary 1D array of size NxM.

# Space Complexity: O(1) as we are not using any extra space.