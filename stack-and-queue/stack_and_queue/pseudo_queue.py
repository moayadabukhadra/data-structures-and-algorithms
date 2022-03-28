
from stack_and_queue.stack import Stack

class PseduQueue:
    def __init__(self):
        self.first_stack=Stack()
        self.sec_stack=Stack()
    
    def enqueue(self,value):
        "this function adds a node to the queue using a first-in, first-out approach"
        self.first_stack.push(value)


    
    def dequeue(self):
        "this function removes the node located at the front of the queue which is the top value for the sec stack using a first-in, first-out approach"
        if self.sec_stack.is_empty():
            while not self.first_stack.is_empty():
                self.sec_stack.push(self.first_stack.pop())
        if self.first_stack.is_empty() and self.sec_stack.is_empty():
            raise Exception("the queue is empty")
        return self.sec_stack.pop()

    def is_empty(self):
        "returns a boolean if the queue empty or not"
        print(self.first_stack.is_empty() and self.sec_stack.is_empty())
        return self.first_stack.is_empty() and self.sec_stack.is_empty()


if __name__=='__main__':
    queue=PseduQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.is_empty()

   

