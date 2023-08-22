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
        return self.stack[self.head]
    
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
    

class SortedStack:

    def __init__(self):
        self.sorted_stack = Stack(3)


    def push_sorted(self, data):
        secondary_stack = Stack(self.sorted_stack.size)
        if self.sorted_stack.peek() == None:
            self.sorted_stack.push(data)
            return
        
        while not self.sorted_stack.isEmpty(): 
            if data <= self.sorted_stack.peek():
                self.sorted_stack.push(data)
                break
            else:
                popped_data = self.sorted_stack.pop()
                secondary_stack.push(popped_data)
        
        if self.sorted_stack.cur_size == 0:
            self.sorted_stack.push(data)
        
        while not secondary_stack.isEmpty():
            popped_data = secondary_stack.pop()
            self.sorted_stack.push(popped_data)


    

        
                
ss = SortedStack()
ss.push_sorted(1)
ss.push_sorted(2)
ss.push_sorted(0)

ss.sorted_stack.print_stack()