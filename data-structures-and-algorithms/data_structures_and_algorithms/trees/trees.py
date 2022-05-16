from platform import node
import queue
from unittest import result
from data_structures_and_algorithms.stack_and_queue.queue import Node, Queue
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

    def tree_max__using_travesals_functions(self):
      
        max_list=self.inOrder_iteration()
        maxi=max(max_list)
        print(maxi)
        return maxi

    def tree_max(self):
 
        if self.root is None:
            raise Exception("The tree is empty")
        max=self.root.value
        current = self.root
        stack = Stack() 
        
        while True:
            if current is not None:

                stack.push(current)
                current = current.left
                if current is not None and type(current.value) is int  and  current.value>max :
                    max=current.value
           
            elif not stack.is_empty():
                current = stack.pop()
                current = current.right
                if current is not None and type(current.value) is int and current.value>max:
                    max=current.value

            else:
                break

        print(max)
        return max
    






        

            

        


class BinarpointerSearchTree(BinarpointerTree):
       
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
    
def breadth_first(tree):
    if not tree.root:
        raise Exception("The tree is empty")
    result=[]
    root=tree.root
    queue=Queue()
    queue.enqueue(root)
    while not queue.is_empty():
        if queue.front.value.left:
            queue.enqueue(queue.front.value.left)
        if queue.front.value.right:
            queue.enqueue(queue.front.value.right)
        dequeued=queue.dequeue()
        result.append(dequeued.value)
    print(result)
    return result

class kNode:
    def __init__(self,value):
        self.value=value
        self.child=[]

class k_ary_Tree:
    def __init__(self):
        self.root=None
    
def fizz_buzz_tree(kTree):
    new_tree=k_ary_Tree()
    if not kTree.root:
        raise Exception("The tree is empty")
    result=[]
    root =kTree.root
    queue=Queue()
    if root.value % 3 ==0 :
        root.value = "Fizz"
    elif root.value % 5 == 0 :
        root.value = "Buzz"
    else : 
        root.value = str(root.value)
    new_tree.root=root
    queue.enqueue(root)
    while not queue.is_empty():
        if queue.front.value.child:
            for node in queue.front.value.child:
                if node.value is not str:
                    if node.value %3 ==0 and node.value%5==0:
                        node.value="Fizz Buzz"
                    elif node.value % 3 == 0:
                        node.value = "Fizz"
                    elif node.value % 5 == 0 :
                        node.value = "Buzz"
                    
                    
                    else : 
                        node.value = str(node.value)
                queue.enqueue(node)
        dequeued=queue.dequeue()
        result.append(dequeued.value)
    print(result)
    
    return root.value



def get_files_Count(dir1,dir2):

    q = Queue()
    q2=Queue()
    
    count = 0 
    count2=0
    q.enqueue(dir1)
    q2.enqueue(dir2)
    while (not q.is_empty() or not q2.is_empty()):
        
            
        if not q.is_empty():
            temp = q.peek()
            q.dequeue()
            if (temp.left != None):
                q.enqueue(temp.left)
            if (temp.right != None):
                q.enqueue(temp.right)
            if (temp.left == None and
                temp.right == None):
                count += 1
        
        if not q2.is_empty():
            temp2=q2.peek()
            q2.dequeue()
            if (temp2.left != None):
                q2.enqueue(temp2.left)
            if (temp2.right != None):
                q2.enqueue(temp2.right)
            if (temp2.left == None and
                temp2.right == None):
                count2 += 1
    print(count==count2)
    return count==count2
 
 
 


                






        

    

if __name__=='__main__':        
    
    node1 =kNode(1)
    node2= kNode(10)
    node3 =kNode(30)
    node4=kNode(12)
    node5=kNode(15)
    node6=kNode(9)
    node7=kNode(70)
    node2.child.append(node5)
    node5.child.append(node6)
    node5.child.append(node7)
    node1.child.append(node2)
    node1.child.append(node3)
    node1.child.append(node4)
    tree=k_ary_Tree()
    tree.root=node1
    fizz_buzz_tree(tree)