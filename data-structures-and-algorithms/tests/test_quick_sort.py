from this import d
from quick_sort.quick_sort import quick_sort, Partition, swap
import unittest
def test_quick_sort():
    arr=[8,4,23,42,16,15]
    quick_sort(arr,0,len(arr)-1)
    assert arr == [4, 8, 15, 16, 23, 42]

def test_quick_sort2():
    arr=[20,18,12,8,5,-2]
    quick_sort(arr,0,len(arr)-1)
    assert arr == [-2, 5, 8, 12, 18, 20]

def test_quick_sort3():
    arr=[5,12,7,5,5,7]
    quick_sort(arr,0,len(arr)-1)
    assert arr == [5,5,5,7,7,12]

    
    
   



class TestCase(unittest.TestCase):
    def test_quick_sort_edge_case(self):
        with self.assertRaises(Exception):
            quick_sort(5,1,2)

    def test_quick_sort_edge_case2(self):
        with self.assertRaises(Exception):
            quick_sort([4, 8, 15, 16, 23, 42],"2",3)
        