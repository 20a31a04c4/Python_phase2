class queue: 
    def __init__(self):
        self.temp=[] 
        self.original=[] 
    def enqueue(self, element): 
        self.temp.append(element)
        while len(self.original) !=0:
            pop_element=self.original.pop(0)
            self.temp.append(pop_element)
        while len(self.temp) !=0:
            pop_element=self.temp.pop(0)
            self.temp.append(pop_element)    
    def dequeue(self):
        return self.original.pop(0)
    # def queue_peek(self):
    #     if len(self.arr) == 0:
    #         print("underflow")
    #     else:    
    #         return self.arr[-1]
    # def isEmpty(self):
    #     if len(self.arr)==0:
    #         return True
    #     else:
    #         return False 
    def printqueue(self):
        print("temp:",self.temp)
        print("original:",self.original)
s=queue() 
s.enqueue(10)
s.enqueue(20)
s.enqueue(30) 
s.enqueue(40)
s.enqueue(50) 
print(s.printqueue)       
        
#temp=queue()
# orig=queue()
