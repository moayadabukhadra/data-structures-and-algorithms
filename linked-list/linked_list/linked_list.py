
from unittest import result


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
        """
        this function inserts a node in the linked list after the node of the value in the arguments (old data)
        """
        
        new_node = Node(new_data)
        temp = self.head
        while(temp):

            if temp.data == old_data:
                new_node.next = temp.next
                temp.next = new_node
                return 0  
            temp = temp.next
        if temp is None:
            print("the value is not in the linked list")
            return "the value is not in the linked list"
           
    def insert_before_another(self,old_data,new_data):
        """
        this function inserts a node in the linked list before the node of the value in the arguments (old data)
        """
        new_node = Node(new_data)
        old_data=Node(old_data)
        temp = self.head
        if temp.data == old_data.data:
            new_node.next=temp
            self.head=new_node
            
        else:
            while(temp):
                if temp.next is None:
                    print("the value is not in the linked list")
                    return "the value is not in the linked list"
                
                if temp.next.data == old_data.data:
                    new_node.next = temp.next
                    temp.next = new_node
                    return 0
                
                temp = temp.next
            


    def kthFromEnd(self, k):
        """
        Return the node's value that is k places from the tail of the linked list.
        """
        temp = self.head
        length = 0
        try:
            while temp.next is not None:
                temp = temp.next
                length += 1
            temp = self.head
            if k>length:
                print("Location is greater than the length of LinkedList")
                return "Location is greater than the length of LinkedList"
            else:
                for i in range(0, length - k):
                    temp = temp.next
                print(temp.data)
                return temp.data
        except:
                print("the index should be a positive integer value")
                raise ValueError("the index should be a positive integer value")
            
            





    

                
       


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
        """
        this function add's a node at the end of the linked list
        """
        new_node=Node(node)
        if self.head is None:
            self.head = new_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        


    
    def delete(self, data):
        """
        this function takes a value for a node in the linked list and deletes it 
        """
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
            print("the value is not in the linked list")
            return("the value is not in the linked list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
    def zip_lists(self,list1,list2):
        current1=list1.head
        current2=list2.head
        if current1==None:
            return list2
        if current2==None:
            return list1
        if current1 ==None and current2==None:
            print("the two lists are empty")
            raise Exception("the two lists are empty")
        new_list=LinkedList()
        current3=new_list.head
        current3=current1
        current3.next=current2
        current1=current1.next
        current2=current2.next
        new_list.__str__
        return new_list
    
    def zip_lists(self,list1, list2):
        """
        this function takes two list as input and returns a new list of the two list zipped together 
        """
        if list1.head ==None and list2.head==None:
            "if both of the lists is empty"
            print("both lists Can't be empty")
            raise Exception("both lists Can't be empty")
        "if one of the lists is empty"
        if list1.head == None and list:
            return list2
        elif list2.head == None:
            return list1
        new_list = LinkedList()
        current1 = list1.head
        current2 = list2.head
        while current1 or current2:
            if current1:
                new_list.append(current1.data)
            if current2:
                new_list.append(current2.data)
            if current1 and current1.next:
                current1 = current1.next
            else:
                current1 = False
            if current2 and current2.next:
                current2 = current2.next
            else:
                current2 = False
        new_list.__str__()
        return new_list
    
    def palindrome(self):
        "this function checks if the linked list is palindrome returns true else returns False"
        temp=self.head
        tail=self.head
        check_list=[] 
        if self.head==None:
            #if the linked list was empty
            raise Exception("the list is empty")
        while tail:
            check_list.append(tail.data) #appends the linked list values to a normal list 
            tail=tail.next
        # print(check_list)
        while temp!=None:
            popped= check_list.pop() #takes an element from the end of the check list 
        # to compare it with the first one and delets it 
            if popped == temp.data:
                result= True
            else:
                result=False
                print(result)
                return False
            temp=temp.next
        print(result)
        return result
    


    def palindrome_two(self):
        "without using built in functions"
        "this function checks if the linked list is palindrome returns true else returns False"
        temp=self.head
        tail=self.head
        check_list=[] 
        if self.head==None:
            #if the linked list was empty
            raise Exception("the list is empty")
        while tail:
            check_list+=[tail.data] #appends the linked list values to a normal list 
            tail=tail.next
        print(check_list)
        l=len(check_list)
        i=0
        for i in range(len(check_list)):

            if check_list[l-1] == temp.data:
                result= True
            else:
                result=False
                print(result)
                return False
            temp=temp.next
            l-=1
        print(result)
        return result

        
                
            
    



        
    
       




if __name__=="__main__":
    ll1=LinkedList()
    ll1.insert("m")
    ll1.insert("o")
    ll1.insert("a")
    ll1.insert("y")
    ll1.insert("a")
    ll1.insert("d")
    # ll1.insert("a")
    # ll1.insert("t")
    ll1.__str__()
    ll2=LinkedList()
    ll2.insert("m")
    ll2.insert("o")
    ll2.insert("a")
    ll2.insert("o")
    ll2.insert("o")
    ll2.insert("m")

    ll2.__str__()
    ll1.palindrome_two()
    ll2.palindrome_two()
    ll=LinkedList()
    # ll.zip_lists(ll1,ll2)

