



class Queue:
    def __init__(self):
        self.cap = 5
        self.cur_size = 5
        self.queue = ["cat1", "dog1", "cat2", "dog2", "cat3"]
        self.head = 0
        self.size = len(self.queue)

    def push(self, animal):
        if self.cur_size + 1 <= self.cap: 
            self.cur_size = self.cur_size + 1 
            self.queue.append(animal)
        else:
            print("Capacity is full!")
        
    def remove(self):
        if self.queue[self.head] != None and self.cur_size != 0:
            self.queue[self.head] = None
            self.head += 1
            self.cur_size -= 1 
        else:
            print("QUEUE is empty!")
      
    def print_queue(self):
        for i in range(len(self.queue)-1, -1, -1):
            print(self.queue[i])

    def peek(self):
        return self.stack[self.head]
    
    def isEmpty(self):
        if self.queue[self.head] == None:
            return True
        else:
            return False
    
    def size(self):
        return self.cur_size
    
    def pop(self):
        popped_data = self.queue[self.head]
        self.remove()
        return popped_data
    
    def simulate_adoption_shelter(self, preference):
        temp_head = -1

        if preference == "dm":
            _ = self.queue.pop()
        else:
            while temp_head + 1 < self.cur_size:
                temp_head = temp_head + 1
                # remove dog
                if self.queue[temp_head][0] == preference:
                    self.queue[temp_head] = None
                    break
    


    

q = Queue()

q.simulate_adoption_shelter("c")
q.print_queue()
