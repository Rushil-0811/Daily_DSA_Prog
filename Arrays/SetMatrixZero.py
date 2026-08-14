# brute find all zeroes, replace the elements in their row and column with -1
# replace all -1 with zero
class Solution:
     # Function to set entire row and column to 0 if an element in the matrix is 0
    def setZeroes(self, matrix):
        # Get number of rows
        m = len(matrix)
        # Get number of columns
        n = len(matrix[0])

        # First pass: mark rows and columns
        for i in range(m):
            for j in range(n):
                # If current cell is zero
                if matrix[i][j] == 0:
                    # Mark entire row
                    for col in range(n):
                        if matrix[i][col] != 0:
                            matrix[i][col] = -1
                    # Mark entire column
                    for row in range(m):
                        if matrix[row][j] != 0:
                            matrix[row][j] = -1

        # Second pass: replace -1 with 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

# Driver code
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
sol.setZeroes(matrix)
for row in matrix:
    print(row)

# better
# instead of marking directly as -1 within array we keep 2 separate arrays outside
# one to track rows to be zero
# one to track cols to be zero
# u mark accordingly and after complete scan u back and replace the marked positions with zero
class Solution:
    # Function to set entire row and column to 0 if an element in the matrix is 0
    def setZeroes(self, matrix):
        # Get number of rows
        m = len(matrix)
        # Get number of columns
        n = len(matrix[0])

        # Create row marker array
        row = [0] * m
        # Create column marker array
        col = [0] * n

        # First pass: mark rows and columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                # If element is zero, mark its row and column
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        # Second pass: set cells to zero based on markers
        for i in range(m):
            for j in range(n):
                # If the row or column is marked, set cell to zero
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

# Driver code
matrix = [[1,1,1],[1,0,1],[1,1,1]]
obj = Solution()
obj.setZeroes(matrix)
for r in matrix:
    print(r)

# optimal
# Instead of using separate arrays, we use the first row and first column of the matrix itself to store whether a row or column needs to be zeroed. We also store two flags:
# firstRowZero:Was the first row supposed to be all zero?
# firstColZero:Was the first column supposed to be all zero?
# Then:
# First pass: Mark zeros in the first row and column for any zero found in the rest of the matrix.
# Second pass: Use those markers to set rows and columns to zero.
# Finally, handle the first row and column separately based on the flags. This is super space-efficient because we’re reusing the input matrix itself to store markers.
# Check if the first row has any zero and store in a boolean flag.
# Check if the first column has any zero and store in a boolean flag.
# Traverse the rest of the matrix:
# If a cell is zero, mark its row in the first column and its column in the first row as zero.
# Traverse again (excluding first row and column), setting cells to zero if their row marker or column marker is zero.
# Finally, update the first row and first column based on the stored flags.
class Solution:
    # Function to set entire row and column to 0 if an element in the matrix 
    def setZeroes(self, matrix):
        # Get dimensions of matrix
        m = len(matrix)
        n = len(matrix[0])

        # Flag to track if first row should be zeroed
        first_row_zero = False
        # Flag to track if first column should be zeroed
        first_col_zero = False

        # Check if first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row/column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# Driver code
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
for row in matrix:
    print(row)
