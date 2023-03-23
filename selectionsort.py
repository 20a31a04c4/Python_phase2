#selection sort:sort the elements in ascending order by swaping

n=[1,3,5,55,77,99,56]
for i in range(0,len(n)):
    for j in range(i,len(n)):
        if n[i]>n[j]:
          temp=n[i]
          n[i]=n[j]
          n[j]=temp
print(n) 


def selection(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]        
arr=[2,13,4,5,6,7,67,66,78]
print(arr)
selection(arr)
print(arr)

