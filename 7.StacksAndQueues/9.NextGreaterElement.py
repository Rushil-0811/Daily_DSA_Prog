# Next Greater Element Using a Monotonic Stack

# An integer array arr is given. For every position, find the first later element with a value strictly greater than the value at the current position.

# Store -1 for every position without a greater value on the right. Return all answers in the original array order.

# Example 1
# Input: arr = [4, 5, 2, 10, 8]
# Output: [5, 10, 10, -1, -1]
# Explanation: Value 5 is the first greater value after 4. Value 10 is the first greater value after both 5 and 2. No greater value appears after 10 or 8.

# Brute Force Approach
# The nearest greater element must appear somewhere to the right of the current value. Checking the right side in order ensures that the first greater value found is also the nearest one.

# The search stops after finding that value. If no greater value exists, the answer remains -1. This method is easy to understand but uses nested loops.

# Algorithm
# Create an answer array of size N and initialize every position with -1, covering cases where no greater value exists on the right.

# Select each array index from left to right as the current position requiring a next greater element.

# Scan all later positions in increasing index order, because the first valid value encountered is the nearest greater element.

# Compare every right-side value with the current array value and accept only a strictly larger value.

# Store the first accepted value at the corresponding answer index and stop the inner scan, because every remaining candidate appears farther to the right.

# Keep the initial value -1 when the complete right-side scan finds no strictly greater value.

# Return the completed answer array after processing every index.

class Solution:
    # Finds the next greater value for every position.
    def nextGreaterElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        answer = [-1] * n

        # Match each position with the nearest greater value.
        for i in range(n):
            # Check right-side positions from nearest to farthest.
            for j in range(i + 1, n):
                # A larger value ends the search at the nearest match.
                if arr[j] > arr[i]:
                    answer[i] = arr[j]
                    break

        return answer


# Driver code
def main() -> None:
    arr = [2, 1, 2, 4, 3]
    obj = Solution()
    answer = obj.nextGreaterElements(arr)
    print(answer)


if __name__ == "__main__":
    main()

# Note: Brute force may fail for large arrays. Repeated right-side scans create quadratic work, so an online judge may report Time Limit Exceeded.

# Complexity Analysis
# Time Complexity: O(N2), every index may scan all later positions in the worst case.

# Space Complexity: O(N), the returned answer array stores one result per position, while auxiliary working space is O(1).

# Optimal Approach
# While moving from right to left, every value already processed lies on the right side of the current element. We maintain a monotonic stack to efficiently find the Next Greater Element (NGE). A monotonic stack keeps its values in a consistent increasing or decreasing order, which helps remove elements that can no longer be useful.

# For the current element, first remove stack values that are smaller than or equal to it. After this, if the stack is empty, no greater element exists on the right, so its NGE is -1. Otherwise, the stack top is its NGE.

# After finding the NGE, update the stack so it can help elements further to the left. Remove values that cannot serve as a greater element in the future, then push the current value as a new possible candidate.

# Algorithm
# Create an answer array of size N and initialize every position with -1.

# Create an empty monotonic stack to store potential greater elements.

# Traverse the array from index N - 1 to 0, because the stack must contain only elements appearing to the right of the current index.

# For each current element:

# Remove values from the stack while the top is smaller than or equal to the current value, because they cannot be its Next Greater Element.

# If the stack is empty, keep the answer as -1, because no greater element exists on the right. Otherwise, store the stack top as the NGE.

# Push the current value into the stack so it can become a potential greater element for elements further to the left.

# Return the completed answer array.

class Solution:
    # Finds next greater values with a monotonic stack.
    def nextGreaterElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        answer = [-1] * n
        candidates = []

        # Scan right to left to prepare valid candidates.
        for i in range(n - 1, -1, -1):
            # Remove values failing the strict greater condition.
            while candidates and candidates[-1] <= arr[i]:
                candidates.pop()

            # Use the nearest greater candidate at the stack top.
            if candidates:
                answer[i] = candidates[-1]

            candidates.append(arr[i])

        return answer


# Driver code
def main() -> None:
    arr = [2, 1, 2, 4, 3]
    obj = Solution()
    answer = obj.nextGreaterElements(arr)
    print(answer)


if __name__ == "__main__":
    main()

# Time Complexity: O(N), every array value enters the stack once and leaves the stack at most once.

# Space Complexity: O(N), the monotonic stack and returned answer array each use linear space.

