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

    def is_palindrome(self):
        if self.length <= 1:
            return True
        end = self.tail
        pre = self.head
        for _ in range(self.length//2): #O(logn)
            if pre.value != end.value:
                return False
            pre = pre.next
            end = end.prev
        return True




my_list = DoublyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(2)
my_list.append(1)

print('my_list is_palindrome:')
print( my_list.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )
