# see the thing is array questions will almost always follow the same set of brute better optimal
# brute will be sorting or using a map
# better will be hash map or set or something similar
# optimal will be two pointers, this is even used for reversing

# brute approach
# Define the Solution class
class Solution:
    # Function to find union of two arrays
    def FindUnion(self, arr1, arr2, n, m):
        # Create a dictionary to store frequency
        freq = {}
        # Loop through first array and store frequency
        for i in range(n):
            freq[arr1[i]] = freq.get(arr1[i], 0) + 1
        # Loop through second array and store frequency
        for i in range(m):
            freq[arr2[i]] = freq.get(arr2[i], 0) + 1
        # Create a list to store sorted unique elements
        Union = sorted(freq.keys())
        # Return the union list
        return Union

# Driver code
if __name__ == "__main__":
    # Define size of first array
    n = 10
    # Define size of second array
    m = 7
    # Initialize first array
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Initialize second array
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    # Create object of Solution class
    obj = Solution()
    # Call FindUnion method
    Union = obj.FindUnion(arr1, arr2, n, m)
    # Print output message
    print("Union of arr1 and arr2 is")
    # Print all elements of union
    print(*Union)

# better approach
class Solution:
    # Function to find the union of two arrays using set
    def findUnion(self, arr1, arr2):
        # Create a set with elements from both arrays
        st = set(arr1) | set(arr2)  # Union of two sets

        # Return sorted list
        return sorted(st)

# Driver code
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

obj = Solution()
result = obj.findUnion(arr1, arr2)

print("Union of arr1 and arr2 is:", *result)

# optimal
class Solution:
    # Function to find union of two sorted arrays using two pointers
    def findUnion(self, arr1, arr2, n, m):
        # List to store union elements
        Union = []

        # Initialize pointers
        i, j = 0, 0

        # Iterate while both pointers are within array bounds
        while i < n and j < m:
            # If element in arr1 is smaller
            if arr1[i] < arr2[j]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
            # If element in arr2 is smaller
            elif arr2[j] < arr1[i]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr2[j]:
                    Union.append(arr2[j])
                j += 1
            else:
                # Elements are equal, add once if not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
                j += 1

        # Append remaining elements from arr1
        while i < n:
            if not Union or Union[-1] != arr1[i]:
                Union.append(arr1[i])
            i += 1

        # Append remaining elements from arr2
        while j < m:
            if not Union or Union[-1] != arr2[j]:
                Union.append(arr2[j])
            j += 1

        # Return the union list
        return Union


# Driver code
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    n, m = len(arr1), len(arr2)

    obj = Solution()
    result = obj.findUnion(arr1, arr2, n, m)
    print("Union of arr1 and arr2 is:", *result)
