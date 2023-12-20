class Node:
    #constructor
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    #constructor
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
    def print_list(self): # O(n)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
    def append(self,value): # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght +=1
        #return True    
    def pop(self): #O(n)
        if self.lenght == 0:
            return None
        if self.lenght == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            before = self.head
            while temp.next is not None:
                before = temp
                temp = temp.next
            self.tail = before
            self.tail.next = None
        self.lenght -= 1
        return temp # which returns the node that we just removed