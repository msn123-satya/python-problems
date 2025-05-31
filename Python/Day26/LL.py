#Displaying a linked list
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.display()'''

#reversing a linked list
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        curr=self.head
        while(curr):
           next=curr.next
           curr.next=prev
           prev=curr
           curr=next
        self.head=prev
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.display()
print()
s1.reverse()
s1.display()'''

#adding a node at beginning
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def node_beg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.display()
print()
s1.node_beg(5)
s1.display()'''

#adding a node at end
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def node_end(self,data):
        temp=self.head
        while(temp.next):
            temp=temp.next
        ne=Node(data)
        temp.next=ne
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.display()
print()
s1.node_end(50)
s1.display()'''

#adding a node at specific position
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def node_pos(self,pos,data):
        temp=self.head
        if(pos==1):
            self.node_beg(5)
        for p in range(1,pos-1):
            temp=temp.next
        np=Node(data)
        np.next=temp.next
        temp.next=np
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.display()
print()
s1.node_pos(4,25)
s1.display()'''

#Deleting 1st node
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def del_beg(self):
        temp=self.head
        self.head=temp.next
        temp=None
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.display()
print()
s1.del_beg()
s1.display()'''

#Deleting last node
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def del_last(self):
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.display()
print()
s1.del_last()
s1.display()'''

#Deleting specific node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def del_spec(self,pos):
        '''prev=self.head
        temp=self.head.next
        for p in range(1,pos-1):
            prev=prev.next
            temp=temp.next
        prev.next=temp.next'''
        temp=self.head
        for p in range(1,pos-1):
            temp=temp.next
        temp.next=temp.next.next
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.display()
print()
s1.del_spec(3)
s1.display()

#all_at_a_time
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        curr=self.head
        while(curr):
           next=curr.next
           curr.next=prev
           prev=curr
           curr=next
        self.head=prev
    def node_beg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def node_pos(self,pos,data):
        temp=self.head
        if(pos==1):
            self.node_beg(5)
        for p in range(1,pos-1):
            temp=temp.next
        np=Node(data)
        np.next=temp.next
        temp.next=np
    def node_end(self,data):
        temp=self.head
        while(temp.next):
            temp=temp.next
        ne=Node(data)
        temp.next=ne
    def del_beg(self):
        temp=self.head
        self.head=temp.next
        temp=None
    def del_last(self):
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
s1=single()
s1.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
s1.display()
print()
#s1.reverse()
#s1.display()
#s1.node_beg(5)
#s1.display()
#s1.node_pos(4,25)
#s1.display()
#s1.node_end(50)
#s1.display()
#s1.del_beg()
#s1.display()
s1.del_last()
s1.display()'''

#Displaying a linked list(another method)
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def insert(self):
        n=int(input("Enter no.of nodes:"))
        for p in range(n):
              data=int(input("Enter data:"))
              nw=Node(data)
              if(self.head==None):
                  self.head=nw
                  self.tail=nw
              else:
                  self.tail.next=nw
                  self.tail=nw              
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
s1=single()
s1.insert()
s1.display()'''














