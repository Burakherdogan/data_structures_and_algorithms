class Node:
    #constructor
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack: #has LIFO
    #constructor
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    ##########################################    
    def print_stack(self): #O(n)
        temp = self.top
        while temp is not None: 
            print(temp.value)
            temp = temp.next
    ##########################################
    def push(self, value): #O(1)
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    ##########################################
    def pop(self): #O(1)
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp