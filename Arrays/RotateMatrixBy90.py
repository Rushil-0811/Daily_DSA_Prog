# Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. The rotation must be done in place, meaning the input 2D matrix must be modified directly.
# brute
# In a 90-degree clockwise rotation, each element in the matrix moves from its original position to a new position based on a specific pattern. The first column becomes the first row (in reverse order) and second column becomes the second row, and so on.
# We can simulate this movement by using a new matrix. For each element at position (i, j) in the original matrix, we calculate its new position in the rotated matrix as (j, n - i - 1) where n is the size of the matrix.
# Initialize an empty matrix of the same size (n x n).
# Loop through every element of the original matrix using two nested loops.
# For each element at position (i, j), place it in the new matrix at position (j, n - i - 1).
# After completing the placement for all elements, return or copy the new matrix.
class Solution:
    # Function to rotate the matrix 90 degrees clockwise using extra space
    def rotateClockwise(self, matrix):
        # Get the size of the square matrix
        n = len(matrix)

        # Create a new matrix of same size to store rotated result
        rotated = [[0] * n for _ in range(n)]

        # Traverse each element of original matrix
        for i in range(n):
            for j in range(n):
                # Place the element at its new rotated position
                rotated[j][n - i - 1] = matrix[i][j]

        # Return the rotated matrix
        return rotated

# Driver code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

obj = Solution()
rotated = obj.rotateClockwise(matrix)

# Print the rotated matrix
for row in rotated:
    print(*row)

# optimal
# To rotate a matrix 90 degrees clockwise in-place (without using extra space), we use two key matrix operations:
# Step 1: Transpose the matrix: swap elements across the diagonal. This converts rows into columns.
# Step 2: Reverse each row: this turns the new columns into the final rotated rows.

# This works because:
# Transposing moves elements from (i, j) to (j, i), effectively rotating across the diagonal.
# Reversing the rows repositions the elements in each row, finalizing the clockwise rotation.
# Get the size of the square matrix (number of rows or columns).
# Start the first phase: Transpose the matrix
# For each row starting from the top to bottom:
# For each column starting from the diagonal element (excluding already visited elements):
# Swap the current element with the element that is diagonally opposite across the main diagonal.
# This effectively flips the matrix over its top-left to bottom-right diagonal, converting rows into columns.
# Move to the second phase: Reverse each row
# For every row in the matrix:
# Reverse the order of the elements in that row (first element becomes last, second becomes second last, and so on).
# This realigns the columns to their correct position for the clockwise rotation.
# Once both phases are done, the matrix will have been rotated 90 degrees clockwise in-place.
class Solution:
    # Function to rotate matrix 90 degrees clockwise in-place
    def rotateClockwise(self, matrix):
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                # Swap element at (i, j) with (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            # Reverse the current row to simulate clockwise rotation
            matrix[i].reverse()

# Driver code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

obj = Solution()
obj.rotateClockwise(matrix)

# Print rotated matrix
for row in matrix:
    print(*row)
