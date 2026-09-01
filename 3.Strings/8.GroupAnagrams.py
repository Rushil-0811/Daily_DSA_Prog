# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Group Same Words
# Imagine you and your friends are playing a game with colorful alphabet blocks. Each of you builds different words using the blocks. One friend builds "listen", another makes "silent", and someone else creates "enlist". At first, they all look like different words, but when you look closely, you realize they’re using the exact same letters, just in a different order. So, you put them in one group and say, “These words are like twins—they're made from the same letters!”

# Then someone builds the word "hello" with a different set of blocks. Since no one else made a word using the same letters, it stays alone in its own group. That’s how grouping anagrams works—putting together words that are made from the same letters, even if they look a little different at first.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams, as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams, as they can be rearranged to form each other.

# # better
# Using Hashing with Sorted Strings as Keys :
# Anagrams are words that have the same characters in a different order. If we sort each word, all anagrams will end up with the same sorted representation. So, by sorting each word and grouping them by this sorted version in a hashmap, we can easily group all anagrams together.

# Initialize a map (or dictionary) where:
# Key = sorted version of the string
# Value = list of original strings that are anagrams of each other.

# Loop through the arr list of strings.
#  For each string, do the following:
#  Store the original string in a temporary variable, str.
#  Sort the string in-place (arr[i]), so all anagrams will have the same sorted form.
#  Use the sorted string as a key in the hashmap, and push the original string (str) into the corresponding list.

# After processing all strings, loop through each entry in the hashmap m.
# Push each value (which is a list of anagrams) into the result ans.

# Return the list of anagram groups.


class Solution(object):
   def groupAnagrams(self, arr):
       """
       :type arr: List[str]
       :rtype: List[List[str]]
       """
       ans = []
       n = len(arr)
      
       from collections import defaultdict
       m = defaultdict(list)
       for i in range(n):
           str_ = arr[i]
           sorted_str = ''.join(sorted(arr[i]))
           m[sorted_str].append(str_)
      
       for group in m.values():
           ans.append(group)
       return ans

# optimal
# Signature Hashing Approach for Anagram Grouping :
# Instead of sorting the word (which takes extra time), this approach builds a frequency signature for each word. Since anagrams have exactly the same character counts, their frequency signature (hash) will also be the same. This allows efficient grouping using constant-time hash comparison.

# Create a function that:
# A frequency array of size 26 is initialized (for lowercase English letters).
# Iterates through the word's characters, increasing the matching frequency array index.
# Utilizing the frequency array, creates a distinct string (hash) by adding a separator (such as $) and counts to make a difference.

# Sort words according to their frequency-based hash using a dictionary or map.
# The key is a word's frequency-based hash.
# The value is a list of words that are anagrams, or share this hash.

# For every word:
# Use the hash function to create its frequency hash.
# To the list mapped to this hash, add the word.

# Go through every entry on the map.
# Groups of anagrams are contained in each entry; compile these groups into a final list or array.

# The end result is a list of lists, with words that are anagrams of one another in each inner list.

class Solution(object):
   def getHash(self, s):
       """
       :type s: str
       :rtype: str
       """
       freq = [0] * 26
       for ch in s:
           freq[ord(ch) - ord('a')] += 1


       hash_str = ""
       for i in range(26):
           if freq[i] != 0:
               hash_str += str(freq[i])
           hash_str += "$"
       return hash_str


   def groupAnagrams(self, strs):
       """
       :type strs: List[str]
       :rtype: List[List[str]]
       """
       from collections import defaultdict
       res = []
       mp = defaultdict(list)


       for i in range(len(strs)):
           key = self.getHash(strs[i])
           mp[key].append(strs[i])


       for group in mp.values():
           res.append(group)


       return res



