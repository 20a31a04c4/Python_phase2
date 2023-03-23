class stack:
    def __init__(self):
       self.arr=[] 
       self.size=6
    def stack_push(self, element):
        if len(self.arr) == self.size:
            print("stack is full")
        else: 
            self.arr.append(element)
    def stack_pop(self):
        if len(self.arr) == 0:
            print("stack is underflow") 
        else:
             return self.arr.pop()
s1=stack() 
s1.stack_push(20)
s1.stack_push(30)
s1.stack_push(40)
s1.stack_push(50)
s1.stack_push(60) 
s1.stack_push(70)      
print(s1.arr)  
s2=stack() 
s2.stack_push(s1.stack_pop()) 
s2.stack_push(s1.stack_pop()) 
s2.stack_push(s1.stack_pop()) 
s2.stack_push(s1.stack_pop())
s2.stack_push(s1.stack_pop())
s2.stack_push(s1.stack_pop())
print(s2.arr)
   
