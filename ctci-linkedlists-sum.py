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
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6

    # 579
    return node_1


def sum_numbers_as_node(node):
    init_node = node

    size=0
    while node != None:
        size += 1 
        node = node.next
    node = init_node

    first_num_node_ptr  = node
    first_num_node_ptr.next  = node.next
    second_num_node_ptr = node
    second_num_node_ptr.next  = node.next
    sum_node = None
    at_hand = 0
    counter = 0
    last_flag = False


    for _ in range(counter, int(size/2)):
        second_num_node_ptr = second_num_node_ptr.next
    
    sum_node = None
    while second_num_node_ptr != None:   
        counter += 1 
        if counter == size/2:
            last_flag = True
        sum_digit = second_num_node_ptr.data + first_num_node_ptr.data + at_hand

        # so sth if it is at the las element
        if sum_digit > 9 and not last_flag:
            at_hand = 1
            str_digit = str(sum_digit) 
            sum_digit = int(str_digit[1])
            cur_sum_node = Node(sum_digit)
        elif sum_digit > 9 and last_flag:
            str_digit_str = str(sum_digit) 
            sum_digit_1 = int(str_digit_str[0])
            sum_digit_2 = int(str_digit_str[1])
            cur_sum_node_1 = Node(sum_digit_2)
            cur_sum_node_2 = Node(sum_digit_1)
            at_hand = 0
        elif sum_digit <= 9:
            cur_sum_node = Node(sum_digit)
            at_hand = 0
        else:
            continue

        # iter node
        if sum_node == None:
           sum_node = cur_sum_node
           sum_node_first = sum_node
        else:
            if last_flag == True and sum_digit > 9:
                sum_node.next = cur_sum_node_1
                cur_sum_node_1.next = cur_sum_node_2
                cur_sum_node_2.next = None
                break
            else:
                sum_node.next = cur_sum_node
                sum_node = cur_sum_node


        second_num_node_ptr = second_num_node_ptr.next
        first_num_node_ptr = first_num_node_ptr.next

    node = sum_node_first 
    while node!= None:
        print(node.data)
        node = node.next
        
        
node_1 = init_nodes()
# sum_numbers_as_node(node_1)

def reverse_nodes(node):
    current = node
    prev = None
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev

    current = head
    while head != None:
        print(current.data) 
        current = current.next
reverse_nodes(node_1)
