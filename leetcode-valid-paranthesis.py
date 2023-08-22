class Stack:
    def __init__(self, size):
        self.head = -1 
        self.cap = size
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
    

def is_matching(a, d, next):
    if d[a] == next:
        return True
    else:
        return False

def valid_paranthesis(string):
    d = {")":"(", "]":"[", "}":"{"}

    stack = Stack(len(string))
    for ch in string:
        last_in_stack = stack.peek()
        if ch in "{([":
            stack.push(ch)
        
        else:
            if not stack or (ch==")" and last_in_stack != "(") or (ch == "}" and last_in_stack != "{") or (ch == "]" and last_in_stack != "["):
                return False
            stack.pop()  

    return not stack

print(valid_paranthesis(")(){}"))
