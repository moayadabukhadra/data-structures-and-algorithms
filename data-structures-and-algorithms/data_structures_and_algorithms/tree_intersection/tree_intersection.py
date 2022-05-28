from data_structures_and_algorithms.hashtable.hashtable import HashaTable
from data_structures_and_algorithms.trees.trees import BinarpointerTree , TNode

def tree_intersection(tree1,tree2):
    if not tree1.root or not tree2.root:
        raise Exception("The trees cant be empty")
    output=[]
    hashtable=HashaTable()
    tree1_list=tree1.pre_order_itiration()
    tree2_list=tree2.pre_order_itiration()
    for node in tree1_list:
        node=str(node)
        hashtable.set(node,"value")
    for node in tree2_list:
        node=str(node)
        hashtable.set(node,"value")
    for i in hashtable.map:
        if i and len(i)>=2:
            output.append(i[0][0])
    print(output)
    return output 







if __name__=='__main__':
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

    tree_intersection(tree,tree2)