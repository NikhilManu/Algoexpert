"""
LRU Cache [Name of this Qn in LeetCode]
"""
# Solution ---
------------
class LRUCache:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.cache = {}
        self.currentSize = 0
        self.mostRecent = DoublyLinkedlist()
    
    def get(self,key):
        if key not in self.cache:
            return None
        self.updatemostRecent(self.cache[key])
        return self.cache[key].value
    
    def put(self,key,value):
        if key not in self.cache:
            if self.currentSize == self.maxsize:
                self.removeLeastRecent()
            else:
                self.currentSize += 1
            
            self.cache[key] = Node(key,value)
        else:
            self.cache[key].value = value
            
        self.updatemostRecent(self.cache[key])
    
    def getMostRecentkey(self):
        return self.mostRecent.head.key
    
    def removeLeastRecent(self):
        keytoRemove = self.mostRecent.tail.key
        self.mostRecent.removeTail()
        del self.cache[keytoRemove]
        
    
    def updatemostRecent(self,node):
        self.mostRecent.setHeadto(node)
                          

class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def setHeadto(self,node):
        if self.head == node:
            return
        elif self.head == None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head = node
            self.tail.prev = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBinding()
            self.head.prev = node
            node.next = self.head
            self.head = node
            
    def removeTail():
        if not self.tail:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
            
            
        
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None 
        self.next = None
        
    def removeBinding(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
        
    
  
