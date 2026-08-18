# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
# The main idea is to combine intervals that overlap with each other. To do this easily, we first sort the intervals by their starting point so that all overlapping intervals come next to each other. Then, for each interval, we try to see if the next ones overlap with it. If they do, we merge them into one bigger interval. We keep doing this until we find a non-overlapping interval, and then start the process again from that point.
# Sort all intervals based on their starting points. This helps bring all overlapping intervals next to each other.
# Go through each interval one by one and if the current interval is already covered by a previously merged interval, skip it. Else, pick the current interval as the starting point of a new merged interval.
# Now run another loop to check if the following intervals overlap with the current one
# If the start of next interval is less than or equal to the end of the current merged interval, it means they overlap. Therefore, extend the end of the merged interval to be the maximum of the two ends.
# Keep doing this for the next intervals as long as they overlap. As soon as you find an interval that doesn't overlap, break the inner loop and move back to the outer loop to process the next non-overlapping interval.
# Store each merged interval in the final answer list and after the loop ends, return the list of merged intervals.
from typing import List

class Solution:
    # Function to merge overlapping intervals using brute force
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort the intervals based on the start time
        intervals.sort()

        ans = []
        n = len(intervals)
        i = 0

        # Loop through each interval
        while i < n:
            # Take current interval's start and end
            start = intervals[i][0]
            end = intervals[i][1]

            j = i + 1

            # Merge with all intervals that overlap
            while j < n and intervals[j][0] <= end:
                # Extend the end if overlapping
                end = max(end, intervals[j][1])
                j += 1

            # Append merged interval to result
            ans.append([start, end])

            # Move to the next non-overlapping interval
            i = j

        return ans

# Driver code
sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals))

# optimal
# Imagine laying intervals out on a number line. If two intervals overlap, we can combine them into one, like merging blocks that touch or overlap.

# Instead of checking each interval with every other one (as in brute-force), we first sort the intervals, so that any overlapping intervals will come one after the other. This way, we only need to compare each interval with the last one added to our answer. If they overlap, we merge them. If they don’t, we simply add the current interval as a new entry.
# Sort the intervals based on their starting points. This ensures overlapping intervals come together.
# Initialize an empty list to store the final merged intervals.
# If the list is empty or the current interval starts after the last one ends, it means there is no overlap, so just add it to the list.
# If the current interval starts before or exactly at the end of the last one, it means there is overlap. So, combine both by extending the end of the last one to the further end of the two.
# Keep doing this until all intervals have been checked. The final list will now contain only non-overlapping, merged intervals. 
from typing import List

class Solution:
    # Function to merge overlapping intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start time
        intervals.sort()

        # List to store final merged intervals
        merged = []

        # Traverse all intervals
        for interval in intervals:
            # If merged list is empty or current interval doesn't overlap
            if not merged or merged[-1][1] < interval[0]:
                # Append current interval as a new one
                merged.append(interval)
            else:
                # Overlapping: merge by extending the end
                merged[-1][1] = max(
                    merged[-1][1],
                    interval[1]
                )

        return merged

# Example usage
sol = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(sol.merge(intervals))
