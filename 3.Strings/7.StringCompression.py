# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# only one method, optimal method
# two pointer string compression
# We traverse the array while grouping consecutive repeating characters. We save the character for each group and write its count immediately after it if it appears more than once. We update the array in-place using two pointers, one for writing and one for reading. We can handle the final group without any additional requirements by including a dummy character at the end
# At the end of the array, we add a temporary character, such as `'~'`.
# This eliminates the need for further code after the loop and allows us to understand   when we've reached the end of the final set of repeating characters.
# `i` - The i pointer indicates where to put the array's next character or count.
# `j` - The j pointer reads, which is used to traverse the array from beginning to end.
# `count` - Indicates the number of consecutive appearances of the current character.
# Loop through the array starting from index 1:
# If chars[j] is equal to chars[j - 1], it means the current character is repeating, so we   increase the count.
# If it's differ, a group of the same characters has come to an end:
# Write the previous character (chars[j - 1]) at position i, then move i forward.
# If count is more than 1, Convert the number to a string (e.g., 12 becomes "1", "2"), and write each digit into the array.
# Update i after each digit is written.
# Reset count to 1, since a new character group has started.
# The length of the compressed array is contained in i when the loop is finished.
# Return this value (i).
class Solution:
   def compress(self, chars):
       chars.append('~')
       n = len(chars)
       i = 0
       count = 1


       for j in range(1, n):
           if chars[j] == chars[j - 1]:
               count += 1
           else:
               chars[i] = chars[j - 1]
               i += 1
               if count >= 2:
                   for c in str(count):
                       chars[i] = c
                       i += 1
               count = 1
       return i

