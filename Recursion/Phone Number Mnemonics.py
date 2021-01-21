"""
Letter Combination of Phone Number
"""

"""
Given a string containing digits from 0-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 and 0 maps to itself

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""

# Solution
# O( 4^n * n) Time and Space
-----------------------------

def phoneNumberMnemonics(phoneNumber):
	numberMap = getNumbertoAlpha()
	return getMnemonics(phoneNumber, 0, numberMap, [], [])	

def getMnemonics(phoneNumber, i, numberMap, currentComb, result):
	if i == len(phoneNumber):
		result.append(''.join(currentComb)) 
		return 
	
	for char in numberMap[phoneNumber[i]]:
		currentComb.append(char)
		getMnemonics(phoneNumber, i+1, numberMap, currentComb, result)
		currentComb.pop()
		
	return result
	
	
def getNumbertoAlpha():
	numberMap = {
		'1' : ['1'],
		'2' : ['a','b','c'],
		'3' : ['d','e','f'],
		'4' : ['g','h','i'],
		'5' : ['j','k','l'],
		'6' : ['m','n','o'],
		'7' : ['p','q','r','s'],
		'8' : ['t','u','v'],
		'9' : ['w','x','y','z'],
		'0' : ['0']
	}
	
	return numberMap

