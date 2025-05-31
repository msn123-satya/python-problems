#creating a double linked list and displaying it
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Double:
    def __init__(self):
        self.head=None
        self.tail=None
    def reverse(self):
        temp=self.tail
        if(self.tail is None):
            print("Empty Double linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.prev
    def display(self):
        temp=self.head
        if(self.head is None):
            print("Empty Double linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
n1=Node(10)
d1=Double()
d1.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
d1.tail=n4
d1.display()
print()
d1.reverse()'''
            
#to count no.of nodes in a linked list
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Double:
    def __init__(self):
        self.head=None
        self.tail=None
    def reverse(self):
        temp=self.tail
        if(self.tail is None):
            print("Empty Double linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.prev
    def display(self):
        temp=self.head
        if(self.head is None):
            print("Empty Double linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
    def count_nodes(self):
        temp=self.head
        c=0
        while(temp):
            c=c+1
            temp=temp.next
        print("No.of nodes:",c)
    def sort(self):
        temp=self.head
        l=[]
        while(temp):
            l.append(temp.data)
            temp=temp.next
        l.sort()
        print(*l)
n1=Node(4)
d1=Double()
d1.head=n1
n2=Node(2)
n1.next=n2
n2.prev=n1
n3=Node(1)
n2.next=n3
n3.prev=n2
n4=Node(5)
n3.next=n4
n4.prev=n3
d1.tail=n4
#d1.reverse()
#d1.display()
d1.count_nodes()
d1.sort()'''

#printing node info from head and tail
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Double:
    def __init__(self):
        self.head=None
        self.tail=None
    def reverse(self):
        temp=self.tail
        if(self.tail is None):
            print("Empty Double linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.prev
    def display(self):
        temp=self.head
        if(self.head is None):
            print("Empty Double linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
    def count_nodes(self):
        temp=self.head
        c=0
        while(temp):
            c=c+1
            temp=temp.next
        print("No.of nodes:",c)
        return c
    def sort(self):
        temp=self.head
        l=[]
        while(temp):
            l.append(temp.data)
            temp=temp.next
        l.sort()
        print(*l)
    def print_beg(self,pos):
        c=1
        temp=self.head
        while(temp):
            if(c==pos):
                return (temp.data)
            c=c+1
            temp=temp.next
    def print_end(self,pos):
        c=self.count_nodes()
        temp=self.head
        for p in range(c-pos):
            temp=temp.next
        return (temp.data)
n1=Node(10)
d1=Double()
d1.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
d1.tail=n4
#d1.reverse()
d1.display()
print()
d1.count_nodes()
#d1.sort()
n=int(input("Enter the position from the beg:"))
print(d1.print_beg(n))
n1=int(input("Enter the position from the end:"))
print(d1.print_end(n1))'''

#adding and deleting node at beginning and ending and specific position
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Double:
    def __init__(self):
        self.head=None
        self.tail=None
    def reverse(self):
        temp=self.tail
        if(self.tail is None):
            print("Empty Double linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.prev
    def Node_beg(self,data):
        temp=self.head
        nb=Node(data)
        nb.next=self.head
        self.head.prev=nb
        self.head=nb
    def Node_end(self,data):
        temp=self.tail
        ne=Node(data)
        ne.prev=temp
        self.tail.next=ne
        self.tail=ne
    def Node_pos(self,pos,data):
        temp=self.head
        if(pos==1):
            self.node_beg(data)
        for p in range(1,pos-1):
            temp=temp.next
        np=Node(data)
        np.next=temp.next
        np.prev=temp
        temp.next=np
        temp.next.prev=np
    def display(self):
        temp=self.head
        if(self.head is None):
            print("Empty Double linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
    def count_nodes(self):
        temp=self.head
        c=0
        while(temp):
            c=c+1
            temp=temp.next
        print("No.of nodes:",c)
        return c
    def sort(self):
        temp=self.head
        l=[]
        while(temp):
            l.append(temp.data)
            temp=temp.next
        l.sort()
        print(*l)
    def print_beg(self,pos):
        c=1
        temp=self.head
        while(temp):
            if(c==pos):
                return (temp.data)
            c=c+1
            temp=temp.next
    def print_end(self,pos):
        c=self.count_nodes()
        temp=self.head
        for p in range(c-pos):
            temp=temp.next
        return (temp.data)
    def del_beg(self):
       temp = self.head
       self.head = temp.next
       temp.next = None
       if self.head:
           self.head.prev = None
       else:
           self.tail = None
    def del_end(self):
        temp=self.tail
        self.tail=temp.prev
        temp.prev=None
        if self.tail:
           self.tail.next = None
        else:
           self.head = None
    def del_spec(self,pos,data):
         if(pos==1):
            self.node_beg(data)
         temp=self.head
         for p in range(pos-1):
            temp=temp.next
         if temp==self.head:
            self.head=temp.next
         if temp.next is not None:
            temp.next.prev=temp.prev
         if temp.prev is not None:
            temp.prev.next=temp.next
n1=Node(10)
d1=Double()
d1.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
d1.tail=n4
#d1.reverse()
d1.display()
print()
#d1.count_nodes()
#d1.sort()
#n=int(input("Enter the position from the beg:"))
#print(d1.print_beg(n))
#n1=int(input("Enter the position from the end:"))
#print(d1.print_end(n1))
#d1.Node_beg(5)
#d1.display()
#d1.Node_end(50)
#d1.display()
#d1.Node_pos(3,25)
#d1.del_beg()
#d1.display()
#d1.del_end()
d1.del_spec(3,25)
d1.display()
