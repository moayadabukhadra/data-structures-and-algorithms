


class Node:
    """
    has properties for the "value" stored in the Node, and a pointer to the "next" Node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        "returns the data for a specific node "
        return self.data

    def get_next(self):
        "returns the pointer to the next node"
        return self.next

    def set_next(self, new_next):
        "sets the next attripute for the the new added node"
        self.next = new_next


class LinkedList:
    """
    Implementation for a Singly Linked List
    includes a head property 
    """
    def __init__(self):
        self.head = None

    

    def insert(self, data):
        "inserts a new node to the linked list as the head of the list"
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    
    def includes(self, data):
        "Indicates whether that value exists as a Node value somewhere within the list."
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            print(found)
            return found
        print(found)
        return True


    def insert_after_another(self,old_data,new_data):
        new_node = Node(new_data)
        temp = self.head
        while(temp):
            if temp.data == old_data:
                new_node.next = temp.next
                temp.next = new_node
                return 0
            temp = temp.next

    def insert_before_another(self,old_data,new_data):
        new_node = Node(new_data)
        old_data=Node(old_data)
        temp = self.head
        if temp.data == old_data.data:
            new_node.next=temp
            self.head=new_node
            
        else:
            while(temp):
                try:
                    if temp.next.data == old_data.data:
                        new_node.next = temp.next
                        temp.next = new_node
                        return 0
                except: 
                    return 0
                
                     
                temp = temp.next


    

                
       


    def printList(self):
        values=[]
        temp = self.head
        while (temp):
            values.append(temp.data)
            temp = temp.next
        print(values)
        return values
    def size(self):
        """
        returns the size of the linked list "how many node is in the list"
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        print(count)
        return count


    def __str__(self):
        """
        returns a string for each node in the list and which node is it pointing at 
        """
        output = ""
        if self.head is None:
            output = "Empty linked list"
            print(output)
        else:
            current = self.head
            while(current):
                output+= f'{current.data} --> '
                current = current.next
            
            output+= "None"
        print(output)
        return output

    def append(self, node):
        new_node=Node(node)
        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            print("Data not in list")
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
    
       





ll = LinkedList()
ll.insert("a")
ll.insert("b")
ll.insert("c")
ll.append("moayad")
ll.append(None)
ll.insert_after_another("a", 8)
ll.insert_before_another("moayad",5)
ll.delete("a")

print(ll.head.data)
ll.printList()
ll.__str__()