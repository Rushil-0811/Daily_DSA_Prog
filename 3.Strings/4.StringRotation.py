# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position. For example, if s = "abcde", then it will be "bcdea" after one shift.
# Example 1:
# Input:
#  s = "rotation", goal = "tionrota"
# Output:
#  true
# Explanation:
#  After multiple left shifts on "rotation", we get:
#     1st shift → "otationr"
#     2nd shift → "tationro"
#     3rd shift → "ationrot"
#     4th shift → "tionrota"
#     So the goal string can be obtained by rotating the original string.

# brute

# Start by generating all possible left rotations of the original string using substring slicing and concatenation.
# For each rotated version of the string, compare it with the target (goal) string.
# If a match is found at any point, return true immediately as the goal can be achieved.
# If none of the rotations match the goal string after checking all possibilities, return false.

def rotateString(s, goal):
    # If lengths are different, rotation is impossible
    if len(s) != len(goal):
        return False

    # Generate all possible rotations
    for i in range(len(s)):
        # Left rotation using slicing
        rotated = s[i:] + s[:i]

        # Compare with goal
        if rotated == goal:
            return True

    return False


# optimal
# Double the original string by joining it with itself, creating a new string like s + s.
# Look for the target string goalinside this new doubled string.
# If goal exists within the doubled string, then it's a valid rotation, return true.
# If it's not found, that means the original string cannot be rotated to match goal, return false

def rotateString(s, goal):
    # If lengths are different, rotation is impossible
    if len(s) != len(goal):
        return False

    # Double the original string
    doubled = s + s

    # Check if goal exists in the doubled string
    if goal in doubled:
        return True

    return False
