class Node:
    def __init__(self, d):
        self.next = None
        self.data = d
        self.random = None

def init_nodes():
    node_1 = Node(7)
    node_2 = Node(13)
    node_3 = Node(11)
    node_4 = Node(10)
    node_5 = Node(1)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    node_1.random = "NULL"
    node_2.random = 0
    node_3.random = 4
    node_4.random = 2
    node_5.random = 0

    return node_1


def copy_list(cur_node):
    # iterate all nodes
    # while iterating set next ptr@s of random and next
    # put the nodes to hashset to retrieve when it is necessary, keys are data

    node_dict = {}
    copy_node = None
    prev = None
    head_copy_node = None

    
    while cur_node != None:
        if prev == None:
            copy_node = Node(cur_node.data)
            head_copy_node = copy_node
            head_cur_node = cur_node
        else:
            copy_node = Node(cur_node.data)
            prev.next = copy_node

        # add node to the dict for retrieval
        if cur_node.data not in node_dict.keys():
            random_node = cur_node.random
            if random_node:
                node_dict[cur_node.data] = random_node
            else:
                node_dict[cur_node.data] = None


        cur_node = cur_node.next
        prev = copy_node

    copy_node = head_copy_node
    random_copy_node = None
    while copy_node != None:
        random_copy_node = node_dict[copy_node.data]
        if random_copy_node:
            copy_node.random = random_copy_node
        else:
            copy_node.random = None
        copy_node = copy_node.next
    
    return head_copy_node



def print_linkedlist(current_node):
    while current_node != None:
        print("data: ", current_node.data) 
        if current_node.random:
            print("random.data: ", current_node.random) 
        current_node = current_node.next



def print_linkedlist_II(current_node):
    ans_arr = []
    while current_node != None:
        new_arr = []
        new_arr.append(current_node.data)
        if current_node.random != "NULL":
            new_arr.append(current_node.random)
        else:
            new_arr.append("NULL")

        if current_node.random:
            current_node.random
        current_node = current_node.next
        ans_arr.append(new_arr)
    print(ans_arr)

node_1 = init_nodes()
node_2 = copy_list(node_1)

print_linkedlist_II(node_2)