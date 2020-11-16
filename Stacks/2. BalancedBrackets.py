"""
Valid Parenthesis [Name of this Qn in LeetCode]
"""

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true
"""

# Solution --
# O(N) Time and Space
-------------------------
def BalancedBrackets(string):
    openingBrackets = '{[('
    closingBrackets = '}])'
    matchingBrackets = { '}' : '{', ']' : '[', ')': '('  }
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False

            if stack[-1] != matchingBrackets[char]:
                return False
            else:
                stack.pop()

    return len(stack) == 0
