# You are given an array 'arr' of size 'n' which denotes the position of stalls. You are also given an integer 'k' which denotes the number of aggressive cows.
# You are given the task of assigning stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible. Find the maximum possible minimum distance.

# Example 1:
# Input Format:
#  N = 6, k = 4, arr[] = {0,3,4,7,10,9}
# Result:
#  3
# Explanation:
#  The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

# brute
class Solution:
    # Function to check if cows can be placed with min distance d
    def canPlace(self, stalls, cows, d):
        # Place the first cow at the first stall
        count = 1
        lastPos = stalls[0]

        # Try placing remaining cows
        for i in range(1, len(stalls)):
            # If current stall is at least 'd' away from last cow
            if stalls[i] - lastPos >= d:
                # Place a cow here
                count += 1
                lastPos = stalls[i]
            # If all cows placed successfully
            if count >= cows:
                return True
        # Not possible to place all cows
        return False

    # Function to find maximum minimum distance using brute force
    def aggressiveCows(self, stalls, cows):
        # Step 1: Sort stall positions
        stalls.sort()

        # Step 2: Get the maximum possible distance
        maxDist = stalls[-1] - stalls[0]

        # Step 3: Variable to store answer
        ans = 0

        # Step 4: Try all possible distances from 1 to maxDist
        for d in range(1, maxDist + 1):
            # If cows can be placed with distance d
            if self.canPlace(stalls, cows, d):
                # Update answer
                ans = d

        # Step 5: Return the maximum valid distance
        return ans


# Driver code
stalls = [1, 2, 8, 4, 9]
cows = 3
obj = Solution()
print(obj.aggressiveCows(stalls, cows))

# Time Complexity: O(NlogN) + O(N *(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

# optimal
# We use Binary Search to optimize the solution by reducing the answer space in half each time.

# The main idea of Binary Search is to determine which half of the search space can be eliminated based on a specific condition, thus minimizing unnecessary checks.

# The answer space is sorted: 1 to the difference between max and min values. We can divide this space into two parts:

# One containing valid answers.
# The other containing non-viable options.
# Example: For stalls = {1, 2, 8, 4, 9}, the possible distances are shown below:
# Sort the stalls: Arrange the stalls in ascending order.
# Set the search range:
# Start with the smallest possible distance.
# The largest possible distance is the gap between the farthest and nearest stalls.
# Use Binary Search: Repeat the process until the search range is exhausted:
# Pick the middle distance: Test this distance as a possible answer.
# Check if it works:
# If it works: Try to increase the distance to see if a larger one is possible.
# If it doesn’t work: Decrease the distance and test smaller ones.
# Return answer: After exiting the loop, high holds the largest valid distance.
class Solution:
    # Function to check if cows can be placed with distance d
    def canPlace(self, stalls, cows, d):
        # Place first cow at first stall
        count = 1
        lastPos = stalls[0]

        # Loop through stalls
        for i in range(1, len(stalls)):
            # If stall is at least d away from last placed cow
            if stalls[i] - lastPos >= d:
                # Place cow here
                count += 1
                # Update last position
                lastPos = stalls[i]
            # If all cows placed
            if count >= cows:
                return True
        # Could not place all cows
        return False

    # Function to maximize minimum distance
    def aggressiveCows(self, stalls, cows):
        # Sort stalls
        stalls.sort()

        # Define search space
        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0

        # Binary search
        while low <= high:
            # Find mid distance
            mid = (low + high) // 2

            # If placement possible
            if self.canPlace(stalls, cows, mid):
                # Store answer
                ans = mid
                # Try larger distance
                low = mid + 1
            else:
                # Try smaller distance
                high = mid - 1

        # Return result
        return ans


# Driver code
stalls = [1, 2, 8, 4, 9]
cows = 3
obj = Solution()
print(obj.aggressiveCows(stalls, cows))
