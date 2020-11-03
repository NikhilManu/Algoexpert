"""
-----------------
Palindrome Check
-----------------
Write a function that takes in a non-empty string and that returns a boolean representing whether the string
is a palindrome.
A palindrome is defined as a string that's written the same forward and backward. Note that single-character
strings are palindromes.

Sample Input: "abcdcba"
Sample Output: true
"""

# Solution 1 --->
# Time - O(n^2)  |  Space - O(n)
---------
def isPalindrome(s):
    rev = ''
    for i in reversed(range(len(s))):
        rev += s[i]
    return rev == s

# Solution 2 --->
# Time - O(n)  |  Space - O(n)
---------
def isPalindrome(s):
    rev = []
    for i in reversed(range(len(s))):
        rev .append(s[i])
    return ''.join(rev) == s


# Solution 3 --->
# Time - O(n)  |  Space - O(n)
---------
def isPalindrome(s,i=0):
    j = len(s) - 1 - i
    return True if i >= j else s[i] == s[j] and isPalindrome(s,i+1)


# Solution 4 --->
# Time - O(n)  |  Space - O(1)
---------
def isPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        i += 1
        r -= 1
    return False

  
