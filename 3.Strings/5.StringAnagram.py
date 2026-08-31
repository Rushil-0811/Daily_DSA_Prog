# Given two strings, check if two strings are anagrams of each other or not.

# Example 1:
# Input: CAT, ACT
# Output: true
# Explanation: Since the count of every letter of both strings are equal.

# brute

# First, check if the lengths of both strings are equal. If not, they can't be anagrams and return false immediately.
# If the lengths match, sort both strings using a built-in sorting algorithm.
# Once sorted, iterate through each character of both strings and compare them one by one.
# If any character mismatch is found, return false.
# If all characters match, return true, confirming that the strings are anagram

def areAnagrams(s1, s2):
    # If lengths are different, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    # Sort both strings
    s1 = sorted(s1)
    s2 = sorted(s2)

    # Compare each character
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True

# optimal
# First, check if the lengths of both strings are equal. If not, return false immediately as they cannot be anagrams.
# Initialize a frequency array of size 26 (for all uppercase English letters) and set all elements to 0.
# Traverse the first string and increment the frequency of each character.
# Traverse the second string and decrement the frequency of each character.
# Finally, check if all elements in the frequency array are zero. If any element is not zero, return false as the characters do not match in frequency.
# If all frequencies are zero, the strings are anagrams and the function returns true.

def areAnagrams(s1, s2):
    # If lengths are different, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    # Frequency array for 26 uppercase English letters
    freq = [0] * 26

    # Count characters in the first string
    for ch in s1:
        index = ord(ch) - ord('A')
        freq[index] += 1

    # Remove characters found in the second string
    for ch in s2:
        index = ord(ch) - ord('A')
        freq[index] -= 1

    # Check if all frequencies are zero
    for count in freq:
        if count != 0:
            return False

    return True
