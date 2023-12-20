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
        
