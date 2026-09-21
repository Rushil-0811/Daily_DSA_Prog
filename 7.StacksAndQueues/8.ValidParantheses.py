# A string s containing only the characters (, ), {, }, [ and ] is given. Determine whether all brackets are balanced.

# Every opening bracket must be closed by the same bracket type. Closing brackets must also appear in the correct nested order. Return true for a balanced string and false otherwise.

# Example 1
# Input: s = "{[()]}"
# Output: true
# Explanation: Each opening bracket receives a matching closing bracket in reverse order. The innermost pair () closes first, followed by [], then {}.

# Approach
# The latest opening bracket must be closed first, so the solution needs a data structure that returns the most recently stored bracket.

# A stack follows the Last-In, First-Out rule, making it suitable for this task. Push every opening bracket into the stack. For each closing bracket, check whether the stack top contains the matching opening bracket.

# The string is invalid if the stack is empty or the brackets do not match. After processing all characters, the stack must be empty.

# Algorithm
# Initialize an empty stack to store unmatched opening brackets.

# Traverse every character from left to right.

# When an opening bracket appears:

# Push the bracket onto the stack.

# The latest opening bracket must match the next closing bracket.

# When a closing bracket appears:

# Return false if the stack is empty, because no opening bracket is available for matching.

# Compare the stack top with the required opening bracket.

# Return false if the bracket types do not match.

# Pop the stack when a valid match is found.

# After complete traversal, return true only if the stack is empty, because any remaining opening bracket is unmatched.

class Solution:
    # Checks whether a bracket string is balanced.
    def isBalanced(self, s: str) -> bool:
        st: list[str] = []

        # Every character is processed in original order.
        for ch in s:
            # Opening brackets wait for a future matching close.
            if ch == "(" or ch == "{" or ch == "[":
                st.append(ch)
                continue

            # A closing bracket needs an available opening bracket.
            if len(st) == 0:
                return False

            top_bracket = st[-1]

            # Closing parenthesis must match an opening parenthesis.
            if ch == ")" and top_bracket != "(":
                return False

            # Closing brace must match an opening brace.
            if ch == "}" and top_bracket != "{":
                return False

            # Matching closing and opening square brackets.
            if ch == "]" and top_bracket != "[":
                return False

            # A valid pair is removed from the pending openings.
            st.pop()

        # Balanced strings leave no unmatched opening bracket.
        return len(st) == 0


# Driver code
def main() -> None:
    s = "{[()]}"
    obj = Solution()
    print(str(obj.isBalanced(s)).lower())


if __name__ == "__main__":
    main()