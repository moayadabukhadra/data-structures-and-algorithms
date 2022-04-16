from data_structures_and_algorithms.stack_and_queue.queue import Queue
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

    

if __name__=='__main__':        
    # node1 = TNode(2)
    # node2 = TNode(7)
    # node3 = TNode(5)
    # node4 = TNode(2)
    # node5 = TNode(6)
    # node6 = TNode(9)
    # node7 = TNode(5)
    # node8=TNode(11)
    # node9=TNode(4)
   
    # node1.left=node2
    # node1.right=node3
    # node2.left=node4
    # node2.right=node5
    # node3.right=node6
    # node6.left=node9
    # node5.left=node7
    # node5.right=node8

    tree = BinarpointerTree()
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node5 = TNode(5)
    node6 = TNode(6)
    node7 = TNode(7) 
    node100=TNode(100)
    tree.root = node7
    node7.left = node3
    node7.right=node6
    node3.left = node1
    node3.right = node2
    node6.left=node4
    node6.right=node5 
    node5.right=node100

    

    bs=BinarpointerSearchTree()
    # tree = BinarpointerTree()
    tree.root=node7
    breadth_first(tree)
    # bs.add(1)
    # bs.add(2)
    # bs.add(3)
    # bs.add(4)
    # tree.root = node7
    # tree.pre_order_itiration()
    # bs.add(5)
    # bs.add(6)
    # bs.inOrder_iteration()
   

    # bs.contains(1)
    # bs.inOrder_iteration()
    tree.tree_max()
    print(issubclass(BinarpointerSearchTree,BinarpointerTree))