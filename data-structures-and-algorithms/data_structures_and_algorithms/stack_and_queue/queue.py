
import queue


class Node :
    def __init__(self,value):
        self.value=value
        self.next=None


class Queue :
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        """
        adds a new node to the back of the queue
        """
        node = Node(value)
        if not self.front :
            self.rear = node 
            self.front = node 
        else:  
            self.rear.next = node 
            self.rear = node 
      
    def dequeue(self) :
        """
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        """
        if self.front==None:
            raise Exception("The queue is empty")
        temp=self.front
        self.front=self.front.next
        temp.next=None
        # print(f"{temp.value} removed from the queue")
        return temp.value

    def is_empty(self):
        """
        Returns: Boolean indicating whether or not the queue is empty
        """
        if self.front==None:
            print("The queue is empty")
        else:
            print("The queue is Not empty")
        return self.front==None

    def peek(self):
        """
        Returns: Value of the node located at the front of the queue
        """
        if self.front==None:
            raise Exception("The queue is empty")
        else:
            print(f"{self.front.value} in the front of the queue")
            return self.front.value

    def size(self):
        """
        return an integer with the number of nodes in the queue
        """
        current_rear=self.rear
        current_front=self.front
        size=0
        while current_front:
            current_front=current_front.next
            size +=1
            if current_rear==current_front:
                size+=1
                break
        print(f"the size of the queue {size}")
        return size


    def DuckDuckGoose(self,k,string):
        if  type(k)!=int or k<1 :
            raise Exception("k value should be an integer and bigger than zero ")
        if len(string)<=1:
            raise Exception("There is only one player")
        players=string.split(",")
        for player in players:
           self.enqueue(player)
        if k ==1  :
            return self.rear.value
        print(players)
        i=1
        while self.front!=self.rear:
            while i!=k:
                temp=self.front.value
                self.dequeue()
                self.enqueue(temp)
                i+=1

            else:
                print(f"{self.dequeue()} was removed")

                i=1
        print(self.front.value)
        return self.front.value        
                






if __name__=='__main__':
    queue =  Queue()
    # queue.enqueue(1)
    # queue.enqueue(2)
    # queue.enqueue(3)
    # queue.enqueue(4)
    # queue.enqueue(5)
    # queue.enqueue(6)
    queue.DuckDuckGoose(5,"A,B,C,D,E")
    # queue.dequeue()
    # queue.peek()
    # queue.size()
    # queue.is_empty()