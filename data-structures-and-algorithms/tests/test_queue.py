import pytest
import unittest
from data_structures_and_algorithms.stack_and_queue.queue import Queue

@pytest.fixture
def queue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    return queue

"""
enqueue method test
"""
def test_queue_enqueue():
    queue=Queue()
    queue.enqueue(1)
    actual = queue.front.value
    expected= 1
    assert actual==expected

def test_queue_enqueue_multible_nodes():
    "enqueue multiple values into a queue"
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual=queue.front.value
    expected=1
    assert actual==expected
    actual= queue.rear.value
    expected=3
    assert actual==expected

def test_queue_dequeue(queue):
    actual=queue.dequeue()
    expected=1
    assert actual==expected

def test_queue_empty_multible_dequeue(queue):
    " empty a queue after multiple dequeues"
    "before using dequeue"
    actual=queue.is_empty()
    expected=False
    assert actual==expected
    "after using dequeue"
    for i in range(0,queue.size()):
        queue.dequeue()
    actual= queue.is_empty()
    expected=True
    assert actual==expected

def test_instantiate_empty_queue():
    "instantiate an empty queue"
    queue=Queue()
    actual=queue.is_empty()
    expected= True
    assert actual==expected


def test_queue_peek(queue):
    "peek into a queue, seeing the expected value"
    actual=queue.peek()
    expected= queue.front.value
    assert actual==expected

class TestQueue(unittest.TestCase):
    """
    to test the excpetions
    """
    def test_dequeue_from_empty_queue(self):
        queue=Queue()
        with self.assertRaises(Exception):
            queue.dequeue()
    
    def test_peek_from_empty_queue(self):
        queue=Queue()
        with self.assertRaises(Exception):
            queue.peek()

