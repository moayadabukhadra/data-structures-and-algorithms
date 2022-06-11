# graphs:

## methods:

### 1. add_node:

this method adds a node to the graph.

    `graph.add_node(node)`

    * `node`: the node to add to the graph.

    * returns: the node added to the graph.

Big O:

    * time: O(1)
    * space: O(1)

### 2. add_edge:

    `graph.add_edge(node1, node2)`

    * `node1`: the first node to add to the graph.
    * `node2`: the second node to add to the graph.

    * returns: the edge added to the graph.
    
Big O:

    * time: O(1)
    * space: O(1)

### 3. get_nodes:

    `graph.get_nodes()`

    * returns: a list of all the nodes in the graph.

    Big O:

        * time: O(1)
        * space: O(1)

### 4. get_neighbors:

    `graph.get_neighbors(node)`

    * `node`: the node to get the neighbors of.

    * returns: a list of all the neighbors of the node.

    Big O:

        * time: O(N)
        * space: O(1)

### 5. size:
    
        `graph.size()`
    
        * returns: the number of nodes in the graph.
    
        Big O:
    
            * time: O(N)
            * space: O(1)

### 6. str:
        
            `graph.str()`
        
            * returns: a string representation of the graph.
        
            Big O:
        
                * time: O(N)
                * space: O(N)






