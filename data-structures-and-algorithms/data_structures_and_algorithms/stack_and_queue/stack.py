class Node :
    def __init__(self,value):
        self.value=value
        self.next=None 
        
class Stack :
    def __init__(self):
        self.top = None
        # self.max=None
    def __str__(self):
        """
        returns a string for each node in the stack and which node is it pointing at 
        """
        output = ""
        if self.top is None:
            output = "The Stack is empty"
        else:
            current = self.top
            while(current):
                output+= f'{current.value} --> '
                current = current.next
            
            output+= "None"
        print(output)
        return output

        

    def push(self,value):
        "adds a new node with that value to the top of the stack"
        node = Node(value)
        node.next = self.top
        self.top = node


    def pop(self) :
        """
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        """
        if self.top==None:
            raise Exception("The Stack is empty")
        temp = self.top
        self.top = self.top.next
        temp.next= None

        return temp.value

    def peek(self):
        "This function Returns: Value of the node located at the top of the stack"
        if self.top==None:
            raise Exception("The Stack is empty")
        # print(self.top.value)
        return self.top.value
    
    def is_empty(self):
        """
        this function returns a boolean True if the stack is empty False if Not 
        """
        return self.top == None 
    
    def get_max(self):
        if not self.top:
            raise Exception("The stack is empty")
        max=Stack()
        max.push(self.top.value)
        temp=self.top.next
        
        while temp:
            if type(temp.value)!=int:
                temp=temp.next
                continue
            if temp.value>max.top.value:
                max.pop()
                max.push(temp.value)
            temp=temp.next

        if type(max.top.value)==int:
            print(max.top.value)
            return max.top.value

        elif type(max.top.value)!=int:
            raise Exception("The stack has no numeric values")

        
    def get_max_int(self):
        if not self.top:
            raise Exception("The stack is empty")
        max=self.top.value
        temp=self.top.next
        
        while temp:
            if type(temp.value)!=int:
                temp=temp.next
                continue
            if temp.value>max:
                max=temp.value
            temp=temp.next
        if type(max)==int:
            print(max)
            return max
        elif type(max)!=int:
            raise Exception("The stack has no numeric values")
    
    # def get_max_push(self):
    #     print(self.max)
    #     return self.max









if __name__=='__main__':
    stack=Stack()
    stack.push(5)
    stack.push(2)
    stack.push(10)
    stack.push(5)
    stack.push(5000)
    stack.push(50)
    stack.push(15)
    stack.push(1000)
    # stack.get_max_push()
    # stack.get_max_int()
    # stack.__str__()