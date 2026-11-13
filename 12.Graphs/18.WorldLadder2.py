# Given two distinct words startWord and targetWord, along with a list wordList containing unique words of equal length, return all shortest transformation sequences from start word to target word.

# Only one character can change in one move. Every transformed word must exist in wordList. If no valid shortest sequence exists, return an empty list.

# Example 1
# Input: startWord = "der", targetWord = "dfs", wordList = ["des","der","dfr","dgt","dfs"]

# Output: [["der","dfr","dfs"],["der","des","dfs"]]

# Explanation: Both sequences have length 3, and no shorter valid sequence exists.

# Example 2
# Input: startWord = "gedk", targetWord = "geek", wordList = ["geek","gefk"]

# Output: [["gedk","geek"]]

# Explanation: A direct one-character change reaches the target word.

# Approach
# If two words differ by only one character, one word can be transformed into the other in a single move. This relation creates the graph idea: every word becomes a node, and an edge exists between two words if they differ by exactly one character.

# All parents reaching the same word from the preceding level must be preserved. Delaying dictionary removal until a complete level finishes allows multiple shortest parents, while DFS backtracking reconstructs every shortest sequence from the target to the start.

# Algorithm
# Initialize a dictionary set from wordList and return an empty list when targetWord is absent, since no valid sequence can reach the target.

# Initialize the current BFS level with startWord and create a parent map for storing every shortest predecessor of each generated word.

# Before expanding a level, remove all current-level words from the dictionary together, preventing longer revisits while preserving multiple parents discovered within the same level.

# For every current-level word, generate all one-character transformations by replacing each position with letters from 'a' to 'z'.

# For every generated word still present in the dictionary, record the current word as a parent and add the generated word to the next-level set.

# Finish processing the complete level containing targetWord, then stop BFS because all shortest parent relationships have been collected.

# Run DFS from targetWord through the parent map, reverse every path reaching startWord, add each sequence to the answer, and return all sequences.

from collections import defaultdict
from typing import DefaultDict, List, Set


class Solution:
    # Return all shortest transformation sequences.
    def findSequences(
        self, startWord: str, targetWord: str, wordList: List[str]
    ) -> List[List[str]]:
        dictionary: Set[str] = set(wordList)
        answer: List[List[str]] = []

        # Missing target makes transformation impossible.
        if targetWord not in dictionary:
            return answer

        parents: DefaultDict[str, List[str]] = defaultdict(list)
        current_level: Set[str] = {startWord}
        dictionary.discard(startWord)
        found = False

        # BFS builds only shortest-level parent links.
        while current_level and not found:
            next_level: Set[str] = set()

            # Remove all words discovered at current depth together.
            for word in current_level:
                dictionary.discard(word)

            # Expand every word from current BFS level.
            for word in current_level:
                chars = list(word)

                # Try each character position.
                for pos in range(len(chars)):
                    original = chars[pos]

                    # Try every lowercase replacement.
                    for code in range(ord("a"), ord("z") + 1):
                        chars[pos] = chr(code)
                        changed = "".join(chars)

                        # Valid unseen word belongs to next level.
                        if changed in dictionary:
                            next_level.add(changed)
                            parents[changed].append(word)

                            if changed == targetWord:
                                found = True

                    # Restore original character before next position.
                    chars[pos] = original

            current_level = next_level

        # No shortest path was found.
        if not found:
            return answer

        path: List[str] = [targetWord]

        # Build paths from target back to start using parent links.
        def dfs(word: str) -> None:
            # Start word closes one shortest sequence.
            if word == startWord:
                answer.append(path[::-1])
                return

            # Try every parent from previous BFS level.
            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(targetWord)
        return answer


# Driver code.
def main() -> None:
    startWord = "der"
    targetWord = "dfs"
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    sol = Solution()
    print(sol.findSequences(startWord, targetWord, wordList))


if __name__ == "__main__":
    main()