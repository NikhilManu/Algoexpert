"""
Restore IP Addresses [ LeetCode ]
"""

"""
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. 
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Input: s = "0000"
Output: ["0.0.0.0"]

Input: s = "1111"
Output: ["1.1.1.1"]

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
"""

# Solution
# O(1) Time and Space
-------------------------
def validIPAddresses(string):
	if len(string) <= 3:
		return []
	
	res = []
	for i in range(1, 4):
		cur = ["", "", "", ""]
		cur[0] = string[:i]
		
		if not valid(cur[0]):
			continue
		
		for j in range(i + 1, i + min(len(string) - i, 4)):
			cur[1] = string[i:j]
			
			if not valid(cur[1]):
				continue
				
			for k in range(j + 1, j + min(len(string) - j, 4)):
				cur[2] = string[j:k]
				cur[3] = string[k:]
				
				if valid(cur[2]) and valid(cur[3]):
					res.append('.'.join(cur))
				
	return res

def valid(val):
	x = int(val)
	if x > 255:
		return False
	
	return len(val) == len(str(x))
