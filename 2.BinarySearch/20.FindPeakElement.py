# Problem Statement: Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the array [i, j]. A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbours to the left, right, top, and bottom.
# Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

# Example 1:
# Input:
#  mat = [[5, 10, 8], [4, 25, 7], [3, 9, 6]]
# Output:
#  [1, 1]
# Explanation:
#  The value at index [1, 1] is 25, which is a peak because all its neighbors (10, 7, 4, 9) are smaller.

# theres only one solution, its the most optimal
# To solve this problem we use the binary search approach.
# The key idea comes from how we find a peak in a 1-D array:
# For any middle position (mid), we check if it’s larger than both its neighbors, if it is, we’ve found a peak.
# If mid is smaller than the element on its left, that means a peak must be somewhere to the left, so we can discard the right half.
# If mid is smaller than the element on its right, then a peak must lie to the right, allowing us to discard the left half.
# This method reduces the number of elements we need to consider in every step, improving efficiency.
# For a 2-D array,
# The search will cover the column range from 0 to col-1, where col is the total number of columns.
# We choose a middle column and identify the row with the largest element in that column.
# We apply similar logic as in 1-D: if this element is bigger than both its side neighbors, we’ve found the peak.
# If the left neighbor is bigger, we only search the left part; if the right neighbor is bigger, we search the right part.

class Solution:
      # Helper function to find the index of the row 
      # with the maximum element in a given column
      def maxElement(self, arr, col):
          n = len(arr)
          max_val = float('-inf')
          index = -1
  
          # Iterate through each row to find the maximum element 
          # in the specified column
          for i in range(n):
              if arr[i][col] > max_val:
                  max_val = arr[i][col]
                  index = i
  
          return index
  
      # Function to find a peak element in the 2D matrix 
      # using binary search 
      def findPeakGrid(self, arr):
          n = len(arr)    
          m = len(arr[0])  
  
          # Initialize the lower and upper bounds for binary search
          low = 0
          high = m - 1
  
          while low <= high:
              mid = (low + high) // 2
  
              # Find the index of the row with the maximum element 
              # in the middle column
              row = self.maxElement(arr, mid)
  
              # Determine the elements to the left and right of 
              # the middle element in the found row
              left = arr[row][mid - 1] if mid - 1 >= 0 else float('-inf')
              right = arr[row][mid + 1] if mid + 1 < m else float('-inf')
  
              # Check if the middle element is greater than its neighbors
              if arr[row][mid] > left and arr[row][mid] > right:
                  return [row, mid]
              elif left > arr[row][mid]:
                  high = mid - 1
              else:
                  low = mid + 1
  
          # Return [-1, -1] if no peak element is found
          return [-1, -1]
  
  
mat = [
      [4, 2, 5, 1, 4, 5],
      [2, 9, 3, 2, 3, 2],
      [1, 7, 6, 0, 1, 3],
      [3, 6, 2, 3, 7, 2]
  ]
  
  # Create an instance of Solution class
sol = Solution()
  
  # Call findPeakGrid function and print the result
peak = sol.findPeakGrid(mat)
print(f"The row of peak element is {peak[0]} and "
        f"column of the peak element is {peak[1]}")