class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

################################################ SOLUTION
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
################################################ SOLUTION    

linked_list = LinkedList(5)
linked_list.append(4)
linked_list.append(8)
linked_list.append(2)
linked_list.append(57)
linked_list.append(21)
linked_list.tail.next = linked_list.head
print(linked_list.has_loop()) #returns true

linked_list = LinkedList(5)
linked_list.append(4)
linked_list.append(8)
linked_list.append(2)
linked_list.append(57)
linked_list.append(21)
print(linked_list.has_loop()) #returns false