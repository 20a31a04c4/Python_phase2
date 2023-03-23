class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def add_element(self,head,value):
        new_node=Node(value) 
        temp=head
        while temp.next is not None: 
            temp=temp.next
        temp.next=new_node 
obj=LinkedList()
head=Node(10) 
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)        