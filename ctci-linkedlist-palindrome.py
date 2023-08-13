import math
class Node:

    def __init__(self, d):
        self.next = None
        self.data = d

def init_nodes():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(3)
    node_6 = Node(2)
    node_7 = Node(1)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    return node_1

def is_palindrome_1():
    current_node = init_nodes()
    # reverse the linkedlist
    reversed_head = reverse_list(cur    rent_node)

    # check the lists are the same
    while reversed_head != None and current_node != None:
        if reversed_head.data == current_node.data:
            reversed_head = reversed_head.next
            current_node = current_node.next
            continue
        else:
            return False
    return True


def reverse_list(current_node):
    
    prev = None

    while current_node != None:
        next = current_node.next
        current_node = Node(current_node.data)
        current_node.next = prev
        prev = current_node
        current_node = next

    head = prev
    return head



def is_palindrome():
    size = 7
    stack = []
    current_node = init_nodes()
    
    if current_node == None:
        return False
     
    odd = True if size%2 == 1 else False
   
    for _ in range(0, math.floor(size/2)):
        stack.append(current_node)
        current_node = current_node.next
    

    if odd:
        current_node = current_node.next

    while current_node != None:
      

        el = stack.pop()
        if current_node.data == el.data:
            current_node = current_node.next
        else:
            return False

    return True

print(is_palindrome())