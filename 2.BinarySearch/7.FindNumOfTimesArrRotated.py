# Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated.
#  In brute force, we simply search for the smallest element in the array because it’s the point where the rotation happened its index directly tells us the rotation count. But brute force does this without thinking about sorted array properties just check every element one by one.
class Solution:
    # Function to find the number of rotations in a rotated sorted array
    def findRotations(self, arr):
        # Store size of array
        n = len(arr)

        # Assume the first element is the smallest
        minVal = arr[0]

        # Index of the smallest element
        minIndex = 0

        # Traverse the array
        for i in range(1, n):
            # If current element is smaller than minVal, update
            if arr[i] < minVal:
                minVal = arr[i]
                minIndex = i

        # The index of smallest element = number of rotations
        return minIndex


# Driver code
if __name__ == "__main__":
    obj = Solution()

    # Example input
    arr = [4,5,6,7,0,1,2,3]

    # Call the function and store result
    rotations = obj.findRotations(arr)

    # Print result
    print(rotations)

# better
# Think of the sorted array as a sorted belt of numbers. Rotation just cuts the belt at one position and reattaches it. The spot where the order breaks where a number is bigger than the next number is exactly where the cut happened. So instead of searching for the minimum value by comparing all values to a running minimum, just walk once through the array and find the first place where the sequence goes down. The rotation count is the number of steps from the start to that break point. If there’s no break, the array wasn’t rotated.
# Traverse the array from the first element to the second-last element.
# At each step, check if the current element is greater than the next element.
# If such a break is found, return the index of the next element (that index is the rotation count).
# If no break is found after the full pass, return 0 (array not rotated).
class Solution:
    # Function to find rotation count using one-pass scan
    def findRotationCount(self, arr):
        # Get size of array
        n = len(arr)
        # Traverse till second-last element
        for i in range(n - 1):
            # If break point found
            if arr[i] > arr[i + 1]:
                # Return index of next element as rotation count
                return i + 1
        # No rotation found
        return 0

# Driver code
if __name__ == "__main__":
    # Example input
    arr = [3, 4, 5, 1, 2]

    # Create Solution object
    sol = Solution()

    # Call the function
    rotations = sol.findRotationCount(arr)

    # Output result
    print(rotations)

# optimal
# Think of the rotated sorted array as two sorted halves the rotation “break” point is where the smallest element lives. Using binary search, we can efficiently zoom in on this smallest element by comparing middle elements to the rightmost element. If the middle element is greater than the rightmost element, the rotation point is to the right. Otherwise, it's to the left or could be the middle itself. This way, we reduce the search space by half each time, getting the rotation count in O(log n).

# Imagine searching for the break in a long sorted belt by cutting it in halves repeatedly instead of scanning all the way through.
# Initialize low = 0 and high = n - 1.
# While low is less than high:
# Find mid index.
# If the element at mid is greater than the element at high, the rotation point is after mid, so update low = mid + 1.
# Else, the rotation point is at mid or before it, so update high = mid.
# When low meets high, that index is the rotation count (index of smallest element).
class Solution:
    # Function to find rotation count using binary search
    def findRotations(self, arr):
        low = 0
        high = len(arr) - 1

        # Loop until low meets high
        while low < high:
            mid = low + (high - low) // 2

            # If mid element is greater than element at high,
            # smallest element lies to the right of mid
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                # Else smallest element is at mid or to the left
                high = mid

        # When low == high, we found the smallest element
        return low

# Driver code
if __name__ == "__main__":
    arr = [4,5,6,7,0,1,2,3]
    sol = Solution()
    rotations = sol.findRotations(arr)
    print(rotations)
