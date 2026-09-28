# Given a string s consisting only of characters 'a', 'b', and 'c', return the number of substrings that contain at least one occurrence of all three characters.

# A substring is a contiguous part of a string.

# Example 1
# Input: s = "abcabc"

# Output: 10

# Explanation: The substrings containing at least one 'a', one 'b', and one 'c' are counted. There are 10 such substrings.

# Brute Force Approach
# Every possible substring can be checked independently to see whether it contains a, b, and c.

# For each selected range, scan its characters and track whether all three required characters appear. This guarantees that every valid substring is counted, but overlapping ranges are repeatedly scanned.

# Algorithm
# The size of the string is stored in n. If n is less than 3, 0 is returned because a substring containing all three characters cannot exist.

# A helper function is used to check whether a substring from start to end contains all three characters. Inside this helper, three boolean variables are maintained to track whether 'a', 'b', and 'c' are present.

# The helper scans the substring from start to end. Whenever 'a', 'b', or 'c' appears, the corresponding boolean value is marked as true.

# After scanning the substring, the helper returns true only if all three boolean values are true. This means the substring contains at least one occurrence of each required character.

# Two loops are used to generate every possible substring. The first loop chooses the starting index start, and the second loop chooses the ending index end.

# For every substring, the helper is called. If the helper returns true, count is increased by 1. After all substrings are checked, count is returned.

class Solution:

    # Checks whether the selected substring contains a, b, and c.
    def contains_all_three(
        self,
        s: str,
        start: int,
        end: int
    ) -> bool:
        has_a = False
        has_b = False
        has_c = False

        # Scan the complete selected substring.
        for i in range(start, end + 1):
            if s[i] == "a":
                has_a = True
            elif s[i] == "b":
                has_b = True
            elif s[i] == "c":
                has_c = True

        return has_a and has_b and has_c

    # Counts all substrings containing at least one a, b, and c.
    def number_of_substrings(self, s: str) -> int:
        n = len(s)

        # At least three characters are required.
        if n < 3:
            return 0

        count = 0

        # Choose every possible starting position.
        for start in range(n):

            # Choose every possible ending position.
            for end in range(start, n):

                # Count the substring when all three characters exist.
                if self.contains_all_three(s, start, end):
                    count += 1

        return count


if __name__ == "__main__":
    s = "abcabc"

    solution = Solution()

    print(solution.number_of_substrings(s))

# Complexity Analysis
# Time Complexity: O(N³), where N is the length of the string. There are O(N²) possible substrings, and checking each substring can take O(N) time.

# Space Complexity: O(1), because only three boolean variables are used to track the presence of 'a', 'b', and 'c'.

# Better Approach
# Instead of rescanning each substring, fix a starting index and build the range by moving end to the right while maintaining frequencies of a, b, and c.

# Once the first valid range is found, every later ending position for the same start is also valid. Therefore, all n - end such substrings can be counted together.

# Algorithm
# The size of the string is stored in n. If n is less than 3, 0 is returned because no valid substring can exist.

# A variable count is initialized with 0. This stores the total number of substrings that contain all three characters.

# The string is traversed using start as the starting index. For every start, a frequency array of size 3 is created to store the count of 'a', 'b', and 'c' in the current substring.

# The end pointer moves from start to the end of the string. For every s[end], its frequency is increased in the array.

# After adding a character, we check whether the frequencies of 'a', 'b', and 'c' are all greater than 0. If yes, the current substring contains all three characters.

# Once the first valid substring is found for a fixed start, n - end is added to count because every longer substring starting from the same start will also be valid. Then the loop stops for this start. After all starting positions are checked, count is returned.

class Solution:

    # Counts valid substrings by expanding from every starting index.
    def number_of_substrings(self, s: str) -> int:
        n = len(s)

        # At least three characters are required.
        if n < 3:
            return 0

        count = 0

        # Fix every index as a possible starting position.
        for start in range(n):
            frequency = [0] * 3

            # Expand until the first valid substring is found.
            for end in range(start, n):
                frequency[ord(s[end]) - ord("a")] += 1

                # All later endings will also remain valid.
                if (
                    frequency[0] > 0
                    and frequency[1] > 0
                    and frequency[2] > 0
                ):
                    count += n - end
                    break

        return count


if __name__ == "__main__":
    s = "abcabc"

    solution = Solution()

    print(solution.number_of_substrings(s))

# Optimal Approach
# A sliding window reuses the current range instead of restarting from every index. Expand right until the window contains a, b, and c.

# For every valid window [left...right], all n - right substrings beginning at left and ending at right or later are valid. Then move left forward while the window remains valid to count substrings from additional starting positions.

# That keeps the reasoning compact while still explaining why n - right is added and why shrinking works.

# Algorithm
# The size of the string is stored in n. If n is less than 3, 0 is returned because no substring can contain all three characters.

# A frequency array of size 3 is created to store the counts of 'a', 'b', and 'c' inside the current window.

# Two variables are initialized: left is set to 0 to represent the left boundary of the window, and count is set to 0 to store the number of valid substrings.

# The right pointer moves from 0 to n - 1. For every s[right], the corresponding frequency is increased because this character is now included in the current window.

# Whenever the window contains all three characters, it is valid. At this point, n - right is added to count because every substring starting from left and ending from right to n - 1 will also be valid.

# After counting those substrings, s[left] is removed from the frequency array and left is moved one step forward. This shrinking is repeated while the window still contains all three characters. After the traversal ends, count is returned.

class Solution:

    # Counts valid substrings using a sliding window.
    def number_of_substrings(self, s: str) -> int:
        n = len(s)

        # At least three characters are required.
        if n < 3:
            return 0

        frequency = [0] * 3

        left = 0
        count = 0

        # Expand the window by moving the right boundary.
        for right in range(n):
            index = ord(s[right]) - ord("a")
            frequency[index] += 1

            # Shrink while the window contains all three characters.
            while (
                frequency[0] > 0
                and frequency[1] > 0
                and frequency[2] > 0
            ):
                # Every later ending gives another valid substring.
                count += n - right

                left_index = ord(s[left]) - ord("a")
                frequency[left_index] -= 1
                left += 1

        return count


if __name__ == "__main__":
    s = "abcabc"

    solution = Solution()

    print(solution.number_of_substrings(s))