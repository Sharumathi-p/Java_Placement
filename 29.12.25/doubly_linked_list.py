# Doubly Linked List Implementation in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        print("Forward: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        print("Backward: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Main
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)
    dll.display_forward()
    dll.display_backward()
