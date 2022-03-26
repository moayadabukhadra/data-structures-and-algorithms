import unittest
from stack_and_queue.stack import Stack
import pytest

@pytest.fixture
def stack():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    return stack

"""
pop method tests
"""
def test_stack_pop(stack):
    actual = stack.pop()
    expected= 5
    assert actual==expected

def test_empty_astack_using_pop(stack):
    "before using pop"
    actual = stack.is_empty()
    expected=False
    assert actual == expected
    "after the pop"
    for i in range(0,5):# 5 is number of the nodes in the stack
        stack.pop()
    actual= stack.is_empty()
    expected=True
    assert actual== expected
    


"""
peek method test
"""
def test_stack_peek(stack):
    actual=stack.peek()
    expected= 5
    assert actual == expected

"""
push method tests
"""
def test_stack_push_one_node():
    stack=Stack()
    stack.push(1)
    actual = stack.top.value
    expected= 1
    assert actual==expected

def test_stack_push_multiple_nodes():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.top.value
    expected= 3
    assert actual==expected

"instantiate an empty stack"
def test_instantiate_an_empty_stack():
    stack=Stack()
    actual=stack.is_empty()
    expected=True
    assert actual==expected
    
    


class TestStack(unittest.TestCase):
    """
    to test the excpetions
    """
    def test_pop_from_empty_stack(self):
        stack=Stack()
        with self.assertRaises(Exception):
            stack.pop()
    
    def test_peek_from_empty_stack(self):
        stack=Stack()
        with self.assertRaises(Exception):
            stack.peek()
    


    
    

        




