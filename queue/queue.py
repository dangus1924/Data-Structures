"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def __repr__(self):
        return f"{self.storage}"

    def enqueue(self, item):
        self.size += 1
        return self.storage.insert(0, item)

    def dequeue(self):
        if self.len() < 1:
            return None
        self.size -= 1
        return self.storage.pop()

    def len(self):
        return self.size


q = Queue()

q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
print(q)