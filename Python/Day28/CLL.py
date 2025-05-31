#implementation of circular linked list
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circular:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self):
        n=int(input("Enter no.of nodes:"))
        for p in range(n):
              data=int(input("Enter data:"))
              nw=Node(data)
              if(self.head==None):
                  self.head=nw
                  self.tail=nw
                  self.tail.next=self.head
              else:
                  self.tail.next=nw
                  self.tail=nw
                  self.tail.next=self.head
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty circular linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
                if(temp==self.head):
                    break
            print(temp.data)
c1=Circular()
c1.insert()
c1.display()'''

#reversing the circular linked list,adding node at beg
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circular:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self):
        n=int(input("Enter no.of nodes:"))
        for p in range(n):
              data=int(input("Enter data:"))
              nw=Node(data)
              if(self.head==None):
                  self.head=nw
                  self.tail=nw
                  self.tail.next=self.head
              else:
                  self.tail.next=nw
                  self.tail=nw
                  self.tail.next=self.head
    def Node_beg(self,data):
        temp=self.head
        nb=Node(data)
        nb.next=self.head
        self.tail.next=nb
        self.head=nb
    def Node_end(self,data):
        temp=self.tail
        ne=Node(data)
        self.tail.next=ne
        self.tail=ne
        self.tail.next=self.head
    def Node_pos(self,data,pos):
        np=Node(data)
        if(pos==1):
            self.node_beg(data)
        else:
            temp=self.head
            for i in range(1,pos-1):   
                temp=temp.next
            np.next=temp.next
            temp.next=np
    def del_beg(self):
        temp=self.head
        self.head=temp.next
        self.tail.next=self.head
    def del_end(self):
        temp=self.head
        while(temp.next.next!=self.head):
            temp=temp.next
        temp.next=self.head
        self.tail=temp
    def del_pos(self,pos):
        if(pos==1):
            self.del_beg()
        else:
            temp=self.head
            for i in range(1,pos-1):
                temp=temp.next
            temp.next=temp.next.next
    def reverse(self):
        prev=self.tail
        curr=self.head
        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            if(curr==self.head):
                break
            self.head=prev
            self.tail=curr
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty circular linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
                if(temp==self.head):
                    break
            print(temp.data)
c1=Circular()
c1.insert()
c1.display()
#c1.reverse()
#c1.Node_beg(5)
#c1.Node_end(5)
#c1.del_beg()
#c1.del_end()
#c1.del_pos(2)
c1.Node_pos(3)
c1.display()
