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
        self.length = 1
    ##########################################
    def print_list(self): # O(n)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    ##########################################    
    def append(self,value): # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        #return True
    ##########################################    
    def pop(self): #O(n)
        if self.length == 0:
            return None
        if self.length == 1:
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
        self.length -= 1
        return temp # which returns the node that we just removed
    ##########################################
    def prepend(self, value): #O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1     
    ##########################################
    def pop_first(self): #O(1)
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp
    ##########################################
    def get(self, index): #O(n)
        if index < 0 or index >= self.length:
            return  None
        temp = self.head
        for _ in range(index): #you can use '_'
            temp = temp.next
        return temp
    ##########################################
    def set_value(self, index, value): #O(n)
        if self.length == 0:
            return False
        else:
            temp = self.get(index)
            temp.value = value
            return True
    ##########################################
    def insert(self, index, value): #O(n)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
    ##########################################
    def remove(self, index): #O(n)
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        else:
            before = self.get(index - 1)
            temp = before.next
            before.next = temp.next
            temp.next = None
            self.length -=1
            return temp
    ##########################################
    def reverse(self): #O(nw )
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after 
            
                    
            
            