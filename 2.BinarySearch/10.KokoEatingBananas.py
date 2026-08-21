# A monkey Koko is given ‘n’ piles of bananas, whereas the 'ith' pile has ‘a[i]’ bananas. An integer ‘h’ is also given, which denotes the time (in hours) for all the bananas to be eaten.

# Each hour, the monkey chooses a non-empty pile of bananas and eats ‘k’ bananas. If the pile contains less than ‘k’ bananas, then the monkey consumes all the bananas and won’t eat any more bananas in that hour.

# Find the minimum number of bananas ‘k’ to eat per hour so that the monkey can eat all the bananas within ‘h’ hours.

# brute
# The problem is about finding the minimum eating speed such that Koko can finish all bananas within h hours. The extremely naive approach is to check all possible answers from 1 to max(a[]). The minimum number for which the required time is less than or equal to h is our answer.
# Find the largest pile size (max of the array).
# Loop through all possible speeds from 1 to this maximum value.
# For each speed, calculate the total hours needed. For each pile, compute the time as ceil(pile / speed).
# Sum up the hours for all piles.
# If the total hours is less than or equal to the allowed hours, return this speed as the answer.
import math

class Solution:
    # Function to calculate total hours for given speed
    def calculateTotalHours(self, a, hourly):
        totalHours = 0
        for pile in a:
            # Add hours using ceil
            totalHours += math.ceil(pile / hourly)
        return totalHours

    # Function to find minimum eating speed
    def minEatingSpeed(self, a, h):
        # Find maximum pile size
        maxVal = max(a)

        # Try every possible speed
        for i in range(1, maxVal + 1):
            hours = self.calculateTotalHours(a, i)

            # If hours fit within h
            if hours <= h:
                return i
        return maxVal

# Driver code
a = [3, 6, 7, 11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(a, h))

# Time Complexity: O(n * max(a[])), since for each possible speed we go through all the piles.
# Space Complexity: O(1), since the algorithm does not use any additional space or data structures.

# optimal
# The naive method checks every speed, which is slow if the piles are large. But the possible answer space (from 1 to the maximum pile size) is sorted, meaning if a certain speed works, then all higher speeds will also work. This allows us to apply Binary Search on the answer space to efficiently find the minimum speed at which Koko can finish the bananas within the given hours.
# First, identify the largest pile size since the eating speed cannot be more than that.
# Set the search range with the lowest speed as 1 and the highest speed as the maximum pile size.
# Use binary search within this range to check possible speeds.
# At each step, take the middle value as the current speed and calculate how many hours it would take to finish all piles at this speed.
# If the total hours are less than or equal to the allowed hours, this speed is a candidate, so try to see if a smaller speed also works by moving left.
# If the total hours exceed the allowed hours, then the speed is too slow, so move right to try higher speeds.
# Continue this process until the range closes, and the smallest valid speed found will be the answer.
import math

class Solution:
    # Function to calculate total hours at given speed
    def calculateTotalHours(self, piles, speed):
        totalH = 0
        for bananas in piles:
            totalH += math.ceil(bananas / speed)
        return totalH

    # Function to find minimum eating speed
    def minEatingSpeed(self, piles, h):
        # Find maximum element
        maxPile = max(piles)

        # Initialize low and high pointers
        low, high = 1, maxPile
        ans = maxPile

        # Binary search on answer space
        while low <= high:
            mid = (low + high) // 2
            totalH = self.calculateTotalHours(piles, mid)

            # If possible, try smaller speed
            if totalH <= h:
                ans = mid
                high = mid - 1
            # Otherwise, try larger speed
            else:
                low = mid + 1

        return ans

# Driver code
piles = [3, 6, 7, 11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(piles, h))
