# Given a list of words sorted according to an alien language, return a string containing all unique characters in one valid alien dictionary order.

# Adjacent words reveal ordering rules from the first position holding different characters. A longer word placed before an equal prefix word makes the dictionary invalid. Return an empty string for invalid input or for cyclic ordering rules.

# Example 1
# Input: words = ["wrt", "wrf", "er", "ett", "rftt"]

# Output: "wertf"

# Explanation: Adjacent comparisons give rules w -> e, e -> r, r -> t, and t -> f. One valid order becomes "wertf".

# Example 2
# Input: words = ["abc", "ab"]

# Output: ""

# Explanation: A longer word appears before an equal prefix word, so no valid alien dictionary order exists.

# Approach 1
# The alien dictionary problem can be represented as a directed graph where every unique character forms a node. For every adjacent word pair, the first mismatching characters create a precedence edge from the earlier word’s character to the later word’s character.

# A three-state DFS distinguishes unvisited, active, and processed characters. Reaching an active character confirms a cycle, while adding characters after all outgoing neighbors produces a postorder whose reversal gives a valid alphabet order.

# Algorithm
# Initialize a graph and state map for every unique character, ensuring that characters without precedence relations also appear in the final order.

# Compare every adjacent word pair and return an empty string when a longer earlier word contains the shorter later word as a complete prefix.

# Locate the first mismatching character pair and add one directed edge from the earlier word’s character to the later word’s character.

# Start DFS from every unvisited character, mark the current character active, and return failure upon reaching an active neighbor because a cycle prevents valid ordering.

# After processing all outgoing neighbors, mark the current character finished and append the character to the postorder list.

# Reverse the completed postorder and return the resulting alien alphabet order.

from typing import Dict, List, Set


class Solution:
    # Return a valid alien character order or empty string for invalid data.
    def alienOrder(self, words: List[str]) -> str:
        graph: Dict[str, Set[str]] = {}
        state: Dict[str, int] = {}

        # Create graph node for every character.
        for word in words:
            for symbol in word:
                graph.setdefault(symbol, set())
                state[symbol] = 0

        # Build ordering rules from each adjacent pair.
        for word_index in range(len(words) - 1):
            first = words[word_index]
            second = words[word_index + 1]
            min_length = min(len(first), len(second))

            # Longer word before equal prefix creates invalid order.
            if len(first) > len(second) and first[:min_length] == second:
                return ""

            # First different character gives one directed rule.
            for pos in range(min_length):
                if first[pos] != second[pos]:
                    graph[first[pos]].add(second[pos])
                    break

        order: List[str] = []

        # Run DFS and detect back edge in directed graph.
        def dfs(node: str) -> bool:
            # Active node means cycle in current recursion path.
            if state[node] == 1:
                return False

            # Processed node already has fixed postorder position.
            if state[node] == 2:
                return True

            # Mark node as active before exploring outgoing rules.
            state[node] = 1

            # Visit every character forced after current character.
            for next_char in graph[node]:
                if not dfs(next_char):
                    return False

            # Mark node as processed after all later characters.
            state[node] = 2
            order.append(node)
            return True

        # Start DFS from every unprocessed character.
        for node in list(state.keys()):
            if state[node] == 0:
                if not dfs(node):
                    return ""

        # DFS postorder gives reverse topological order.
        order.reverse()
        return "".join(order)


# Driver code.
def main() -> None:
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    sol = Solution()
    print(sol.alienOrder(words))


if __name__ == "__main__":
    main()

# Complexity Analysis
# Time Complexity: O(C+U+E×log U) with ordered set or TreeSet adjacency, where C, U, and E denote input characters, unique characters, and extracted precedence relations; hash sets reduce the average bound to O(C+U+E).

# Space Complexity: O(U+E), where the graph stores character nodes and precedence edges, while the state map, recursion stack, and answer require O(U) space.

# Approach 2
# Kahn’s Algorithm creates a topological ordering using character indegrees. Every character having indegree 0 has no unresolved precedence requirement and can appear next in the alien alphabet order.

# Processing a character reduces the indegrees of outgoing neighbors. An answer containing fewer than all unique characters indicates a cycle, while ignoring duplicate edges prevents incorrect indegree values.

# Algorithm
# Initialize a graph and indegree map for every unique character, ensuring inclusion of characters having no precedence relations.

# Compare every adjacent word pair and return an empty string for an invalid prefix case involving a longer earlier word and an identical shorter prefix.

# Add an edge only for the first mismatching character pair and increase the destination indegree only when the edge is new.

# Add every character having indegree 0 to a queue, since no preceding character is required.

# Remove characters from the queue, append each character to the answer, and reduce outgoing-neighbor indegrees, adding a neighbor when the indegree becomes 0.

# Return an empty string when the answer contains fewer than U characters; otherwise, return the completed alien alphabet order.

# Note: Multiple valid alien alphabet orders may exist for some inputs. DFS and Kahn’s Algorithm can produce different correct orders as long as every extracted precedence relation is satisfied. An invalid prefix or directed cycle produces an empty string.

from collections import deque
from typing import Dict, List, Set


class Solution:
    # Return a valid alien character order or empty string for invalid data.
    def alienOrder(self, words: List[str]) -> str:
        graph: Dict[str, Set[str]] = {}
        indegree: Dict[str, int] = {}

        # Create graph node and indegree entry for every character.
        for word in words:
            for symbol in word:
                graph.setdefault(symbol, set())
                indegree[symbol] = 0

        # Build directed rules from adjacent sorted words.
        for word_index in range(len(words) - 1):
            first = words[word_index]
            second = words[word_index + 1]
            min_length = min(len(first), len(second))

            # Longer word before equal prefix creates invalid order.
            if len(first) > len(second) and first[:min_length] == second:
                return ""

            # Add one unique edge from first mismatch.
            for pos in range(min_length):
                if first[pos] != second[pos]:
                    if second[pos] not in graph[first[pos]]:
                        graph[first[pos]].add(second[pos])
                        indegree[second[pos]] += 1
                    break

        q = deque()

        # Push all characters without prerequisites.
        for symbol, degree in indegree.items():
            if degree == 0:
                q.append(symbol)

        order: List[str] = []

        # Remove zero-indegree characters level by level.
        while q:
            node = q.popleft()
            order.append(node)

            # Reduce indegree for every dependent character.
            for next_char in graph[node]:
                indegree[next_char] -= 1
                if indegree[next_char] == 0:
                    q.append(next_char)

        # Missing characters in order means cycle.
        if len(order) != len(indegree):
            return ""

        return "".join(order)


# Driver code.
def main() -> None:
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    sol = Solution()
    print(sol.alienOrder(words))


if __name__ == "__main__":
    main()