class Queue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self,item):
        self.queue.append(item)
        print(f"{item} is pushed to queue")
    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        return self.queue.pop(0)
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue[0]
    def Size(self):
        return len(self.queue)
 
queue1 = Queue()
queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)
print(f"Size of the stack1 is {queue1.Size()}")
queue1.peek()
queue2 = Queue()
print(f"Stack2 is empty? {queue2.is_empty()}")
queue2.enqueue(40)
queue2.peek()
