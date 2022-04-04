import unittest
from data_structures_and_algorithms.stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_validate_brackets_one():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected=True
    assert actual ==expected


def test_validate_brackets_two():
    actual = validate_brackets("{}(){}")
    expected=True
    assert actual ==expected

def test_validate_brackets_three():
    actual = validate_brackets("(){}[[]]")
    expected=True
    assert actual ==expected


def test_validate_brackets_fail_one():
    actual = validate_brackets("[({}]")
    expected=(False, "error closing ]. Doesn't match opening (.")
    assert actual ==expected


def test_validate_brackets_fail_two():
    actual = validate_brackets("{}{")
    expected=(False, 'error unmatched opening { remaining.')
    assert actual ==expected

def test_validate_brackets_fail_three():
    actual = validate_brackets("}")
    expected=(False, 'error closing } arrived without corresponding opening.')
    assert actual ==expected


class TestStack(unittest.TestCase):
    def test_empty_str(self):
        with self.assertRaises(Exception):
            validate_brackets("")
    
    def test_input_not_str(self):
        with self.assertRaises(Exception):
            validate_brackets(5)
