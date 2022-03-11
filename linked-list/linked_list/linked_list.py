
class Node:
    """
    has properties for the "value" stored in the Node, and a pointer to the "next" Node.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
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
    def __init__(self, head=None):
        self.head = head

    

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


    def printLL(self):

        "adds the values of the nodes in the linked list to an array"
        current = self.head
        data=[]
        while(current):
            data.append(current.data)
            current = current.next
        print(data)
        return data

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
   
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insert("c")
    ll.__str__()
    print(ll.head.data)
    ll.printLL()