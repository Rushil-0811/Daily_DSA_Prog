# Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space. Return a string with the words in reverse order, concatenated by a single space.

# Input: s = "welcome to the jungle"
# Output: "jungle the to welcome"
# Explanation: The words in the input string are "welcome", "to", "the", and "jungle". Reversing the order of these words gives "jungle", "the", "to", and "welcome". The output string should have exactly one space between each word.

# brute
# In the brute force method, we manually parse the string to extract words without directly using high-level split functions. The idea is to read through the string character by character, identify sequences of non-space characters as words, store them in a list, and then reverse the list to achieve the desired order. We also need to handle multiple spaces, leading spaces, and trailing spaces, which means ignoring extra spaces while collecting words. Once reversed, we join the words using a single space. This way, the output string has exactly one space between each word and no leading or trailing spaces.
# Initialize an empty list to store words.
# Traverse the string character by character.
# Identify consecutive non-space characters as a word.
# Ignore extra spaces and leading/trailing spaces while collecting words.
# Append each identified word to the list.
# Reverse the list of words.
# Join the reversed list into a single string using a single space.
# Return the resulting string.
class Solution:
    # Function to reverse the order of words in a string
    def reverseWords(self, s: str) -> str:
        # List to store words
        words = []
        
        # Temporary variable to store current word
        word = ""
        
        # Traverse each character in the string
        for ch in s:
            # If not space, add character to word
            if ch != " ":
                word += ch
            # If space and we have collected a word
            elif word:
                # Add word to list
                words.append(word)
                # Reset word
                word = ""
        
        # Add the last word if present
        if word:
            words.append(word)
        
        # Reverse the list of words
        words.reverse()
        
        # Join with single space
        return " ".join(words)

# Driver code
if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverseWords(s))

# optimal
# Instead of splitting into words and then reversing, we can scan the string from right to left and build the output directly. By starting at the end and identifying each word, we can append it to our result string immediately. We skip multiple spaces, handle leading/trailing spaces naturally, and avoid reversing the list separately which removes one extra pass. This reduces unnecessary data movement and avoids building a list to reverse later.
# Initialize an empty result string.
# Set a pointer at the last character of the string.
# While the pointer is within the string:
# Skip all spaces to move to the end of a word.
# Mark the end position of the word.
# Move the pointer backward until a space or start of string is found.
# Extract the word and append it to the result string.
# If result is not empty, add a space before appending the next word.
# Return the result string.
class Solution:
    # Function to reverse the order of words 
    def reverseWords(self, s: str) -> str:
        # Result string
        result = ""
        
        # Pointer starting from end
        i = len(s) - 1
        
        # Traverse from right to left
        while i >= 0:
            # Skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1
            
            # If pointer out of bounds, break
            if i < 0:
                break
            
            # Mark end of word
            end = i
            
            # Move left until space or start
            while i >= 0 and s[i] != " ":
                i -= 1
            
            # Extract the word
            word = s[i + 1:end + 1]
            
            # Add space if result is not empty
            if result != "":
                result += " "
            
            # Append word
            result += word
        
        return result

# Driver code
if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverseWords(s))
