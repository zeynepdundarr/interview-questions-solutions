
class Node:

    def __init__(self, d):
        self.next = None
        self.data = d

# this is two ptr approach
def init_nodes():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    return node_1

def delete_middle(node, val):

    print(node.data)
    while node.next != None:
        if val == node.next.data:
            node = node.next.next
        else:
            print(node.data)
            node = node.next


# node = init_nodes()
# print(delete_middle(node, 2))



# Imagine that you have only access to the node 2. Can you delete the node by this info
# if I have doubly linked list, I can delete by this way


def delete_middle_II(head, node):
    # transfer the next node data to to be deleted node. By this way you can persist the links with the previous node. You can go towards end of the linked list by assigning to-be-dleeted's next to the next,next node
    node.data = node.next.data
    node.next = node.next.next

    if node == None or node.next == None:
        return False
    nodee = head
    while nodee != None:
        print(nodee.data)
        nodee = nodee.next 
    return True

node = init_nodes()
print(delete_middle_II(node, node))
