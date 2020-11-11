"""
------------------
LRU Cache [Name of this Qn in LeetCode]
------------------
"""
#Solution  --->
# 
--------
class Node:
    def __init__(self,key,val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self,capacity):
        self.maxsize = capacity
        self.currentSize = 0
        self.cache = {}
        self.head = Node('#','#')   # We create sentinel head  --> Look Below to know what is a sentinel node
        self.tail = Node('#','#')   # We create sentinel tail  --> Look Below to know what is a sentinel node
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].value = value   # Since key already exist in cache we have to only change the value
        else:
            if self.currenSize == self.maxsize:
                LRU = self.tail.prev.key
                self.remove(LRU)
            else:
                self.currentSize += 1
                
            self.cache[key] = Node(key,value)   #  We create new node and also add the key to the cache
        
        self.add(self.cache[key])
        
    def get(self, key):
        if key not in self.cache:
            return None
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].value
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        
    def add(self,node):
        node.prev = self.head
        node.next = self.head.next
        node.prev.next = node
        node.next.prev = node
        
        
"""
Sentinal Node: Sentinal nodes next pointer gives the head of the linked list

So here, sentinal head's next pointer gives head of the linked list 
Similarly, sentinal tail's prev pointer gives the tail of the linked list
"""
