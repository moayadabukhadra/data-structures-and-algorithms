class Node:
    def __init__(self,value=None):
        self.value = value
        

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}


    def add_node(self,value):
        """
        Adds a node to the graph
        """
        v=Node(value)
        self.adjacency_list[v]=[]
        return v



        

    def add_edge(self,node1,node2,weight=0):
        """
        Adds an edge to the graph
        # """
        if not node1 in self.adjacency_list.keys():
            raise KeyError("Node1 not in graph")
        if not node2 in self.adjacency_list.keys():
            raise KeyError("Node2 not in graph")
        edge = Edge(node2,weight)
        self.adjacency_list[node1].append(edge)
        


    def get_nodes(self):
        """
        Returns a list of nodes in the graph
        """
        return list(self.adjacency_list.keys())

    def get_neighbors(self,node):
        """
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        """

        if not node in self.adjacency_list.keys():
            raise KeyError("Node not in graph")
        
        return {edge.vertex:edge.weight for edge in self.adjacency_list[node]}
        



    def size(self):
        """
        Returns the number of nodes in the graph
        """
        if self.adjacency_list == {}:
            return 0
        return len(self.adjacency_list)
    
    def __str__(self):
        if self.adjacency_list == {}:
            return None
        output=''
    
        for node in self.adjacency_list.keys():
            output+=str(node.value)+' -> '
            for edge in self.adjacency_list[node]:
                output+=str(edge.vertex.value)+' -> '
            output+='\n'
        return output

        

if __name__=='__main__':
    g=Graph()
    node1=g.add_node(1)
    node2=g.add_node(2)
    node3=g.add_node(3)
    g.add_edge(node1,node2)
    g.add_edge(node1,node3)
    g.add_edge(node2,node3)

    print(g.__str__())
