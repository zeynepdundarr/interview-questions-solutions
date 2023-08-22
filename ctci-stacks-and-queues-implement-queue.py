class Stack:
    def __init__(self, size):
        self.head = -1 
        self.cap = 3
        self.cur_size = 0
        self.stack = [None] * size
        self.size = size

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
    
    def pop(self):
        popped_data = self.stack[self.head]
        self.remove()
        return popped_data

class QueueAsAStack:
    def __init__(self):
        self.stack = Stack(3)
        self.q_stack = Stack(3)
    
    def push(self, data_arr):
        self.q_stack = Stack(3)
        temp_stack = self.stack
        i = 0

        # add to current stack
        while self.stack.cur_size != self.stack.size and i != len(data_arr): 
            self.stack.push(data_arr[i])
            i += 1
        
        # temp_stack = self.stack
        while self.stack.cur_size != 0:
            popped = self.stack.pop()
            self.q_stack.push(popped)

        self.stack = temp_stack

    def remove(self):
        # temp_stack = self.stack
        temp_stack = Stack(3)
        while self.q_stack.cur_size != 0:
            popped = self.q_stack.pop()
            temp_stack.push(popped)

        temp_stack.remove()

        q_stack = Stack(3)
        while temp_stack.cur_size != 0:
            popped = temp_stack.pop()
            q_stack.push(popped)
        self.q_stack = q_stack

    def peek(self):
        pass


qaas = QueueAsAStack()

qaas.push([1,2,3])

qaas.stack.print_stack()
print("\nQUEUE")

qaas.remove()
qaas.q_stack.print_stack()
