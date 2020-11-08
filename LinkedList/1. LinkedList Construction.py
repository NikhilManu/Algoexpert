""" 
LinkedList Construction (doubly LinkedList)
"""

class DoublyLinkedLIst:
    def __init__():
        self.head = None 
        self.tail = None
        
    def sethead(self,node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.InsertBefore(self.head,node)
        
    def setTail(self,node):
        if not self.tail:
            self.head = node
            self.tail = node
            return
        self.InsertAfter(self.tail,node)
    
    def InsertBefore(self,node,nodetoInsert):
        if nodetoInsert == self.head and nodetoInsert == self.tail:
            return 
        self.remove(nodetoInsert)
        nodetoInsert.prev = node.prev
        nodetoInsert.next = node
        if not node.prev:
            self.head = nodetoInsert
        else:
            node.prev.next = nodetoInsert 
        node.prev = nodetoInsert
        
    def InsertAfter(self,node,nodetoInsert):
        if nodetoInsert == self.head and nodetoInsert == self.tail:
            return
        self.remove(nodetoInsert)
        nodetoInsert.prev = node
        nodetoInseert.next = node.next
        if not node.next:
            self.tail = nodetoInsert
        else:
            node.next.prev = nodetoInsert
        node.next = nodetoInsert    
        
    def InsertatPosition(self,pos,nodetoInsert):
        if pos == 1:
            self.sethead(nodetoInsert)
            return
        node = self.head
        curpos = 1
        while not node and curpos != pos:
            node = node.next
            curpos += 1
        if node:
            self.InsertBefore(node,nodetoInsert)
        else:
            self.setTail(nodetoInsert)
        
    
    def removenodeswithValue(self,val):
        node = self.head
        while node:
            nodetoRemove = node
            node = node.next
            if nodetoRemove.val = val:
                self.remove(nodetoRemove)
        
        
    def remove(self,node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removenodebinding(node)
        
    def containsnodewithValue(self,val):
        node = head
        while node and node.val != val:
            node = node.next
            
        return node.val == val
    
    def removenodebinding(self,node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
            
        node.prev = None
        node.next = None




