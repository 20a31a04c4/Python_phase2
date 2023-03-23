class stack:
    def __init__(self):
        self.size=5
        self.arr=[]
        self.arr2=[]
    def push(self,element):
        self.arr.append(element)
    def stack_pop(self):
        self.arr.pop()
    def binary_search(self,key):
        low=0
        high=len(self.arr)-1
        found = False
        while low<=high:
            mid=(low+high)//2
            if key == self.arr[low]:
                print('it is found at',low)
                break
            elif key==self.arr[high]:
                print('it is found at',high)
                break
            elif self.arr[mid] == key:
                print('found at',mid)
                found = True
                break
            elif key < self.arr[mid]:
                high=mid+1
            elif key > self.arr[mid]:
                low=mid-1
        else:
            print('not found')
obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
obj.push(60)
print(obj.arr)
obj.arr.sort()
obj.binary_search(50)