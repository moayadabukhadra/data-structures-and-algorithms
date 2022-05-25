
from data_structures_and_algorithms.tree_intersection.tree_intersection import tree_intersection
from data_structures_and_algorithms.trees.trees import BinarpointerTree,TNode
import unittest

def test_tree_intersections():
    tree = BinarpointerTree()
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node5 = TNode(5)
    node6 = TNode(6)
    node7 = TNode(7) 
    node8= TNode(8)
    tree.root = node7
    node7.left = node3
    node7.right=node6
    node3.left = node1
    node3.right = node2
    node6.left=node4
    node6.right=node5   
    tree2 = BinarpointerTree()
    tree2.root = node3

    actual= tree_intersection(tree,tree2)
    expected=["1","2","3"]
    assert actual==expected

class TestlinkedList(unittest.TestCase):
    def test_edge_case(self):
        tree=BinarpointerTree()
        tree2=BinarpointerTree()
        with self.assertRaises(Exception):
            tree_intersection(tree,tree2)
