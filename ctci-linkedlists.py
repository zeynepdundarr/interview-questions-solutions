class Node:

    def __init__(self, d):
        self.next = None
        self.data = d

# this is two ptr approach
def remove_duplicates():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(3)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7

    cur_node = node_1
    while cur_node.next != None:
        next_node = cur_node.next
        while next_node != None:
            if cur_node.data == next_node.data:
                to_be_deleted_node = next_node
                next_node = to_be_deleted_node.next
            else:
                next_node = next_node.next

        print(cur_node.data)
        cur_node = cur_node.next

    
remove_duplicates()



# hashset approach

remove_duplicates(
    
)