# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
# Example 1
# Input:
#  str = ["flower", "flow", "flight"]
# Output:
#  "fl"

# The common prefix across all strings must exist between the smallest and largest string when sorted lexicographically.
# Sorting the array helps bring these boundary strings to the extremes.
# By comparing only the first and last strings, we can determine the full common prefix shared by the entire array.
# Character-wise comparison from the beginning allows us to identify where the prefix stops.
# The point at which the characters start differing marks the end of the shared prefix.
# The portion before this mismatch is the longest common prefix among all strings.

class Solution:
    # Returns the longest common prefix from a list of strings
    def longestCommonPrefix(self, strs):
        # Handle empty list case
        if not strs:
            return ""
        
        # Sort the list lexicographically
        strs.sort()
        
        # First string in sorted list
        first = strs[0]
        
        # Last string in sorted list
        last = strs[-1]
        
        # Store the common prefix characters
        ans = []
        
        # Compare characters of first and last string
        for i in range(min(len(first), len(last))):
            # Stop if characters differ
            if first[i] != last[i]:
                return ''.join(ans)
            # Add matching character to result
            ans.append(first[i])
        
        # Return the longest common prefix
        return ''.join(ans)

# Run the function with sample input
if __name__ == "__main__":
    # Create an instance of Solution
    solution = Solution()
    
    # Input list of strings
    input_strs = ["interview", "internet", "internal", "interval"]
    
    # Call the method to find prefix
    result = solution.longestCommonPrefix(input_strs)
    
    # Print the result
    print("Longest Common Prefix:", result)  

# Time Complexity: O(N * log N + M), where N is the number of strings and M is the minimum length of a string. The sorting operation takes O(N * log N) time, and the comparison of characters in the first and last strings takes O(M) time.

# Space Complexity: O(M), as the ans variable can store the length of the prefix which in the worst case will be O(M).