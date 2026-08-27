#  Q- You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. The elements of each row and each column are sorted in non-decreasing order. But, the first element of a row is not necessarily greater than the last element of the previous row (if it exists). You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.

# Example 1:
# Matrix=
# 1   4   7   11
# 2   5   8   12
# 3   6   9   16
# 10 13  14  17
# Target: 9
# Output: Found at (2,2) (0-indexed)

# brute
# We will use a loop to select a particular row at a time.
# Next, for every row, we will use another loop to traverse each column.
# Inside the loops, we will check if the element i.e. matrix[i][j] is equal to the ‘target’. If we found any matching element, we will return true.
# Finally, after completing the traversal, if we found no matching element, we will return false.

from typing import List

# Class to handle matrix search operations
class MatrixSearch:
    def __init__(self, matrix: List[List[int]]):
        """
        Initialize the matrix object
        :param matrix: 2D list representing the matrix
        """
        self.matrix = matrix

    def search_element(self, target: int) -> bool:
        """
        Search for the target element in the matrix
        :param target: integer value to search
        :return: True if target exists, False otherwise
        """
        n = len(self.matrix)       # Number of rows
        m = len(self.matrix[0])    # Number of columns

        # Traverse each row
        for i in range(n):
            # Traverse each column in the current row
            for j in range(m):
                # Check if current element matches the target
                if self.matrix[i][j] == target:
                    return True  # Target found

        # Target not found in the matrix
        return False


if __name__ == "__main__":
    # Define a 2D row and column-wise sorted matrix
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    # Create MatrixSearch object
    ms = MatrixSearch(matrix)

    # Search for element 8
    found = ms.search_element(8)

    # Print the result
    print(found)  # True

#  tc Time Complexity: O(N X M), where N = given row number, M = given column number in order to traverse the matrix, we are using nested loops running for n and m times respectively.
# Space Complexity: O(1) as we are not using any extra space.

# better
# We will use a loop to select a particular row at a time.
# Next, for every row, i, we will check if it contains the target using binary search.
# After applying binary search on row, if we found any element equal to the target, we will return true. Otherwise, we will move on to the next row.
# Finally, after completing all the row traversals, if we found no matching element, we will return false.

from typing import List

# Class to perform binary search operations in a 2D matrix
class MatrixSearch:
    def __init__(self, matrix: List[List[int]]):
        """
        Initialize the MatrixSearch object with a given 2D matrix.
        :param matrix: A 2D list of integers representing the matrix.
                       The matrix is assumed to be row-wise sorted.
        """
        self.matrix = matrix  # Store the matrix inside the object

    def binary_search(self, nums: List[int], target: int) -> bool:
        """
        Perform binary search on a single row (1D list).
        Binary search works efficiently on sorted arrays.

        :param nums: List of integers (one row of the matrix)
        :param target: Integer value we want to search
        :return: True if target exists in nums, False otherwise
        """
        # Initialize pointers to the first and last elements
        low = 0
        high = len(nums) - 1

        # Continue searching while there are elements to check
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2
            # Check if middle element is the target
            if nums[mid] == target:
                return True  # Target found
            # If target is greater than mid element, search in right half
            elif target > nums[mid]:
                low = mid + 1
            # If target is smaller than mid element, search in left half
            else:
                high = mid - 1

        # Target not found in the row
        return False

    def search_element(self, target: int) -> bool:
        """
        Search for the target element in the entire matrix.
        It uses binary search on each row individually.

        :param target: Integer value to search for in the matrix
        :return: True if target exists in the matrix, False otherwise
        """
        # Loop through each row in the matrix
        for i, row in enumerate(self.matrix):
            # Call binary search on the current row
            found_in_row = self.binary_search(row, target)
            # If target is found in this row, return True immediately
            if found_in_row:
                return True

        # If the loop finishes without returning, target is not in any row
        return False

# Example usage
if __name__ == "__main__":
    # Define a 2D matrix sorted in each row
    matrix = [
        [1, 4, 7, 11, 15],   # Row 0
        [2, 5, 8, 12, 19],   # Row 1
        [3, 6, 9, 16, 22],   # Row 2
        [10, 13, 14, 17, 24],# Row 3
        [18, 21, 23, 26, 30] # Row 4
    ]

    # Create a MatrixSearch object and pass the matrix
    ms = MatrixSearch(matrix)

    # Search for the number 8
    found = ms.search_element(8)

    # Print the result (True if found, False otherwise)
    print(found)  # Expected output: True

# Time Complexity: O(N*logM), where N = given row number, M = given column number. We are traversing all rows and it takes O(N) time complexity. And for all rows, we are applying binary search. So, the total time complexity is O(N*logM).

# Space Complexity: O(1) as we are not using any extra space.

# optimal

# As we are starting from the cell (0, m-1), the two variables i.e. ‘row’ and ‘col’ will point to 0 and m-1 respectively.
# We will do the following steps until row < n and col >= 0(i.e. while(row < n && col >= 0)):
# If matrix[row][col] == target: We have found the target and so we will return true.
# If matrix[row][col] > target: We need the smaller elements to reach the target. But the column is in increasing order and so it contains only greater elements. So, we will eliminate the column by decreasing the current column value by 1(i.e. col--) and thus we will move row-wise.
# If matrix[row][col] < target: In this case, We need the bigger elements to reach the target. But the row is in decreasing order and so it contains only smaller elements. So, we will eliminate the row by increasing the current row value by 1(i.e. row++) and thus we will move column-wise.
# If we are outside the loop without getting any matching element, we will return false.

from typing import List

# Class to perform staircase search in a 2D row and column-wise sorted matrix
class MatrixSearch:
    def __init__(self, matrix: List[List[int]]):
        """
        Initialize the matrix search object.
        :param matrix: 2D list representing the sorted matrix
        """
        self.matrix = matrix

    def search_element(self, target: int) -> bool:
        """
        Search for the target element using staircase search.
        Start from the top-right corner and move left or down depending on value.
        Time complexity: O(n + m)
        :param target: Integer to search for
        :return: True if target exists in matrix, False otherwise
        """
        n = len(self.matrix)       # Number of rows
        m = len(self.matrix[0])    # Number of columns

        row = 0            # Start at first row
        col = m - 1        # Start at last column (top-right)

        # Loop until we go out of matrix bounds
        while row < n and col >= 0:
            current = self.matrix[row][col]  # Current element
            if current == target:
                return True  # Found target
            elif current < target:
                row += 1     # Move down to next row
            else:
                col -= 1     # Move left to previous column

        # Target not found after traversing
        return False


if __name__ == "__main__":
    # Example matrix
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    ms = MatrixSearch(matrix)
    found = ms.search_element(8)
    print(found)  # True

# Time Complexity: O(N+M), where N = given row number, M = given column number. We are starting traversal from (0, M-1), and at most, we can end up being in the cell (M-1, 0). So, the total distance can be at most (N+M). So, the time complexity is O(N+M).

# Space Complexity: O(1) as we are not using any extra space.