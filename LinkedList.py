#implement linkedlist operations to add,to add at start,to remove an element from end,add in between two elements,
#search an element and display element found at which location,reverse of string.

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.previous = None
class LinkedList:
    def start_add(self,head,value):
        new_node1=Node(value)
        new_node1.next=head
        head=new_node1
        return head
    def add_in_between(self,head,value,pos):
        new_node=Node(value)
        curr=head
        prev=None
        while pos != 0:
            prev = curr
            curr = curr.next
            pos = pos-1
        prev.next = new_node
        new_node.next =curr
        return new_node
    def add_element(self,head,value):
        new_node=Node(value)  #1
        temp=head
        while temp.next is not None:  #2
            temp=temp.next
        temp.next=new_node  #3
        new_node.previous = temp
        new_node.next = None
        
    def remove_element(self):
        temp=head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    def print_list(self):
        temp=head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
    def search_element(self,value):
        temp=head
        count=0
        pos=0
        while temp.next is not None:
            temp=temp.next
            pos +=1 
            if temp.data==value:
                count +=1 
                break
            else:
                count 
        if count !=0:
            return f"element found at {pos}" 
        else:
            return "not found"       
    def reverse(self,head):
        curr=head
        prev=None
        while curr is not None:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        head=prev
        return head 
    def reverse_half(self,head):
        first=head
        cur=head
        prev=None
        n=3
        while n!=0:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            n-=1
        first.next=cur
        return prev   
    


obj=LinkedList()
head=Node(10) 
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)
obj.add_element(head,77)
obj.add_element(head,7)
# obj.print_list()
# obj.remove_element()
# obj.print_list()
# obj.add_in_between(head,777,2)
# obj.print_list()
# val=int(input()) 
# print(obj.search_element(val)) 
# head=obj.reverse(head)
# obj.print_list()
# obj.reverse_half(head)
obj.add_element
obj.print_list()




