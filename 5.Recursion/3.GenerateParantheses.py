# Problem Statement: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input:
#  n = 3
# Output:
#  ["((()))", "(()())", "(())()", "()(())", "()()()"]

# Generate all sequences of length 2n.
# For each sequence, use a validator to check conditions.
# Ensure the count of ')' never exceeds '(' at any point.
# At the end of the sequence, the count must be 0.


def is_valid(s):
    balance = 0
    for c in s:
        if c == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def generate_all(curr, n, res):
    if len(curr) == 2 * n:
        if is_valid(curr):
            res.append(curr)
        return
    generate_all(curr + '(', n, res)
    generate_all(curr + ')', n, res)

def generate_parenthesis(n):
    res = []
    generate_all("", n, res)
    return res

def main():
    result = generate_parenthesis(3)
    for s in result:
        print(s)

if __name__ == "__main__":
    main()

# optimal
# Start with an empty string curr = "".
# Initialize counters: open = 0, close = 0.
# If open < n, add '(' and recurse.
# If close < open, add ')' and recurse.
# If curr.length == 2 * n, add it to the result.

def backtrack(curr, open, close, n, res):
    if len(curr) == 2 * n:
        res.append(curr)
        return
    if open < n:
        backtrack(curr + '(', open + 1, close, n, res)
    if close < open:
        backtrack(curr + ')', open, close + 1, n, res)

def generate_parenthesis(n):
    res = []
    backtrack("", 0, 0, n, res)
    return res

def main():
    result = generate_parenthesis(3)
    for s in result:
        print(s)

if __name__ == "__main__":
    main()