from data_structures_and_algorithms.graph.graph import Graph,Node,Edge
import pytest
def test_add_node():
    g = Graph()
    actual = g.add_node(1).value
    assert actual == 1
    g.add_node(2)
    assert g.size() == 2
    g.add_node(3)
    assert g.size() == 3

def test_add_edge():
    g = Graph()
    node1=g.add_node(1)
    node2=g.add_node(2)
    node3=g.add_node(3)
    g.add_edge(node1,node2)
    g.add_edge(node1,node3)
    g.add_edge(node2,node3)
    assert g.get_neighbors(node1) == {node2:0,node3:0}
    assert g.get_neighbors(node2) == {node3:0}
    assert g.get_neighbors(node3) == {}




def test_get_nodes():
    g = Graph()
    node1=g.add_node(1)
    node2=g.add_node(2)
    node3=g.add_node(3)
    assert g.get_nodes() == [node1,node2,node3]

def test_get_neighbors():
    g = Graph()
    node1=g.add_node(1)
    node2=g.add_node(2)
    node3=g.add_node(3)
    g.add_edge(node1,node2)
    g.add_edge(node1,node3)
    g.add_edge(node2,node3)
    assert g.get_neighbors(node1) == {node2:0,node3:0}
    assert g.get_neighbors(node2) == {node3:0}
    assert g.get_neighbors(node3) == {}

    
def test_graph_size():
    g = Graph()
    assert g.size() == 0
    g.add_node(1)
    assert g.size() == 1
    g.add_node(2)
    assert g.size() == 2
    g.add_node(3)
    assert g.size() == 3

def test_str():
    g = Graph()
    node1=g.add_node(1)
    node2=g.add_node(2)
    node3=g.add_node(3)
    g.add_edge(node1,node2)
    g.add_edge(node1,node3)
    g.add_edge(node2,node3)
    assert str(g) == '1 -> 2 -> 3 -> \n2 -> 3 -> \n3 -> \n'

def test_str_empty_graph():
    g = Graph()
    assert g.__str__() == None
def test_add_edge_with_node_not_in_graph():
    g = Graph()
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    with pytest.raises(KeyError):
        g.add_edge(node1,node3)
    with pytest.raises(KeyError):
        g.add_edge(node2,node3)
    with pytest.raises(KeyError):
        g.add_edge(node3,node1)

def test_get_neighbors_with_node_not_in_graph():
    g = Graph()
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    with pytest.raises(KeyError):
        g.get_neighbors(node1)
    with pytest.raises(KeyError):
        g.get_neighbors(node2)
    with pytest.raises(KeyError):
        g.get_neighbors(node3)


def test_graph_with_one_node_and_edge():
    g = Graph()
    node1=g.add_node(1)
    g.add_edge(node1,node1)
    assert g.get_neighbors(node1) == {node1:0}
    assert g.size() == 1

    



        



    