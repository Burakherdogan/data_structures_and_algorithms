class Node:
    #constructor
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class BinarySearchTree:
    #constructor
    def __init__(self):
        self.root = None
        
    ##########################################
    def insert(self, value): #O(logn)
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    ##########################################
    def contains(self, value): #O(logn)
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False           


                

