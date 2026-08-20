#  Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.
# brute
# The problem states that every number in the array appears exactly twice, except for one number that appears only once. If we traverse through the array and compare each element with its neighbors, we can detect the unique number. If an element is not equal to its left and right neighbors, then it must be the single number.

# We handle corner cases:
# If it’s the first element, just compare it with the next.
# If it’s the last element, just compare it with the previous.
# Approach
# Find the total size of the array.
# If the size is equal to one, return the only element.
# Traverse the array from start to end.
# If the current element is the first one, compare it with the next. If they are different, return it.
# If the current element is the last one, compare it with the previous. If they are different, return it.
# Otherwise, compare the current element with both previous and next. If it is different from both, return it.
# If no such element is found during traversal, return an invalid marker (though by problem guarantee, one will always exist).
class Solution:
    def singleNonDuplicate(self, arr):
        # Get the size of the array
        n = len(arr)

        # If array has only one element, return it
        if n == 1:
            return arr[0]

        # Loop through the array
        for i in range(n):
            # Check if it's the first element and not equal to the next
            if i == 0:
                if arr[i] != arr[i + 1]:
                    return arr[i]

            # Check if it's the last element and not equal to the previous
            elif i == n - 1:
                if arr[i] != arr[i - 1]:
                    return arr[i]

            # Check if the current element is not equal to both neighbors
            else:
                if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                    return arr[i]

        # Dummy return if no element found
        return -1

# Driver code
if __name__ == "__main__":
    # Input array with one unique element
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

    # Create an object of Solution class
    obj = Solution()

    # Call the function and store result
    ans = obj.singleNonDuplicate(arr)

    # Print the result
    print("The single element is:", ans)

# brute 2 will be using the xor method

# optimal
# The array is sorted, and all elements except one appear exactly twice. If we observe carefully, every pair starts at even index and ends at odd index when the array is still balanced (i.e., before the unique element is encountered).

# But once the unique element is inserted, this pairing pattern breaks and the shift happens after that unique element. So we can use this pattern to cut the search space in half using binary search:
# If the pairing is proper (i.e., arr[mid] == arr[mid ^ 1]), then the unique (non-duplicate) element lies in the right half.
# If the pairing breaks (i.e., arr[mid] != arr[mid ^ 1]), then the unique element lies in the left half.
# This leads us to an O(log n) solution by binary eliminating half of the array every step.
# Check if the array has only one element, return that element.
# Check if the first element is not equal to the second return the first.
# Check if the last element is not equal to the second last return the last.
# Set two pointers: low = 1, high = n - 2 (excluding boundary elements).
# Run a loop while low ≤ high:
# Find mid = (low + high) / 2.
# If arr[mid] ≠ arr[mid - 1] and arr[mid] ≠ arr[mid + 1], return arr[mid].
# Check if mid is part of a correct pair:
# If mid is even and arr[mid] == arr[mid + 1], or
# If mid is odd and arr[mid] == arr[mid - 1],
# Then the unique element lies to the right, so move low = mid + 1.
# Otherwise, move high = mid - 1.
# If no unique element is found (theoretically unreachable), return -1.

class Solution:
      # Function to find the single non-duplicate element using binary search
    def singleNonDuplicate(self, arr):
        # Get the size of the array
        n = len(arr)

        # Edge case: only one element in the array
        if n == 1:
            return arr[0]

        # Edge case: first element is the unique one
        if arr[0] != arr[1]:
            return arr[0]

        # Edge case: last element is the unique one
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]

        # Initialize binary search bounds
        low, high = 1, n - 2

        # Perform binary search
        while low <= high:
            # Calculate middle index
            mid = (low + high) // 2

            # Check if middle element is the unique one
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]

            # If mid is in the left half (pairing is valid)
            if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or \
               (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                # Move to the right half
                low = mid + 1
            else:
                # Move to the left half
                high = mid - 1

        # Dummy return (not reachable if input is valid)
        return -1

# Driver code
if __name__ == "__main__":
    # Input array with all elements appearing twice except one
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

    # Create an object of Solution class
    obj = Solution()

    # Call the function and store the result
    ans = obj.singleNonDuplicate(arr)

    # Print the result
    print("The single element is:", ans)
