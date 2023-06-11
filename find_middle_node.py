#WITHOUT using the length attribute.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
######################################### SOLUTION   
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow.value #this will give us value
######################################### SOLUTION    

linked_list = LinkedList(4)
linked_list.append(30)
linked_list.append(2)
linked_list.append(422)
linked_list.append(3)

print(linked_list.find_middle_node())