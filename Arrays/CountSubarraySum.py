# brute
# we will check the sum of every possible subarray and count how many of them are equal to k. To get every possible subarray sum, we will be using three nested loops. The first two loops(say i and j) will iterate over every possible starting index and ending index of a subarray. Basically, in each iteration, the subarray range will be from index i to index j. Using another loop we will get the sum of the elements of the subarray [i…..j]. Among all values of the sum calculated, we will only consider those that are equal to k.

# Note: We are selecting every possible subarray using two nested loops and for each of them, we add all its elements using another loop.
# First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = size of the array).
# Inside the loop, we will run another loop(say j) that will signify the ending index of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).
# After that for each subarray starting from index i and ending at index j (i.e. arr[i….j]), we will run another loop to calculate the sum of all the elements(of that particular subarray).
# After calculating the sum, we will check if the sum is equal to the given k. If it is, we will increase the value of the count.
class Solution:
    # Function to find count of subarrays with sum equal to k
    def subarraySum(self, arr, k):
        # Size of the array
        n = len(arr)

        # Initialize count of subarrays
        count = 0

        # Traverse all possible start indices
        for i in range(n):
            # Traverse all possible end indices from start
            for j in range(i, n):
                # Initialize sum for current subarray
                total = 0

                # Calculate sum of subarray from i to j
                for m in range(i, j + 1):
                    total += arr[m]

                # If sum equals k, increment count
                if total == k:
                    count += 1

        # Return total count of subarrays
        return count


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [3, 1, 2, 4]

    # Target sum
    k = 6

    # Create Solution object
    sol = Solution()

    # Call function and store result
    result = sol.subarraySum(arr, k)

    # Print the count of subarrays
    print("The number of subarrays is:", result)

# better
#  we carefully observe, we can notice that to get the sum of the current subarray we just need to add the current element(i.e. arr[j]) to the sum of the previous subarray i.e. arr[i….j-1]. Assume previous subarray = arr[i……j-1]
# current subarray = arr[i…..j]
# Sum of arr[i….j] = (sum of arr[i….j-1]) + arr[j] This is how we can remove the third loop and while moving j pointer, we can calculate the sum.
# First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = array size).
# Inside the loop, we will run another loop(say j) that will signify the ending index as well as the current element of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).
# Inside loop j, we will add the current element to the sum of the previous subarray i.e. sum = sum + arr[j]. 
# After calculating the sum, we will check if the sum is equal to the given k. If it is, we will increase the value of the count.
class Solution:
    # Function to find count of subarrays with sum equal to k
    def subarraySum(self, arr, k):
        # Size of the array
        n = len(arr)

        # Initialize count of subarrays
        count = 0

        # Traverse all possible start indices
        for i in range(n):
            # Initialize sum for current subarray
            total = 0

            # Traverse all possible end indices from start
            for j in range(i, n):
                # Add current element to sum
                total += arr[j]

                # If sum equals k, increment count
                if total == k:
                    count += 1

        # Return total count of subarrays
        return count


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [3, 1, 2, 4]

    # Target sum
    k = 6

    # Create Solution object
    sol = Solution()

    # Call function and store result
    result = sol.subarraySum(arr, k)

    # Print the count of subarrays
    print("The number of subarrays is:", result)

# optimal
# In this approach, we are going to use the concept of the prefix sum to solve this problem. Here, the prefix sum of a subarray ending at index i simply means the sum of all the elements of that subarray.

# Assume, the prefix sum of a subarray ending at index i is x. In that subarray, we will search for another subarray ending at index i, whose sum equals k. Here, we need to observe that if there exists another subarray ending at index i with sum k, then the prefix sum of the rest of the subarray will be x-k. The below image will clarify the concept:

# Now, for a subarray ending at index i with the prefix sum x, if we remove the part with the prefix sum x-k, we will be left with the part whose sum is equal to k. And that is what we want. Now, there may exist multiple subarrays with the prefix sum x-k. So, the number of subarrays with sum k that we can generate from the entire subarray ending at index i, is exactly equal to the number of subarrays with the prefix sum x-k, that we can remove from the entire subarray.

# That is why, instead of searching the subarrays with sum k, we will keep the occurrence of the prefix sum of the subarrays using a map data structure. 

# In the map, we will store every prefix sum calculated, with its occurrence in a <key, value> pair. Now, at index i, we just need to check the map data structure to get the number of times that the subarrays with the prefix sum x-k occur. Then we will simply add that number to our answer.

# We will apply the above process for all possible indices of the given array. The possible values of the index i can be from 0 to n-1(where n = size of the array)
# First, we will declare a map to store the prefix sums and their counts.
# Then, we will set the value of 0 as 1 on the map.
# Then we will run a loop(say i) from index 0 to n-1(n = size of the array).
# For each index i, we will do the following:
# We will add the current element i.e. arr[i] to the prefix sum.
# We will calculate the prefix sum i.e. x-k, for which we need the occurrence.
# We will add the occurrence of the prefix sum x-k i.e. mpp[x-k] to our answer.
# Then we will store the current prefix sum in the map increasing its occurrence by 1.
class Solution:
    # Function to find count of subarrays with sum equal to k using prefix sums and hashmap
    def subarraySum(self, arr, k):
        # Size of the array
        n = len(arr)

        # Dictionary to store frequency of prefix sums
        prefixSumCount = {}

        # Initialize prefix sum and count of subarrays
        prefixSum = 0
        count = 0

        # Base case: prefix sum 0 has occurred once
        prefixSumCount[0] = 1

        # Traverse through the array
        for i in range(n):
            # Add current element to prefix sum
            prefixSum += arr[i]

            # Calculate the prefix sum that needs to be removed
            remove = prefixSum - k

            # If this prefix sum has been seen before,
            # add its count to the result
            if remove in prefixSumCount:
                count += prefixSumCount[remove]

            # Update the frequency of the current prefix sum
            prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1

        # Return the total count of subarrays
        return count


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [3, 1, 2, 4]

    # Target sum
    k = 6

    # Create Solution object
    sol = Solution()

    # Call function and store result
    result = sol.subarraySum(arr, k)

    # Print the count of subarrays
    print("The number of subarrays is:", result)
