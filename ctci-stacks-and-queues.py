class Stack:
    def __init__(self, s1, s2, s3):
        self.head_index_1 = -1 
        self.head_index_2 = s1 - 1
        self.head_index_3 = s1+s2 - 1

        self.cap_1 = s1
        self.cap_2 = s2 
        self.cap_3 = s3

        self.cap_arr = [self.cap_1, self.cap_2, self.cap_3]
        self.cur_size_arr = [0, 0, 0]
        self.head_arr = [self.head_index_1, self.head_index_2, self.head_index_3]
        self.arr = [None]* (s1+s2+s3)

    def push(self, data, stack_no):

        if self.cur_size_arr[stack_no] + 1 <= self.cap_arr[stack_no]: 
            
            head = self.head_arr[stack_no]+1
            self.head_arr[stack_no] = head 

            self.arr[head] = data
            self.cur_size_arr[stack_no] = self.cur_size_arr[stack_no] + 1 
        else:
            print("Capacity is full!")
        # if capacity is enough
        # change head
        
    def remove(self, stack_no):
        head_index = self.head_arr[stack_no]
        if self.arr[head_index] != None and self.cur_size_arr[stack_no] != 0:
            self.head_arr[stack_no] -= 1
            self.arr[head_index] = None
            self.cur_size_arr[stack_no] = self.cur_size_arr[stack_no] - 1 
        else:
            print("Stack is empty!")
        
      

    def print_stack(self):
        for i in range(len(self.arr)-1, -1, -1):
            print(self.arr[i])


    def peek(self):
        return self.head_arr


stack = Stack(3,3,3)

stack.push(1, 0)
stack.push(2, 0)
stack.push(3, 0)


stack.push(10, 1)
stack.push(20, 1)
stack.push(30, 1)

stack.push(100, 2)
stack.push(200, 2)
stack.push(300, 2)

stack.head
stack.remove()
# stack.remove(0)
# stack.remove(0)
# stack.remove(0)

stack.print_stack()



