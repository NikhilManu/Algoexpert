"""
Given a Pattern and a string. The Pattern consist only of x and y. Find the substring x and substring y which matches with the string.

Input: string : "gogopowerrangergogopowerranger", pattern : "xxyxxy"
Output : ["go", "powerranger"]  # Here first values denotes x and second value denotes y


Note: Pattern will only continue letters x and y
"""
    

from collections import Counter

def PatternMatcher(string,pattern):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    firstYpos,count = getCountandFirstYpos(newPattern)
    if count['y'] != 0:
        for lenx in range(1,len(string)):
            leny = (len(string) - lenx * count['x']) / count['y']
            if leny <= 0 or leny % 1 != 0:
                continue
            leny = int(leny)
            yidx = firstYpos * lenx
            x = string[:lenx]
            y = string[yidx: yidx + leny]
            potentialPattern = map(lambda char: x if char == 'x' else y,pattern)
            if string == ''.join(potentialPattern):
                return [x,y] if not didSwitch else [y,x]
    else:
        lenx = len(string) / count['x'] 
        if lenx % 1 != 0:
            break
        x = string[:lenx]
        potentialPattern = map(lambda char: x,pattern)
        if string == ''.join(potentialPattern):
            return [x,""] if not didSwitch else ["",x]
        
    return []
            
            
def getCountandFirstYpos(pattern):
    count = Counter(pattern)    # Ask the interviewer whether we can use dependencies
    firstYpos = pattern.index('y')
    return count,firstYpos
    

def getNewPattern(pattern):
    newPattern = list(pattern)
    if newPattern[0] == 'x':
        return newPattern
    
    return list(map(lambda char: 'y' if char == 'x' else 'x',newPattern))
    
     
  
