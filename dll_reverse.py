class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        

    def reverse(self):
        current_node = self.head
        while current_node is not None: #O(n)
            temp_next = current_node.next
            current_node.next = current_node.prev
            current_node.prev = temp_next
            current_node = temp_next
        self.head = self.tail
        self.tail = current_node

my_list = DoublyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)


print('DLL before reverse():')
my_list.print_list()


my_list.reverse()


print('\nDLL after reverse():')
my_list.print_list()
