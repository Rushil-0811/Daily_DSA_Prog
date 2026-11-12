# Given two distinct words startWord and targetWord, along with a list wordList containing unique words of equal length, find the length of the shortest transformation sequence from start word to target word.

# Only one character can change in one move. Every transformed word must exist in wordList. If no valid transformation sequence exists, return 0.

# Example 1
# Input: startWord = "der", targetWord = "dfs", wordList = ["des","der","dfr","dgt","dfs"]

# Output: 3

# Explanation: The shortest valid sequence is der -> dfr -> dfs, so sequence length is 3.

# Example 2
# Input: startWord = "gedk", targetWord = "geek", wordList = ["geek","gefk"]

# Output: 2

# Explanation: One character change converts gedk to geek, so sequence length is 2.

# pproach
# If two words differ by only one character, one word can be transformed into the other in a single move. This relation creates the graph idea: every word becomes a node, and an edge exists between two words if they differ by exactly one character.

# Now the task becomes finding the shortest path from startWord to targetWord in this graph. Since each transformation has the same cost, BFS is used because it explores all shorter sequences before moving to longer ones.

# A hash set stores unused dictionary words for average O(1) lookup. Removing a generated word immediately after discovery prevents duplicate queue entries and repeated processing.

# Algorithm
# Initialize a hash set with all words from wordList and return 0 when targetWord is absent, as no valid sequence can end at the target.

# Add {startWord, 1} to a queue and remove startWord from the set, establishing the first sequence level while preventing rediscovery.

# Continue BFS while the queue contains states and remove the front word with the corresponding sequence length.

# Return the stored sequence length when the removed word equals targetWord, as BFS reaches words in increasing transformation distance.

# For every character position, store the original character and replace the position with each letter from 'a' to 'z', generating every possible one-character transformation.

# For every generated word found in the set, remove the word immediately and enqueue the word with steps+1; restore the original character after processing the position.

# Return 0 when the queue becomes empty without reaching targetWord, indicating that no valid transformation sequence exists.

from collections import deque
from typing import List, Set


class Solution:
    # Return length of the shortest valid transformation sequence.
    def wordLadderLength(
        self, startWord: str, targetWord: str, wordList: List[str]
    ) -> int:
        dictionary: Set[str] = set(wordList)

        # Missing target makes transformation impossible.
        if targetWord not in dictionary:
            return 0

        q = deque()

        # Start word has sequence length one.
        q.append((startWord, 1))
        dictionary.discard(startWord)

        # BFS explores shorter transformations before longer transformations.
        while q:
            word, steps = q.popleft()

            # Reaching target gives minimum sequence length.
            if word == targetWord:
                return steps

            word_chars = list(word)

            # Try changing every position of current word.
            for pos in range(len(word_chars)):
                original = word_chars[pos]

                # Try every lowercase letter at selected position.
                for code in range(ord("a"), ord("z") + 1):
                    word_chars[pos] = chr(code)
                    new_word = "".join(word_chars)

                    # Valid unseen word becomes next BFS state.
                    if new_word in dictionary:
                        dictionary.remove(new_word)
                        q.append((new_word, steps + 1))

                # Restore original character before next position.
                word_chars[pos] = original

        return 0


# Driver code.
def main() -> None:
    startWord = "der"
    targetWord = "dfs"
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    sol = Solution()
    print(sol.wordLadderLength(startWord, targetWord, wordList))


if __name__ == "__main__":
    main()