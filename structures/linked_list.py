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
        self.lenght += 1
        