"""
Caesar Cipher Encryptor
Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function
that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet,
where k is the key.
Note that letters should "wrap" around the alphabet;
in other words, the letter z shifted by one returns the  letter a.

Sample Input: "xyz", 2
Sample Output: "zab"
"""

# Solution 1 --->
# Time - O(n)  | Space - O(n)
------------------------
def CaesarCipher(s,key):
    res = []
    key = key % 26
    for i in s:
        unicode = ord(i) + key
        if unicode <= 122:
            res.append(chr(unicode))
        else:
            res.append(chr(96 + unicode % 122 ))
            
    return "".join(res)


# Solution 2 --->
# Time - O(n)  | Space - O(n)
------------------------
def CaesarCipher(s,key):
    res = []
    key = key % 26 
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    for i in s:
        newletter = alpha.index(i) + key
        if newletter <= 25:
            res.append(alpha[newletter])
        else:
            res.append(alpha[-1 + newletter % 25])
            
    return res


    
        
  
