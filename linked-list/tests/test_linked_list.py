import unittest
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

def test_insert_after_value_not_in_the_list():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    actual=ll.insert_after_another(50,11)
    expected="the value is not in the linked list"
    assert actual==expected

def test_insert_after_last_node():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    ll.insert_after_another(6,100)
    actual=ll.printList()
    expected=[1,2,3,4,5,6,100]
    assert actual== expected

def test_insert_before_value_not_in_linked_list():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    actual=ll.insert_before_another(50,11)
    expected="the value is not in the linked list"
    assert actual==expected

def test_insert_before_the_head_node():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    ll.insert_before_another(1,100)
    actual = ll.printList()
    expected=[100,1,2,3,4,5,6]
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

def test_delete_value_not_in_list():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)

    
    actual=ll.delete(10)
    expected="the value is not in the linked list"
    assert actual==expected

def test_kth_from_end_happy_path():
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    actual=ll.kthFromEnd(4)
    expected = 2
    assert actual==expected

def test_kth_from_end_edge_case():
    "if the index was 0 which is the last node in the linked list"
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    actual=ll.kthFromEnd(0)
    expected=6
    assert actual==expected

def test_kth_from_end_k_bigger_than_length():
    "if k > the length of the list"
    ll=LinkedList()
    data=[1,2,3,4,5,6]
    for el in data:
        ll.insert(el)
    actual=ll.kthFromEnd(10)
    expected="Location is greater than the length of LinkedList"
    assert actual==expected





class TestlinkedList(unittest.TestCase):
    "expcted failure test"
    def test_kth_from_end_expected_failure_two(self):
        ll=LinkedList()
        data=[1,2,3,4,5,6]
        for el in data:
            ll.insert(el)
       
        with self.assertRaises(ValueError):
            ll.kthFromEnd("this is a string")


    def test_linked_list_zip_happy_path(self):
        
        ll1= LinkedList()
        ll1.insert(1)
        ll1.insert(3)
        ll1.insert(5)
        ll2= LinkedList()
        ll2.insert(2)
        ll2.insert(4)
        ll2.insert(6)
        ll=LinkedList()
        
        self.assertEqual(ll.zip_lists(ll1,ll2).__str__(), "1 --> 2 --> 3 --> 4 --> 5 --> 6 --> None")

    def test_linked_list_edge_case(self):
        "if one of the lists is empty it will return the other list"
        ll1= LinkedList()
        ll1.insert(1)
        ll1.insert(3)
        ll1.insert(5)
        ll2= LinkedList()
        ll=LinkedList()
        self.assertEqual(ll.zip_lists(ll1,ll2).__str__(), ll1.__str__())
      
    def test_zip_lists_expected_failure(self):
        ll1= LinkedList()
        ll2= LinkedList()
        ll=LinkedList()
        with self.assertRaises(Exception):
            ll.zip_lists(ll1,ll2)

    def test_zip_lists_if_the_length_is_different(self):
        """
        if one of the lists is bigger than the other the new list will take the nodes in the bigger one 
        after the first one is done
        """
        ll1= LinkedList()
        ll1.insert(1)
        ll1.insert(3)
        ll1.insert(5)
        ll1.insert(7)
        ll1.insert(9)
        ll2= LinkedList()
        ll2.insert(2)
        ll2.insert(4)
        ll2.insert(6)
        ll=LinkedList()
        self.assertEqual(ll.zip_lists(ll1,ll2).__str__,"1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 9 None")



