# class Node:

#     def __init__(self, d):
#         self.next = None
#         self.data = d


# def init_nodes_1():
#     node_1 = Node(1)
#     node_2 = Node(2)
#     node_3 = Node(3)

#     node_1.next = node_2
#     node_2.next = node_3
#     return node_1, node_3

# def init_nodes_2():
#     node_1 = Node(8)
#     node_2 = Node(9)
#     node_3 = Node(10)

#     node_1.next = node_2
#     node_2.next = node_3

#     return node_1, node_3


# def find_intersecting_node(node_1, node_2):
#     node_1_traversed = reverse_list(node_1)
#     node_2_traversed = reverse_list(node_2)

#     prev = None
#     while node_1_traversed.data == node_2_traversed.data:
#         prev = node_1_traversed
#         node_1_traversed = node_1_traversed.next 
#         node_2_traversed = node_2_traversed.next 
#     return prev

# def reverse_list(current_node):
#     prev = None
#     while current_node != None:
#         next = current_node.next
#         current_node = Node(current_node.data)
#         current_node.next = prev
#         prev = current_node
#         current_node = next

#     head = prev
#     return head

# node_1, last_node_1 = init_nodes_1()
# node_2, last_node_2 = init_nodes_2()

# node_4 = Node(18)
# node_5 = Node(19)
# node_6 = Node(20)

# last_node_1.next = node_4
# last_node_2.next = node_4

# node_4.next = node_5
# node_5.next = node_6


# print(find_intersecting_node(node_1, node_2).data)


class Node:
    def __init__(self, d):
        self.next = None
        self.data = d

def iter_nodes(current_node, iter_count):
    i = 0
    while iter_count != i: 
        current_node = current_node.next
        i += 1
    return current_node

def init_nodes_1():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.next = node_2
    node_2.next = node_3
    return node_1, node_3

def init_nodes_2():
    node_1 = Node(8)
    node_2 = Node(9)
    node_3 = Node(10)
    node_4 = Node(11)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    return node_1, node_4

def find_intersecting_node_II(current_node_1, current_node_2):
    size_1 = 0
    size_2 = 0
    node_1_copy, node_2_copy = current_node_1, current_node_2
    # determine sizes
    while node_1_copy != None:
        size_1 += 1
        prev_1 = node_1_copy
        node_1_copy = node_1_copy.next 

    while node_2_copy != None:
        size_2 += 1
        prev_2 = node_2_copy
        node_2_copy = node_2_copy.next 

    if prev_1.data != prev_2.data:
        return False

    node_1_copy_2, node_2_copy_2 = current_node_1, current_node_2

    if size_1 > size_2:
        # iterate to the kth node
        long_list= iter_nodes(node_1_copy_2, size_1 - size_2)
        short_list = node_2_copy_2
    else:
        # iterate to the kth node
        long_list = iter_nodes(node_2_copy_2, size_2 - size_1)
        short_list = node_1_copy_2

    while short_list != None:
        if long_list != short_list: 
            long_list = long_list.next
            short_list = short_list.next
        else:
            return short_list.data
    return False

node_1, last_node_1 = init_nodes_1()
node_2, last_node_2 = init_nodes_2()

node_4 = Node(18)
node_5 = Node(19)
node_6 = Node(20)

last_node_1.next = node_4
last_node_2.next = node_4

node_4.next = node_5
node_5.next = node_6
print(find_intersecting_node_II(node_1, node_2))

