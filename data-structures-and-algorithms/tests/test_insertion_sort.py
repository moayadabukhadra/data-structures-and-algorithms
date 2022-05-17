from insertion_sort.insertion_sort import insertion_sort
import unittest


def test_insertion_sort_reverse():
    actual=insertion_sort([20,18,12,8,5,-2])
    expected=[-2, 5, 8, 12, 18, 20]
    assert actual==expected

def test_insertion_sort_few():
    actual=insertion_sort([5,12,7,5,5,7])
    expected=[5, 5, 5, 7, 7, 12]
    assert actual==expected

def test_insertion_mearly_few():
    actual=insertion_sort([2,3,5,7,13,11])
    expected=[2,3,5,7,11,13]
    assert actual==expected
    

class TestQueue(unittest.TestCase):
    def test_edge_case_one(self):
        with self.assertRaises(Exception):
            insertion_sort("")
    
    def test_edge_case_two(self):
        with self.assertRaises(Exception):
            insertion_sort([])


