import re
import pytest
import unittest
from data_structures_and_algorithms.trees.trees import BinarpointerSearchTree, BinarpointerTree , TNode,breadth_first,fizz_buzz_tree,kNode,k_ary_Tree


def test_empty_tree():
    tree=BinarpointerTree()
    actual= tree.root
    expected=None
    assert actual == expected


def test_only_root_tree():
    node1=TNode("root")
    tree=BinarpointerTree()
    tree.root=node1

    actual=tree.root.value
    expected= "root"
    assert actual== expected

def test_BST_is_asub_class_of_bt():
    actual=issubclass(BinarpointerSearchTree,BinarpointerTree)
    expected=True
    assert actual == expected
def test_add_left_right_child():
    "instantiate abinary search tree"
    bs=BinarpointerSearchTree()

    "add a root to the tree"
    bs.add(5)
    actual=bs.root.value
    expected=5
    assert actual ==expected

    "add a left child"
    bs.add(1)
    actual= bs.root.left.value
    expected=1
    assert actual==expected

    "add right child"
    bs.add(10)
    actual= bs.root.right.value
    expected= 10
    assert actual == expected

def test_pre_order(tree):
    actual=tree.pre_order_itiration()
    expected=[7, 3, 1, 2, 6, 4, 5]
    assert actual==expected

def test_in_order(tree):
    actual=tree.inOrder_iteration()
    expected=[1,3,2,7,4,6,5]
    assert actual==expected

def test_post_order(tree):
    actual=tree.postOrder_Iteration()
    expected= [1,2,3,4,5,6,7]
    assert actual==expected

def test_contains():
    
    bs=BinarpointerSearchTree()
    bs.add(1)
    bs.add(2)
    bs.add(3)

    "True"
    actual=bs.contains(1) and bs.contains(2) and bs.contains(3)
    expected= True
    assert actual==expected

    "False"

    actual= bs.contains(4)
    expected=False
    assert actual == expected

def test_tree_max(tree):
    actual=tree.tree_max()
    expected=7
    assert actual==expected

def test_breadth_first(tree):
    actual= breadth_first(tree)
    expected=[7, 3, 6, 1, 2, 4, 5]
    assert actual==expected

def test_fizz_buzz():
    node1 =kNode(1)
    node2= kNode(10)
    node3 =kNode(30)
    node4=kNode(12)
    node5=kNode(15)
    node6=kNode(9)
    node7=kNode(70)
    node2.child.append(node5)
    node5.child.append(node6)
    node5.child.append(node7)
    node1.child.append(node2)
    node1.child.append(node3)
    node1.child.append(node4)
    tree=k_ary_Tree()
    tree.root=node1

    # running the function
    
    
    actual = fizz_buzz_tree(tree)
    expected = "1"
    assert actual == expected

    # for the child
    childs=[]
    for child in tree.root.child:
        childs.append(child.value)
    actual=childs
    expected=["Buzz","Fizz Buzz","Fizz"]
    assert actual==expected


@pytest.fixture
def tree():
    tree = BinarpointerTree()
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node5 = TNode(5)
    node6 = TNode(6)
    node7 = TNode(7) 
    tree.root = node7
    node7.left = node3
    node7.right=node6
    node3.left = node1
    node3.right = node2
    node6.left=node4
    node6.right=node5   
    return tree





    



class TestStack(unittest.TestCase):
    def test_pre_order_exception(self):
        tree= BinarpointerTree
        with self.assertRaises(Exception):
            tree.pre_order_itiration()


    def test_in_order_exception(self):
        tree= BinarpointerTree
        with self.assertRaises(Exception):
            tree.inOrder_iteration()
    
    def test_post_order_exception(self):
        tree= BinarpointerTree
        with self.assertRaises(Exception):
            tree.postOrder_Iteration()

    def test_tree_max_exception(self):
        tree=BinarpointerTree()
        with self.assertRaises(Exception):
            tree.tree_max()
    def test_breadth_tset_empty_tree(self):
        tree=BinarpointerTree()
        with self.assertRaises(Exception):
            breadth_first(tree)

    def test_k_tree(self):
        tree=k_ary_Tree()
        with self.assertRaises(Exception):
            fizz_buzz_tree(tree)

    