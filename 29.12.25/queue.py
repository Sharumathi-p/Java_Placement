# Queue Implementation in Python

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        item = self.items.pop(0)
        print(f"Dequeued: {item}")
        return item
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.items[0]
    
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements:", self.items)

# Main
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.dequeue()
    q.display()
    print(f"Front element: {q.peek()}")
