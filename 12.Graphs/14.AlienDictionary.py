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