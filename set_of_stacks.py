class Stack:
    def __init__(self, size):
        self.head = -1 
        self.cap = 3
        self.cur_size = 0
        self.stack = [None] * size

    def push(self, data):
        if self.cur_size + 1 <= self.cap: 
            self.head = self.head + 1 
            self.stack[self.head] = data
            self.cur_size = self.cur_size + 1 
        else:
            print("Capacity is full!")
        
    def remove(self):
        if self.stack[self.head] != None and self.cur_size != 0:
            self.stack[self.head] = None
            self.head -= 1
            self.cur_size -= 1 
        else:
            print("Stack is empty!")
        
      
    def print_stack(self):
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i])


    def peek(self):
        return self.head
    
    def isEmpty(self):
        if self.stack[self.head] == None:
            return True
        else:
            return False
    
    def size(self):
        return self.cur_size


class SetOfStack:
    def  __init__(self, s1, s2, s3):
        self.stack_no = 0
        self.head = -1
        self.total_size = 0
        self.current_stack_no = 0

        self.stack_size = 3
        self.stack_1 = [None] * s1
        self.stack_2 = [None] * s2
        self.stack_3 = [None] * s3
        self.set_of_stacks = [Stack(s1), Stack(s2), Stack(s3)]
        self.current_stack = self.set_of_stacks[self.current_stack_no]
        self.stack_capacity_arr = [s1, s2, s3]


    def push(self, data):
        if self.is_current_stack_available(): 
            self.current_stack.push(data)
            self.head = self.current_stack.peek()
            self.total_size += 1
        else:
            if self.can_move_to_next_stack():
                self.move_to_next_stack()
                self.current_stack.push(data)
                self.head = self.current_stack.peek()
                self.total_size += 1

            else:
                print("All stack plates are full!")

            print("Current stack is full, passing to new stack")


    def print_stack(self):
        for i, stack in enumerate(set_of_stacks.set_of_stacks):
            print("i: ", i)
            stack.print_stack()
     
    def is_current_stack_available(self):
        if self.current_stack.size() + 1 <= self.stack_capacity_arr[self.current_stack_no]:
            return True
        else:
            return False
        
    def can_move_to_next_stack(self):
        if self.current_stack_no + 1 < len(self.set_of_stacks):
            return True
        else:
            return False

    def move_to_next_stack(self):
        self.current_stack_no += 1
        self.current_stack = self.set_of_stacks[self.current_stack_no]


    def remove(self):
        # check if data exists in current stack
        if self.current_stack.stack[self.head] != None:
            if self.head >= 0:
                self.head -= 1
                self.total_size -= 1
                self.current_stack.remove()
            else:
                prev_stack = self.set_of_stacks[self.current_stack_no-1]
                head = prev_stack.peek()
                # it shouldnt be empty normally
                if prev_stack.stack[head] != None:
                    self.current_stack = prev_stack
                    self.head = head
                    self.current_stack_no -= 1 
                    self.total_size -= 1
                    self.current_stack.remove()
                else:
                    print("Empty previous stack")
        else:
            print("Empty current stack")




set_of_stacks = SetOfStack(3,3,3)

set_of_stacks.push(10)
set_of_stacks.push(11)
set_of_stacks.push(12)

set_of_stacks.push(13)
set_of_stacks.push(14)
set_of_stacks.push(15)

# find head 
set_of_stacks.remove()
set_of_stacks.remove()
# find out why 13 is not deleted
set_of_stacks.remove()
set_of_stacks.print_stack()

set_of_stacks.remove()

print("----")
# set_of_stacks.print_stack()

# 0 -> 1 -> 2
