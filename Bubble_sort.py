def bubble_sort(arr):
    for i in range(len(arr)-1):
        swap=False
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:     #if we place >,we get in descending order
                swap=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if swap==False:
            break
    return arr 
arr=[21,34,56,43,2,3,45,89]
print(arr)
print(bubble_sort(arr))                  
