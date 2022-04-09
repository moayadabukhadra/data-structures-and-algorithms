
from unittest import result
from data_structures_and_algorithms.stack_and_queue.stack import Stack

class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarpointerTree:
    def __init__(self):
        self.root = None

    def pre_order_rec(self):
        if self.root is None:
            raise Exception("The tree is empty")
        def _walk(node):
            print(node.value)

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)

    def pre_order_itiration(self):
        result=[]
        if self.root is None:
            raise Exception("The tree is empty")
        stack = Stack()
        current = self.root

        stack.push(current)

        while not stack.is_empty():
            current = stack.pop()
            print(current.value)
            result.append(current.value)

            if current.right:
                stack.push(current.right)

            if current.left:
                stack.push(current.left)
        print(result)
        return result

    def inOrder_iteration(self):
        result=[]
        if self.root is None:
            raise Exception("The tree is empty")
       
        current = self.root
        stack = Stack() 
        
        while True:
            
            
            if current is not None:
               
                stack.push(current)
                current = current.left
    
           
            elif not stack.is_empty():
                current = stack.pop()
                print(current.value)
                result.append(current.value)
                current = current.right
    
            else:
                break
        print(result)
        return result

    def Postorder_rec(self,root):
        if self.root is None:
            raise Exception("The tree is empty")
        if root:

            self.printPostorder(root.left)

            self.printPostorder(root.right)

            print(root.value)


    def postOrder_Iteration(self):
        result=[]
        if self.root is None:
            raise Exception("The tree is empty")
        stack = Stack()
        root=self.root
        while True:
            while root != None:
                stack.push(root)
                stack.push(root)
                root = root.left
    
            if stack.is_empty():
                print(result)
                return result
            
            root = stack.pop()
    
            if (stack.is_empty() is False and stack.peek() == root):
                root = root.right
            else:
                print(root.value)
                result.append(root.value)
                root = None

        


class BinarpointerSearchTree:
    def __init__(self):
        self.root=None
    def postOrder_Iteration(self):
        result=[]
        if self.root is None:
            raise Exception("The tree is empty")
        stack = Stack()
        root =self.root
        while True:
            while root != None:
                stack.push(root)
                stack.push(root)
                root = root.left
    
            if stack.is_empty():
                print(result)
                return result
            
            root = stack.pop()
    
            if (stack.is_empty() is False and stack.peek() == root):
                root = root.right
            else:
                print(root.value)
                result.append(root.value)
                root = None

            
    def add(self, value):
        newnode = TNode(value)
        root = self.root
        pointer = None

        if self.root==None:
            self.root=newnode

        while root:
            pointer = root
            if (value < root.value):
                root = root.left
            else:
                root = root.right
        
        if (pointer == None):
            pointer = newnode
    
        elif (value < pointer.value):
            pointer.left = newnode
    
        else:
            pointer.right = newnode
    
               
    def inOrder(self):
        
        if self.root is None:
            raise Exception("The tree is empty")
        result=[]
        current = self.root
        stack = Stack() 

        while True:

            if current is not None:
                stack.push(current)
                current = current.left

            elif not stack.is_empty():
                current = stack.pop()
                print(current.value)
                result.append(current.value)
                current = current.right

            else:
                break
        print(result)
        return result

    def contains(self,value):

        if self.root is None:
            raise Exception("The tree is empty")

        root=self.root
        while root is not None:
            
            if value == root.value:
                print(True)
                return True
            if root and value>root.value:
                root=root.right

            if root and value< root.value:
                root=root.left
    
        print(False)
        return False
    


    

if __name__=='__main__':        
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node5 = TNode(5)
    node6 = TNode(6)
    node7 = TNode(7)
    
    node7.left = node3
    node7.right=node6
    node3.left = node1
    node3.right = node2
    node6.left=node4
    node6.right=node5
    bs=BinarpointerSearchTree()
    tree = BinarpointerTree()
    bs.add(1)
    bs.add(2)
    bs.add(3)
    bs.add(4)
    tree.root = node7
    tree.pre_order_itiration()
    bs.add(5)
    bs.add(6)
    bs.postOrder_Iteration()
   
    # bs.contains(1)
    bs.inOrder()
   