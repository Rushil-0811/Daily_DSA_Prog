# Given a string s and an integer k, return the length of the longest substring that can be changed into a substring containing the same character after replacing at most k characters.

# You can replace any character in the substring with any other uppercase English character.

# Example 1
# Input: s = "ABAB", k = 2

# Output: 4

# Explanation: We can replace both 'A' characters with 'B', or both 'B' characters with 'A'. So the whole string can become one repeating character.

# Brute Force Approach
# In this approach, every possible substring is checked.

# For any substring, we need to decide whether it can be converted into a string having only one repeating character using at most k replacements.

# The best character to keep unchanged is always the character that appears the most in that substring. All other characters need to be replaced.

# So, for a substring:

# replacementsNeeded = length of substring - maximum frequency of any character in that substring

# If replacementsNeeded is less than or equal to k, the substring is valid.

# Algorithm
# Store the string length in n and return 0 when n == 0 or k < 0, because no valid result can be formed in these cases.

# Initialize maxLength = 0 to store the longest valid substring found so far.

# Select every start index and move end from start toward n - 1 so every possible substring can be considered.

# For each range s[start...end], build a frequency array of size 26 and find the highest character frequency in that substring.

# Calculate replacementsNeeded = (end - start + 1) - maxFrequency. If this value exceeds k, break the current end traversal, because extending the same starting position cannot decrease the required number of replacements.

# Otherwise, update maxLength with end - start + 1 and return it after all starting positions are processed.

class Solution:

    # Returns replacements needed
    # for the selected substring.
    def replacements_needed(
        self,
        s: str,
        start: int,
        end: int
    ) -> int:
        frequency = [0] * 26
        max_frequency = 0

        # Count characters in the
        # selected substring.
        for i in range(start, end + 1):
            index = ord(s[i]) - ord("A")
            frequency[index] += 1

            max_frequency = max(
                max_frequency,
                frequency[index]
            )

        length = end - start + 1

        return length - max_frequency

    # Finds the longest substring
    # valid within k replacements.
    def character_replacement(
        self,
        s: str,
        k: int
    ) -> int:
        n = len(s)

        # No valid substring can exist
        # for these input conditions.
        if n == 0 or k < 0:
            return 0

        max_length = 0

        # Try every possible start.
        for start in range(n):

            # Try every possible end
            # for the current start.
            for end in range(start, n):
                needed = self.replacements_needed(
                    s,
                    start,
                    end
                )

                # Further expansion cannot
                # reduce replacements needed.
                if needed > k:
                    break

                max_length = max(
                    max_length,
                    end - start + 1
                )

        return max_length


if __name__ == "__main__":
    s = "AABABBA"
    k = 1

    solution = Solution()

    print(solution.character_replacement(s, k))

# Better Approach
# Instead of counting frequencies again for every substring, we can build the substring while moving toward the right.

# For every starting index, the ending index is expanded one character at a time. While expanding, the frequency array is updated immediately.

# At every step, we also maintain the maximum frequency in the current substring. This helps us quickly calculate how many characters need to be replaced.

# If currentLength - maxFrequency is less than or equal to k, the substring is valid. If it becomes greater than k, we stop expanding for that starting index.

# For the same starting index, adding more characters cannot reduce the number of replacements needed. It can either stay the same or increase. So, once the substring becomes invalid, there is no benefit in expanding it further.

# Algorithm
# The size of the string is stored in n. If n is 0, 0 is returned because an empty string has no substring. If k is negative, 0 is returned because negative replacements are not possible.

# A variable maxLength is initialized with 0 to store the best valid substring length found so far.

# The string is traversed using start as the starting index. For every start, a frequency array of size 26 is created to track character counts in the current substring.

# The end pointer moves from start to the end of the string. For every s[end], its frequency is increased because this character is now included in the current substring.

# The maxFrequency value is updated using the frequency of s[end]. This value tells us the count of the character that appears most often in the current substring.

# The current length is calculated as end - start + 1, and replacementsNeeded is calculated as currentLength - maxFrequency. If replacementsNeeded is greater than k, the loop is stopped for this start. Otherwise, maxLength is updated. After all starting positions are checked, maxLength is returned.

class Solution:

    # Expands from every start
    # while maintaining frequencies.
    def character_replacement(
        self,
        s: str,
        k: int
    ) -> int:
        n = len(s)

        # No valid substring can exist
        # for these input conditions.
        if n == 0 or k < 0:
            return 0

        max_length = 0

        # Try every possible start.
        for start in range(n):
            frequency = [0] * 26
            max_frequency = 0

            # Expand the substring
            # one character at a time.
            for end in range(start, n):
                index = ord(s[end]) - ord("A")
                frequency[index] += 1

                max_frequency = max(
                    max_frequency,
                    frequency[index]
                )

                current_length = (
                    end - start + 1
                )

                replacements_needed = (
                    current_length - max_frequency
                )

                # Further expansion cannot
                # reduce replacements needed.
                if replacements_needed > k:
                    break

                max_length = max(
                    max_length,
                    current_length
                )

        return max_length


if __name__ == "__main__":
    s = "AABABBA"
    k = 1

    solution = Solution()

    print(solution.character_replacement(s, k))

# Optimal Approach
# The optimal approach uses sliding window.

# The window represents the current substring that we are trying to convert into one repeating character.

# For a window to be valid, the number of characters that need replacement must be at most k.

# The best character to keep unchanged is the one with the maximum frequency inside the window. So:

# replacementsNeeded = window length - maxFrequency

# If replacementsNeeded becomes greater than k, the window is too large and must be adjusted from the left.

# A small optimization is used here: instead of shrinking the window repeatedly using a while loop, we shrink it by one position using an if condition. This works because the goal is to maintain the largest possible window size. When the window becomes invalid, adding one character from the right and removing one character from the left prevents the window from growing incorrectly.

# The maxFrequency value is not recomputed while shrinking. It may sometimes represent an older maximum frequency, but that is fine because it never causes us to miss the best answer. It helps maintain the maximum possible window length efficiently.

# Algorithm
# The size of the string is stored in n. If n is 0, 0 is returned because there is no substring. If k is negative, 0 is returned because negative replacements are not valid.

# A frequency array of size 26 is created to count characters inside the current window. Since the string contains uppercase English letters, a fixed-size array is enough.

# Three variables are initialized: left is set to 0 to mark the left boundary of the window, maxFrequency is set to 0 to store the highest character frequency seen while expanding, and maxLength is set to 0 to store the best answer.

# The right pointer moves from 0 to n - 1. For every s[right], its frequency is increased because this character is now included in the window.

# The maxFrequency value is updated using the frequency of s[right]. This represents the count of the most frequent character seen in the current expanding process.

# The current window length is calculated as right - left + 1. If currentLength - maxFrequency becomes greater than k, the window needs more replacements than allowed. So, the frequency of s[left] is decreased and left is moved one step forward.

# After the window is adjusted, the current window length is calculated again and maxLength is updated if this length is greater. After the traversal ends, maxLength is returned.

class Solution:

    # Uses a sliding window
    # with character frequencies.
    def character_replacement(
        self,
        s: str,
        k: int
    ) -> int:
        n = len(s)

        # No valid substring can exist
        # for these input conditions.
        if n == 0 or k < 0:
            return 0

        frequency = [0] * 26

        left = 0
        max_frequency = 0
        max_length = 0

        # Expand the window with right.
        for right in range(n):
            index = ord(s[right]) - ord("A")
            frequency[index] += 1

            max_frequency = max(
                max_frequency,
                frequency[index]
            )

            current_length = (
                right - left + 1
            )

            # Shrink once when the window
            # needs too many replacements.
            if current_length - max_frequency > k:
                left_index = (
                    ord(s[left]) - ord("A")
                )

                frequency[left_index] -= 1
                left += 1

            # Measure the adjusted
            # window after possible shrinking.
            current_length = (
                right - left + 1
            )

            max_length = max(
                max_length,
                current_length
            )

        return max_length


if __name__ == "__main__":
    s = "AABABBA"
    k = 1

    solution = Solution()

    print(solution.character_replacement(s, k))
    