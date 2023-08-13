class Node:

    def __init__(self, d):
        self.next = None
        self.data = d

# this is two ptr approach
def init_nodes():
    node_1 = Node(10)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8
    return node_1


def connect_node_to_first_partition(head, node):
    if head == None:
        head = node
    else:
        node.next = head.next
        head.next = node
        head = node
    return head


def add_nodes_to_head(head, node):
    if head == None:
        head = node
    else: 
        head.next = node
        head = node
    return head

def partition_nodes(node, partition_val):
    init_node = Node(node.data)
    init_node.next = node.next 

    before_head_end = None
    after_head_end = None
    after_head_start = None
    before_head_start = None
    while node != None:
        if node.data >= partition_val:
            after_head_end = add_nodes_to_head(after_head_end, node)
            if after_head_start == None:
                after_head_start = after_head_end
        else:
            before_head_end = add_nodes_to_head(before_head_end,node)
            if before_head_start == None:
                before_head_start = before_head_end

        node = node.next
    
    before_head_end.next = after_head_start

    node = before_head_start 
    while node != None:
        print(node.data)
        node = node.next

node = init_nodes()
partition_nodes(node, 5)
    



