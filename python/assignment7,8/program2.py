class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # Add to the end of the queue
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        removed_item = self.items.pop(0)  # Remove from the front
        print(f"Dequeued: {removed_item}")
        return removed_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()

print("Front of the queue:", q.peek())
print("Queue size:", q.size())
