#  Given an array/list of length ‘N’, where the array/list represents the boards and each element of the given array/list represents the length of each board. Some ‘K’ numbers of painters are available to paint these boards. Consider that each unit of a board takes 1 unit of time to paint. You are supposed to return the area of the minimum time to get this job done of painting all the ‘N’ boards under the constraint that any painter will only paint the continuous sections of boards.

# Example 1:
# Input Format: N = 4, boards[] = {5, 5, 5, 5}, k = 2
# Result: 10
# Explanation: We can divide the boards into 2 equal-sized partitions, so each painter gets 10 units of the board and the total time taken is 10.

# brute
# First, we will find the maximum element and the summation of the given array.
# We will use a loop(say time) to check all possible answers from max(arr[]) to sum(arr[]).
# Next, inside the loop, we will send ‘time’, to the function countPainters() function to get the number of painters to whom we can allocate the boards.
# The first value of ‘time’, for which the number of painters will be lesser or equal to ‘k’, will be our answer. So, we will return that particular value of ‘time’.
# Finally, if we are out of the loop, we will return max(arr[]) as there cannot exist any answer smaller than that.
from typing import List

class PainterPartition:
    # Helper to count how many painters are required for a given max time
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1              # Start with one painter
        boards_painter = 0        # Current load on a painter

        for board in boards:
            if boards_painter + board <= time:
                # Assign board to the current painter
                boards_painter += board
            else:
                # Assign board to a new painter
                painters += 1
                boards_painter = board

        return painters

    # Function to find the minimum maximum time to paint all boards with k painters
    def find_largest_min_distance(self, boards: List[int], k: int) -> int:
        low = max(boards)         # No painter can paint less than the largest board
        high = sum(boards)        # All boards painted by one painter (max possible)

        for time in range(low, high + 1):
            if self.count_painters(boards, time) <= k:
                return time       # Found a valid configuration

        return low  # Fallback case

# Test case
boards = [10, 20, 30, 40]
k = 2

pp = PainterPartition()
ans = pp.find_largest_min_distance(boards, k)

print("The answer is:", ans)  # Expected: 60

# Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
# Space Complexity: O(1), no extra space used.

# optimal
# Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to max(arr[]) and the high will point to sum(arr[]).
# Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula: mid = (low+high) // 2 ( ‘//’ refers to integer division.
# Eliminate the halves based on the number of painters returned by countPainters(): We will pass the potential value of time, represented by the variable 'mid', to the ‘countPainters()' function. This function will return the number of painters we need to paint all the boards
# If painters > k: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
# Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
# Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.
from typing import List

class PainterPartition:
    # Count painters required for a given max allowed time
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1
        boards_painter = 0

        for board in boards:
            if boards_painter + board <= time:
                boards_painter += board
            else:
                painters += 1
                boards_painter = board

        return painters

    # Use binary search to find the minimum time
    def find_largest_min_distance(self, boards: List[int], k: int) -> int:
        low = max(boards)
        high = sum(boards)
        result = high

        while low <= high:
            mid = (low + high) // 2
            painters = self.count_painters(boards, mid)

            if painters > k:
                low = mid + 1  # Too few painters, increase time
            else:
                result = mid   # Valid time, try reducing it
                high = mid - 1

        return result

# Test
boards = [10, 20, 30, 40]
k = 2
pp = PainterPartition()
ans = pp.find_largest_min_distance(boards, k)
print("The answer is:", ans)  # Expected: 60

# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
# Space Complexity: O(1) since no extra space is required.