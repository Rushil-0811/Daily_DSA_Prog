# You are given a sorted array ‘arr’ of length ‘n’, which contains positive integer positions of ‘n’ gas stations on the X-axis. You are also given an integer ‘k’. You have to place 'k' new gas stations on the X-axis. You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions. Let 'dist' be the maximum value of the distance between adjacent gas stations after adding k new gas stations. Find the minimum value of ‘dist’
# brute
# First, we will declare an array ‘howMany[]’ of size n-1, to keep track of the number of placed gas stations.
# Next, using a loop we will pick k gas stations one at a time.
# Then, using another loop, we will find the index 'i' where the distance (arr[i+1] - arr[i]) is the maximum and insert the current gas station between arr[i] and arr[i+1] (i.e. howMany[i]++).
# Finally, after placing all the new stations, we will find the distance between two consecutive gas stations. For a particular section, distance = section_length / (number_of_stations_ inserted+1) = (arr[i+1]-arr[i]) / (howMany[i]+1)
# Among all the distances, the maximum one will be the answer.

class GasStationSolver:
    def minimise_max_distance(self, arr, k):
        n = len(arr)
        how_many = [0] * (n - 1)  # Extra stations between each pair

        # Place k gas stations
        for _ in range(k):
            max_section = -1
            max_ind = -1

            # Find segment with maximum section length
            for i in range(n - 1):
                diff = arr[i + 1] - arr[i]
                section_length = diff / (how_many[i] + 1)
                if section_length > max_section:
                    max_section = section_length
                    max_ind = i

            # Add one gas station to the longest section
            how_many[max_ind] += 1

        # Calculate final maximum section length
        max_ans = -1
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            section_length = diff / (how_many[i] + 1)
            max_ans = max(max_ans, section_length)

        return max_ans

# Example usage
arr = [1, 2, 3, 4, 5]
k = 4
solver = GasStationSolver()
ans = solver.minimise_max_distance(arr, k)
print("The answer is:", ans)

# TC
# Time Complexity: O(k*n) + O(n), n = size of the given array, k = no. of gas stations to be placed.

# Space Complexity: O(n-1) as we are using an array to keep track of placed gas station

# better
# In the previous approach, for every gas station, we were finding the index i for which the distance between arr[i+1] and arr[i] is maximum. After that, our job was to place the gas station. Instead of using a loop to find the maximum distance, we can simply use the heap data structure i.e. the priority queue.

# First, we will declare an array ‘howMany[]’ of size n-1, to keep track of the number of placed gas stations and a priority queue that uses max heap.
# We will insert the first n-1 indices with the respective distance value, arrr[i+1]-arr[i] for every index.
# Next, using a loop we will pick k gas stations one at a time.
# Then we will pick the first element of the priority queue as this is the element with the maximum distance. Let’s call the index ‘secInd’.
# Now we will place the current gas station at ‘secInd’(howMany[secInd]++) and calculate the new section length, new_section_length = initial_section_length / (number_of_stations_ inserted+1) = (arr[secInd+1] - arr[secInd]) / (howMany[i] + 1)
# After that, we will again insert the pair into the priority queue for further consideration.
# After performing all the steps for k gas stations, the distance at the top of the priority queue will be the answer as we want the maximum distance.
import heapq

class Solution:
    def minimiseMaxDistance(self, arr, k):
        n = len(arr)
        howMany = [0] * (n - 1)

        # Max-heap using negative values
        pq = []
        for i in range(n - 1):
            dist = arr[i + 1] - arr[i]
            heapq.heappush(pq, (-dist, i))  # Use negative for max-heap

        for _ in range(k):
            negDist, idx = heapq.heappop(pq)
            howMany[idx] += 1

            totalDist = arr[idx + 1] - arr[idx]
            newDist = totalDist / (howMany[idx] + 1)
            heapq.heappush(pq, (-newDist, idx))

        # Return the max distance (negated back)
        return -pq[0][0]

# Example usage
arr = [1, 2, 3, 4, 5]
k = 4
sol = Solution()
print("The answer is:", sol.minimiseMaxDistance(arr, k))

# TC 
# Time Complexity: O(nlogn + klogn), n = size of the given array, k = no. of gas stations to be placed.

# Space Complexity: O(n-1)+O(n-1). The first O(n-1) is for the array to keep track of placed gas stations and the second one is for the priority queue..

# optimal
# First, we will find the maximum distance between two consecutive gas stations i.e. max(dist).
# Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 0 and the high will point to max(dist).
# Now, we will use the ‘while’ loop like this: while(high - low > 10^(-6)).
# Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula: mid = (low+high) / 2.0
# Eliminate the halves based on the number of stations returned by numberOfGasStationsRequired(): We will pass the potential value of ‘dist’, represented by the variable 'mid', to the ‘numberOfGasStationsRequired()' function. This function will return the number of gas stations we can place.
# If result > k: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid).
# Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid).
# Finally, outside the loop, we can return either low or high as their difference is beyond 10^(-6). They both can be the possible answer. Here, we have returned the ‘high’.

class GasStationOptimizer:
    # Function to calculate how many gas stations are needed 
    # if the maximum allowed distance between stations is 'dist'
    def number_of_gas_stations_required(self, dist, arr):
        count = 0  # total number of additional gas stations required
        n = len(arr)

        # Iterate through consecutive station positions
        for i in range(1, n):
            # Calculate how many stations are needed between arr[i-1] and arr[i]
            number_in_between = int((arr[i] - arr[i - 1]) / dist)

            # If the distance divides perfectly, we overcounted by 1,
            # so subtract one extra station
            if (arr[i] - arr[i - 1]) == dist * number_in_between:
                number_in_between -= 1

            count += number_in_between  # accumulate required stations

        return count  # return total number of extra stations needed

    # Function to minimize the maximum distance between gas stations
    def minimise_max_distance(self, arr, k):
        # Binary search between smallest (0) and largest gap in stations
        low = 0
        high = max(arr[i+1] - arr[i] for i in range(len(arr) - 1))

        diff = 1e-6  # precision tolerance for stopping condition

        # Binary search loop until precision is achieved
        while high - low > diff:
            mid = (low + high) / 2.0  # candidate distance
            count = self.number_of_gas_stations_required(mid, arr)

            # If more than k stations are required, increase distance
            if count > k:
                low = mid
            else:
                # Otherwise we can reduce the distance
                high = mid

        return high  # minimum possible maximum distance

# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]  # positions of existing gas stations
    k = 4  # number of additional gas stations allowed

    optimizer = GasStationOptimizer()
    result = optimizer.minimise_max_distance(arr, k)

    print("The answer is:", result)

# tc
# Time Complexity: O(n*log(Len)) + O(n), n = size of the given array, Len = length of the answer space.

# Space Complexity: O(1), as we are using no extra space to solve this problem.