"""
Min Stack 
          ---[Name of these Qns in Leetcode]
Max Stack
"""
"""

Construct a Stack which has function 
1. push
2. pop
3. peek or Top
4. min
5. max

All these Operations should be in O(1) Time 

"""
# Solution ---> AlgoExpert Solution
# O(1) Time and Space for all Funtion
---------------------------------------
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minmax = []
        
    
    def push(self, val):
        newminMax = { 'min' : val, 'max': val }
        if len(self.minmax):
            lastminMax = self.minmax[-1]
            newminMax['min'] = min(val, lastminMax['min'])
            newminMax['max'] = min(val, lastminMax['max'])
        self.minmax.append(newminMax)
        self.stack.append(val)
        
    def pop(self):
        self.minmax.pop()
        return self.stack.pop()
        
    
    def peek(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minmax[-1]['min']
    
    def getMax(self):
        return self.minmax[-1]['max']
    
      
  
