# Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.

# A substring is a continuous part of a string.

# Return the maximum length of a substring in which the number of distinct characters is less than or equal to k.

# Example 1
# Input: s = "eceba", k = 2

# Output: 3

# Explanation: The longest substring with at most 2 distinct characters is "ece", so the answer is 3.

# Brute Force Approach
# Every pair of start and end indices forms one possible substring. Checking every such range guarantees examination of every possible answer.

# A fresh set can scan the selected range and record distinct characters. A substring remains valid when the set size stays at most k. Complete rescanning keeps the logic direct but repeatedly processes characters belonging to overlapping substrings.

# Algorithm
# Store the string length in n and return 0 when n == 0 or k <= 0, because no non-empty valid substring can exist.

# Initialize maxLength = 0 to store the longest valid substring found so far.

# Select every start index and move end from start toward n - 1, so every possible substring can be examined.

# For each selected range s[start...end], use a fresh set and scan the range to collect its distinct characters.

# If the set size exceeds k, break the current end traversal, because extending the same starting position cannot remove any of the existing distinct characters.

# Otherwise, update maxLength with end - start + 1, then return it after all starting positions are processed.

class Solution:

    # Counts distinct characters
    # inside the selected range.
    def count_distinct(
        self,
        s: str,
        start: int,
        end: int
    ) -> int:
        distinct = set()

        # Scan the selected substring.
        for i in range(start, end + 1):
            distinct.add(s[i])

        return len(distinct)

    # Finds the longest substring
    # with at most k distinct characters.
    def longest_substring_at_most_k_distinct(
        self,
        s: str,
        k: int
    ) -> int:
        n = len(s)

        # No valid non-empty substring
        # can exist in these cases.
        if n == 0 or k <= 0:
            return 0

        max_length = 0

        # Try every possible start.
        for start in range(n):

            # Extend the substring
            # from the current start.
            for end in range(start, n):
                distinct_count = self.count_distinct(
                    s,
                    start,
                    end
                )

                # Further expansion cannot
                # reduce the distinct count.
                if distinct_count > k:
                    break

                max_length = max(
                    max_length,
                    end - start + 1
                )

        return max_length


if __name__ == "__main__":
    s = "eceba"
    k = 2

    solution = Solution()

    print(
        solution.longest_substring_at_most_k_distinct(
            s,
            k
        )
    )

# Complexity Analysis
# Time Complexity: O(N³), where N represents the string length. O(N²) substrings exist, and scanning one selected substring may require O(N) time.

# Space Complexity: O(N), because the set may store every distinct character from one substring.

# Better Approach
# The Brute Force Approach first selects a complete substring and then scans the range separately. A better method builds each substring gradually from a chosen starting index.

# A frequency map records characters during right-side expansion. After the map contains more than k distinct characters, every longer substring from the same start remains invalid because additional characters cannot remove an existing distinct character.

# Algorithm
# Store the string length in n and return 0 when n equals 0 or k <= 0.

# Initialize maxLength with 0 for storing the best valid length found so far.

# Select every start index and create a fresh frequency map, because each starting position begins an independent expansion.

# Move end from start toward n - 1 and increase the frequency of s[end] after adding the current character.

# Stop expansion when the map size exceeds k, because every longer substring from the same start will retain more than k distinct characters.

# Update maxLength with end - start + 1 for every valid expansion, then return maxLength after processing all starting positions.

class Solution:

    # Expands from every start
    # while tracking frequencies.
    def longest_substring_at_most_k_distinct(
        self,
        s: str,
        k: int
    ) -> int:
        n = len(s)

        # No valid non-empty substring
        # can exist in these cases.
        if n == 0 or k <= 0:
            return 0

        max_length = 0

        # Try every possible start.
        for start in range(n):
            frequency = {}

            # Grow the current substring.
            for end in range(start, n):
                current = s[end]

                frequency[current] = (
                    frequency.get(current, 0) + 1
                )

                # Further expansion cannot
                # reduce the distinct count.
                if len(frequency) > k:
                    break

                max_length = max(
                    max_length,
                    end - start + 1
                )

        return max_length


if __name__ == "__main__":
    s = "eceba"
    k = 2

    solution = Solution()

    print(
        solution.longest_substring_at_most_k_distinct(
            s,
            k
        )
    )

# Complexity Analysis
# Time Complexity: O(N²), where N represents the string length. Expansion from every starting position may process many later characters.

# Space Complexity: O(N), because the frequency map may store many distinct characters for a general string.

# Optimal Approach
# Starting a new expansion from every position repeats earlier work. A sliding window keeps one active substring and reuses valid characters from the previous window.

# Pointer right expands the window and explores longer substrings. When the distinct count exceeds k, pointer left removes characters until the window becomes valid again. Character frequencies reveal when a character has completely left the window and should no longer contribute to the distinct count.

# Algorithm
# Store the string length in n and return 0 when n equals 0 or k <= 0.

# Initialize left and maxLength with 0, and create a frequency map for characters inside the current window.

# Move right from 0 to n - 1 and increase the frequency of s[right], because the current character enters the window.

# While the map contains more than k characters, decrease the frequency of s[left], erase a zero-frequency entry, and move left forward.

# Update maxLength with right - left + 1 after restoring validity, because the current window now contains at most k distinct characters.

# Return maxLength after right processes every character.

class Solution:

    # Uses a sliding window
    # with character frequencies.
    def longest_substring_at_most_k_distinct(
        self,
        s: str,
        k: int
    ) -> int:
        n = len(s)

        # No valid non-empty substring
        # can exist in these cases.
        if n == 0 or k <= 0:
            return 0

        frequency = {}

        left = 0
        max_length = 0

        # Expand the window with right.
        for right in range(n):
            current = s[right]

            frequency[current] = (
                frequency.get(current, 0) + 1
            )

            # Shrink until the window
            # has at most k distinct characters.
            while len(frequency) > k:
                left_char = s[left]
                frequency[left_char] -= 1

                # Remove a character only
                # after its last copy leaves.
                if frequency[left_char] == 0:
                    del frequency[left_char]

                left += 1

            max_length = max(
                max_length,
                right - left + 1
            )

        return max_length


if __name__ == "__main__":
    s = "eceba"
    k = 2

    solution = Solution()

    print(
        solution.longest_substring_at_most_k_distinct(
            s,
            k
        )
    )

# Complexity Analysis
# Time Complexity: O(N), where N represents the string length. Pointer right processes every character once, while pointer left moves only forward.

# Space Complexity: O(N), because the frequency map may contain up to N distinct characters for a general character set. A fixed-size character set reduces auxiliary space to O(1).

