
from linked_list.linked_list import LinkedList

def test_empty_linked_list():
    LL=LinkedList()
    actual = LL.size()
    expected=0
    assert actual == expected

def test_insert_to_linked_list():
    LL=LinkedList()
    actual = LL.size()
    expected= 0
    assert actual==expected
    LL.insert(10)
    actual = LL.size()
    expected= 1
    assert actual==expected

def test_head_pointing_to_next_node():
    """
    when inserting a node to the linked list
     the head will be the the new node added to the list and the first element will be (None)

     in the test a node with value 10 inserted to the list
      this node will be the head of the linked list and it will point to the value (None)--> "the first value in the list"
    """
    LL=LinkedList()
    LL.insert(10)
    actual = LL.__str__()
    expected = "10 --> None"
    assert actual==expected

def test_insert_multiple_nodes():
    """
    inserting multiple nodes to the list the new node will be the head for the list 
    the output string will show the order for the nodes in the list when inserting more than one node
    """
    LL=LinkedList()
    LL.insert("first")
    LL.insert("sec")
    LL.insert("3rd")
    actual = LL.__str__()
    expected="first --> sec --> 3rd --> None"
    assert actual==expected

def test_includes_True():
    LL=LinkedList()
    LL.insert(5)
    actual = LL.includes(5)
    expected= True
    assert actual == expected

def test_includes_False():
    LL=LinkedList()
        
    actual = LL.includes(5)
    expected= False
    assert actual == expected

def test_all_values_in_linked_list():
    LL=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        LL.insert(el)
    actual = LL.printList()
    expected=data
    assert actual==expected

def test_delete():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    
    for el in data:
        ll.insert(el)
    ll.delete(3)
    actual=ll.printList()
    expected=[1,2,4,5,6]
    assert actual==expected
    

def test_insert_after():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    
    ll.insert_after_another(5,10)
    actual = ll.printList()
    expected= [1,2,3,4,5,10,6]
    assert actual==expected
    ll.insert_after_another(6,7)
    actual = ll.printList()
    expected=[1,2,3,4,5,10,6,7]
    assert actual==expected

def test_insert_before():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    
    ll.insert_before_another(5,10)
    actual = ll.printList()
    expected= [1,2,3,4,10,5,6]
    assert actual==expected
    ll.insert_before_another(6,7)
    actual = ll.printList()
    expected=[1,2,3,4,10,5,7,6]
    assert actual==expected

def test_append():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    
    ll.append(10)
    actual = ll.printList()
    expected= [1,2,3,4,5,6,10]
    assert actual==expected

