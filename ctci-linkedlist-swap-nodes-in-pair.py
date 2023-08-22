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


def swap_nodes(head, x, y):
    if x == y:
        return head

    prev_x = None
    cur_node_x = head
    cur_node_y = head
    while cur_node_x and cur_node_x.data != x:
        prev_x = cur_node_x
        cur_node_x = cur_node_x.next

    prev_y = None
    while cur_node_y and cur_node_y.data != y:
        prev_y = cur_node_y
        cur_node_y = cur_node_y.next

    if prev_y != None:
        prev_y.next = cur_node_x
    else:
        head = cur_node_x

    if cur_node_y == None or cur_node_x == None:
        return False

    if prev_x != None:
        prev_x.next = cur_node_y
    else:
        head = cur_node_y

    temp_next_node_y = cur_node_y.next
    cur_node_y.next = cur_node_x.next
    cur_node_x.next = temp_next_node_y
    
    return head

def print_linkedlist(current_node):
    while current_node != None:
        print(current_node.data) 
        current_node = current_node.next

def swap_nodes_in_pairs(node):

    i = 1
    head = node

    for i in range(1,4):
        if i % 2 == 1:
            head = swap_nodes(head, i, i+1)
    return head

node_1 = init_nodes()
# print(swap_nodes_in_pairs(node_1).data) 
print_linkedlist(swap_nodes_in_pairs(node_1))

# swap_nodes(node_1, 2, 4)
    
# head_1 = swap_nodes(node_1, 1, 2)
# print("1st test")
# print(print_linkedlist(head_1))
# print()
# head_2 = swap_nodes(node_1, 2, 3)
# print("2nd test")
# print(print_linkedlist(head_2))
# print()
# head_3 = swap_nodes(head_1, 3, 4)
# print("3rd test")
# print(print_linkedlist(head_3))

