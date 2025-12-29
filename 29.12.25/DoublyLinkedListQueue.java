public class Node {
    int data;
    Node next, prev;

    Node(int val) {
        data = val;
        next = prev = null;
    }
}

class DoublyLinkedListQueue {
    Node front, rear;

    void enqueue(int val) {
        Node newNode = new Node(val);
        if (rear == null) {
            front = rear = newNode;
        } else {
            rear.next = newNode;
            newNode.prev = rear;
            rear = newNode;
        }
    }

    void peek() {
        if (front == null) {
            System.out.println("Queue is empty.");
        } else {
            System.out.println("Front element: " + front.data);
        }
    }
}

public class cll {
    public static void main(String[] args) {
        DoublyLinkedListQueue q = new DoublyLinkedListQueue();

        // Case 1: Peek when queue is empty
        q.peek();

        // Case 2: Add some elements and peek
        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);
        q.peek();
    }
}
 {
    
}
