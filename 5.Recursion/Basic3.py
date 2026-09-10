# Problem Description: Given a string, find all the possible subsequences of the string.

# Use recursion to decide for each character whether to include it or not in the current subsequence. This forms a binary decision tree exploring all combinations.
# Start with an empty subsequence. For each character, recursively make a decision.
# Either include it in the subsequence or exclude it from the subsequence.
# When you reach the end of the string, print the current subsequence.

# Solution class to generate all subsequences using recursion
class Solution:
    # Helper recursive method to generate subsequences
    def helper(self, s, index, current, result):
        # Base case: if index reaches string length, add current subsequence to result
        if index == len(s):
            result.append("".join(current))
            return

        # Exclude current character and recurse
        self.helper(s, index + 1, current, result)

        # Include current character and recurse
        current.append(s[index])
        self.helper(s, index + 1, current, result)

        # Backtrack by removing last character
        current.pop()

    # Method to return all subsequences of string s
    def getSubsequences(self, s):
        # List to store all subsequences
        result = []

        # List to store current subsequence characters
        current = []

        # Start recursion from index 0
        self.helper(s, 0, current, result)

        # Return list of subsequences
        return result

if __name__ == "__main__":
    # Input string
    s = "abc"

    # Create Solution object
    sol = Solution()

    # Get all subsequences
    subsequences = sol.getSubsequences(s)

    # Print all subsequences
    for subseq in subsequences:
        print(f'"{subseq}"')
