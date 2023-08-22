class Node:
    def __init__(self, d):
        self.next = None
        self.data = d

def init_nodes():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_3
    return node_1


def loop_detection(node):
    slow = node
    fast = node
    start = True

    while fast != None:
        print("fast_data: ", fast.data)
        print("slow_data: ", slow.data)
        if slow.data == fast.data:
            if start: 
                start = False
            else:
                return slow.data
        slow = slow.next
        fast = fast.next.next

    return False

node_1 = init_nodes()
print(loop_detection(node_1))