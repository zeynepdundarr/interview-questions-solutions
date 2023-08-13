
# # TODO: 
# # try to implement recursively
# # if you could find the k-1 to the last element, could you find the kth element?
# # Can you do it iteratively, imagine if you had two pointers pointing to adjacent nodes and


# class Node:

#     def __init__(self, d):
#         self.next = None
#         self.data = d

# # this is two ptr approach
# def init_nodes():
#     node_1 = Node(1)
#     node_2 = Node(2)
#     node_3 = Node(3)
#     node_4 = Node(4)
#     node_5 = Node(5)
#     node_6 = Node(6)
#     node_7 = Node(3)
#     node_1.next = node_2
#     node_2.next = node_3
#     node_3.next = node_4
#     node_4.next = node_5
#     node_5.next = node_6
#     node_6.next = node_7
#     return node_1

# def return_kth_to_last(k):
    
#     first_node =  init_nodes()
#     temp_node = first_node

#     size = 0
#     while first_node != None:
#         size += 1
#         first_node = first_node.next
        
#     index = 0
#     cur_node = temp_node
#     while cur_node != None:
#         if size - k - 1 == index:
#             return cur_node.data
#         index += 1
#         cur_node = cur_node.next
#     return False



# print(return_kth_to_last(4))



# TODO: 
# try to implement recursively
# if you could find the k-1 to the last element, could you find the kth element?
# Can you do it iteratively, imagine if you had two pointers pointing to adjacent nodes and


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

def return_kth_to_last_II(k):
    
    head = None
    cur_node = init_nodes()
    size = 0
    while cur_node != None:
        reversed_node, head = push_reverse_node(cur_node.data, head)
        cur_node = cur_node.next
        size += 1 

    index = 0
    while reversed_node != None:
        if index == k:
            return reversed_node.data
        else:
            reversed_node = reversed_node.next
        index += 1
    

def push_reverse_node(data, head):
    reversed_node = Node(data)
    reversed_node.next = head
    head = reversed_node
    return reversed_node, head
    


print(return_kth_to_last_II(2))