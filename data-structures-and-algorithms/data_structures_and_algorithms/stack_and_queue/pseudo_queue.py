from data_structures_and_algorithms.stack_and_queue.stack import Node, Stack

class PseduQueue:
    def __init__(self):
        self.first_stack=Stack()
        self.sec_stack=Stack()

    def enqueue(self,value):
        "this function adds a node to the queue using a first-in, first-out approach"
        while self.first_stack.top:
            self.sec_stack.push(self.first_stack.pop())
        
        self.first_stack.push(value)

        while self.sec_stack.top:
            self.first_stack.push(self.sec_stack.pop())

   
       

    def dequeue(self):
        "this function removes the node located at the front of the queue"
        # if self.sec_stack.is_empty():
        #     while not self.first_stack.is_empty():
        #         self.sec_stack.push(self.first_stack.pop())
        if self.first_stack.is_empty():
            raise Exception("the queue is empty")
        # print(self.sec_stack.peek().value)
        # return self.sec_stack.pop()
        self.first_stack.pop()

    def is_empty(self):
        "returns a boolean if the queue empty or not"
        print(self.first_stack.is_empty())
        return self.first_stack.is_empty() 

    def __str__(self):
        output="front --> "
        temp=self.first_stack.top
        while temp:
            output+=f"{temp.value} --> "
            temp=temp.next
        output+= "rear"
        print(output)
        return output


    

if __name__=='__main__':
    queue=PseduQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()

    queue.__str__()
    # queue.is_empty()

   

