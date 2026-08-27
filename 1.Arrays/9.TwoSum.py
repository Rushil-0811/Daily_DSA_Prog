# brute we gonna use two loops
class Solution:
    # Function to check if any two numbers sum up to target (variant 1)
    def two_sum_exists(self, arr, target):
        n = len(arr)
        # Outer loop picks one element at a time
        for i in range(n):
            # Inner loop searches for another element that complements arr[i]
            for j in range(i + 1, n):
                # If sum equals target, return "YES"
                if arr[i] + arr[j] == target:
                    return "YES"
        # No pair found that sums to target
        return "NO"

    # Function to return indices of two numbers that sum to target (variant 2)
    def two_sum_indices(self, arr, target):
        n = len(arr)
        # Outer loop picks one element at a time
        for i in range(n):
            # Inner loop searches for another element that complements arr[i]
            for j in range(i + 1, n):
                # If sum equals target, return the pair of indices
                if arr[i] + arr[j] == target:
                    return [i, j]
        # No such pair found
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()

    arr = [2, 6, 5, 8, 11]
    target = 14

    # Variant 1
    print(sol.two_sum_exists(arr, target))

    # Variant 2
    print(sol.two_sum_indices(arr, target))

# better we gonna use hash map
class Solution:
    # Variant 1: Check if two numbers sum to target using hashing
    def two_sum_exists(self, arr, target):
        mp = {}  # Dictionary to store element -> index
        # Iterate over all elements
        for i, num in enumerate(arr):
            complement = target - num
            # Check if complement exists in dictionary
            if complement in mp:
                return "YES"  # Pair found
            # Store current element and its index
            mp[num] = i
        # No pair found
        return "NO"

    # Variant 2: Return indices of two numbers that sum to target using hashing
    def two_sum_indices(self, arr, target):
        mp = {}  # Dictionary to store element -> index
        for i, num in enumerate(arr):
            complement = target - num
            # If complement found, return indices
            if complement in mp:
                return [mp[complement], i]
            # Store current element and index
            mp[num] = i
        # No pair found
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.two_sum_exists(arr, target))
    print(sol.two_sum_indices(arr, target))

# optimal we gonna use two pointers, but this is also called greedy for some reason
class Solution:
    # Variant 1: Check if two numbers sum to target using two-pointer approach
    def two_sum_exists(self, arr, target):
        # Create list of tuples (value, original_index)
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        
        # Sort list based on the values (to apply two-pointer technique)
        nums_with_index.sort(key=lambda x: x[0])

        # Initialize two pointers: left at start, right at end
        left, right = 0, len(arr) - 1
        
        # Continue until pointers cross
        while left < right:
            # Calculate sum of values at pointers
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            
            if current_sum == target:
                # Found a pair
                return "YES"
            elif current_sum < target:
                # Sum too small, move left pointer to right to increase sum
                left += 1
            else:
                # Sum too large, move right pointer to left to decrease sum
                right -= 1
        
        # No pair found
        return "NO"

    # Variant 2: Return indices of two numbers that sum to target
    def two_sum_indices(self, arr, target):
        # Create list of tuples (value, original_index)
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        
        # Sort the list by values
        nums_with_index.sort(key=lambda x: x[0])

        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                # Return original indices of found elements
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                # Move left pointer right to increase sum
                left += 1
            else:
                # Move right pointer left to decrease sum
                right -= 1
        
        # No valid pair found
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.two_sum_exists(arr, target))  # Output: YES
    print(sol.two_sum_indices(arr, target)) # Output: [1, 3]


