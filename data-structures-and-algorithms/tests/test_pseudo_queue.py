import unittest
from data_structures_and_algorithms.stack_and_queue.pseudo_queue import PseduQueue


def test_enqueue():
    "adding one node to the queue"
    queue=PseduQueue()
    queue.enqueue(1)

    actual= queue.first_stack.top.value 
    expected=1
    assert actual==expected

def test_enqueue_multible_nodes():
    "adding multible nodes to the queue"
    queue=PseduQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.first_stack.top.value #the rear calue of the queue
    expected=1
    assert actual==expected
    "tests that the next node to the top is 2"
    actual=queue.first_stack.top.next.value
    expected=2
    assert actual==expected

def test_dequeue():
    "removing a node from the queue"
    queue=PseduQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    actual=queue.dequeue()
    expected=1
    assert actual==expected

def test_psedu_queue_empty_multible_dequeue():
        "before using dequeue"
        queue=PseduQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        actual=queue.is_empty()
        expected=False
        assert actual == expected
        "after using dequeue"
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        actual=queue.is_empty()
        expected=True
        assert actual == expected
    
def test_pseduo_queue_using_str():
    queue=PseduQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    actual=queue.__str__()
    expected="front --> 1 --> 2 --> 3 --> 4 --> 5 --> rear"
    assert actual==expected
    queue.dequeue()
    actual=queue.__str__()
    expected="front --> 2 --> 3 --> 4 --> 5 --> rear"
    assert actual==expected

    
class TestQueue(unittest.TestCase):
    """
    to test the excpetions
    """
    def test_dequeue_from_empty_queue(self):
        queue=PseduQueue()
        with self.assertRaises(Exception):
            queue.dequeue()

    




