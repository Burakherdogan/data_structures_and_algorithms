class Node:
    #constructor
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    #constructor
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    ##########################################
    def print_queue(self): #O(n)
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next    
    ##########################################
    def enqueue(self, value):
        new_node = Node(value) #O(1)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    ##########################################
    def dequeue(self): #O(1)
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
        
        
        