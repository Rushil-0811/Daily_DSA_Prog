# Given two strings, s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# brute
# Using Sorting and Comparison : 

# Sort the smaller string (s1) and each substring of the larger one (s2) of the same length, then directly compare them. If any match occurs, a permutation exists. This works because permutations become identical after sorting.

# 1. Handle Edge Cases
# Check if the length of s1 is greater than the length of s2.
# If it is, then permutation is impossible; return false immediately .

# 2. Sort the first string
# Sort the string s1's characters.
# This arranged version is used as a point of comparison.

# 3. Iterate over the second string
# Extract a substring from s2 that has the same length as s1 for each iteration.
# From the start index (0), loop through string s2 until the length of s2 minus the length of s1.

# 4. Sort and Compare
# Sort every substring that was extracted.
# Compare this substring directly to the sorted version of s1 after sorting.

# 5. Return answer
# Return true right away if the sorted substring ever matches the sorted s1.
# Return false if, after looking through every potential substring, no match is found.

class Solution(object):
   def checkInclusion(self, s1, s2):
       """
       :type s1: str
       :type s2: str
       :rtype: bool
       """
       n, m = len(s1), len(s2)
       if n > m:
           return False
      
       s1_sorted = sorted(s1)


       for i in range(m - n + 1):
           if sorted(s2[i:i + n]) == s1_sorted:
               return True
      
       return False


# better
# Anagram Check Using Character Frequency : 
# Instead of sorting, the algorithm quickly checks if two strings are anagrams using a simple character-counting method. By repeatedly checking every possible window of the same size in the larger string, it identifies whether any permutation of the first string exists in the second string.

# 1. Edge Case
# In a situation when s1 is longer than s2, there can be no permutation.
# If this happens, return false right away.

# 2. Move a window over the longer string
# Iterate through every substring in the longer string s2 that could have length s1.
# Extract the current substring of length m (length of s1) at each stage.

# 3. Determine whether the substring in question is an anagram of s1.
# To effectively look for an anagram:
# Make use of a 26-character frequency array (count).
# Characters in one string are used to calculate increment counts, whereas characters in the other string are used to calculate decrement counts.
# Both strings are anagrams if, after processing, all counts are zero.

# 4. Return the Result
# Return true right away if a substring matches at any point (anagram found).
# Return false if, after examining every potential substring, no match is found.

class Solution(object):
   def isAnagram(self, a, b):
       count = [0] * 26
      
       for c in a:
           count[ord(c) - ord('a')] += 1


       for c in b:
           count[ord(c) - ord('a')] -= 1


       for i in range(26):
           if count[i] != 0:
               return False


       return True


   def checkInclusion(self, s1, s2):
       """
       :type s1: str
       :type s2: str
       :rtype: bool
       """
       n, m = len(s2), len(s1)
       if m > n:
           return False  # Edge case


       for i in range(n - m + 1):
           sub = s2[i:i + m]
           if self.isAnagram(sub, s1):
               return True


       return False

# optimal
# Using Sliding Window with Character Frequency Matching  :
# The idea is to check if any substring of s2 is a permutation of s1 by comparing character frequencies. Instead of checking all substrings from scratch, we use a sliding window of size equal to s1 and track how character counts change as the window moves. If at any point the character frequency in the window matches that of s1, we’ve found a valid permutation. This avoids redundant work and makes the solution efficient.

# 1. Edge Case
# In a situation when s1 is longer than s2, there can be no permutation.
# If this happens, return false right away.

# 2. Initialize Frequency Arrays
# Make two 26-size frequency arrays: one for s1 and one for s2's initial window.
# Every index denotes a character between 'a' and 'z'.

# 3. Populate the Initial Frequency Window 
# Loop through the first n1 characters (s1 length):
# count1 with the s1 character frequency.
# count2 with the first n1 characters' frequency in s2.

# 4. Compare the First Window
# Verify that count1 and the first window (the beginning frequency count of s2) match.
# Return true if they are equal because a permutation has been found.

# 5. Slide the Window Across s2
# Slide the window one character at a time to begin:

# At the window's end, add the new character.
# Take remove the figure from the front that exits the window.
# Adjust the count2 array accordingly.

# Compare counts 1 and 2 after each shift
# Return true if they are the same.
# Return false if, after the loop, no matching window was found.
class Solution(object):
   def checkInclusion(self, s1, s2):
       """
       :type s1: str
       :type s2: str
       :rtype: bool
       """
       n1 = len(s1)
       n2 = len(s2)
       if n1 > n2:
           return False


       count1 = [0] * 26
       count2 = [0] * 26


       for i in range(n1):
           count1[ord(s1[i]) - ord('a')] += 1
           count2[ord(s2[i]) - ord('a')] += 1


       if count1 == count2:
           return True


       j = 0
       for i in range(n1, n2):
           count2[ord(s2[i]) - ord('a')] += 1
           count2[ord(s2[j]) - ord('a')] -= 1
           if count1 == count2:
               return True
           j += 1


       return False