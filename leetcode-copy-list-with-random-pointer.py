class Node:
    def __init__(self, d):
        self.next = None
        self.data = d

def init_nodes():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    return node_1


def copy_list(head):
        # iterate all nodes
        # while iterating set next ptr@s of random and next
        # put the nodes to hashset to retrieve when it is necessary, keys are data