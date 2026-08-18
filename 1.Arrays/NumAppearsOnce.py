# better
class Solution:
    # Function to find the element that appears only once using hashing
    def getSingleElement(self, arr):
        n = len(arr)

        # Step 1: Find max value to create hash array
        maxi = max(arr)

        # Step 2: Create and initialize hash list
        hash_arr = [0] * (maxi + 1)

        # Step 3: Count frequency of each number
        for num in arr:
            hash_arr[num] += 1

        # Step 4: Find and return the number that appears once
        for num in arr:
            if hash_arr[num] == 1:
                return num

        return -1  # fallback

# Driver code
arr = [4, 1, 2, 1, 2]
obj = Solution()
ans = obj.getSingleElement(arr)
print("The single element is:", ans)

# optimal u just use xor
class Solution:
    # Function to find the single non-repeating element using XOR
    def getSingleElement(self, arr):
        xorr = 0

        # XOR all elements — duplicates cancel out
        for num in arr:
            xorr ^= num

        return xorr

# Driver code
arr = [4, 1, 2, 1, 2]
obj = Solution()
ans = obj.getSingleElement(arr)
print("The single element is:", ans)
