class Node:
    #constructor
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    #constructor
    def __init__(self, value):
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
    def append(self, value): #O(1)
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    ##########################################
    def pop(self): #O(1)
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    ##########################################
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    ##########################################
    def pop_first(self): #O(1)
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    ##########################################
    def get(self, index): # O(logn)
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev 
        return temp
    ##########################################
    def set_value(self, index, value): #O(logn)
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    ##########################################
    def insert(self, index, value): # O(logn)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index)
            new_node.prev = temp.prev
            temp.prev.next = new_node
            temp.prev = new_node
            new_node.next = temp
        self.length += 1
        return True
    ##########################################
    def remove(self, index): #O(logn)
        if index < 0 or index >= self.length:        
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp
    

