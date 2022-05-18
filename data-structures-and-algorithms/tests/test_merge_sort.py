from merge_sort.merge_sort import Mergesort,Merge
import unittest


def test_Mergesort_reverse():
    arr=[20,18,12,8,5,-2]
    Mergesort(arr)
    actual = arr
    expected=[-2, 5, 8, 12, 18, 20]
    assert actual==expected

def test_Mergesort_few():
    arr=[5,12,7,5,5,7]
    Mergesort(arr)
    actual=arr
    expected=[5, 5, 5, 7, 7, 12]
    assert actual==expected

def test_merge_nearly_few():
    arr=[2,3,5,7,13,11]
    Mergesort(arr)
    actual=arr
    expected=[2,3,5,7,11,13]
    assert actual==expected
    

class TestQueue(unittest.TestCase):
    def test_edge_case_one(self):
        with self.assertRaises(Exception):
            Mergesort("")
    
    def test_edge_case_two(self):
        with self.assertRaises(Exception):
            Mergesort([])