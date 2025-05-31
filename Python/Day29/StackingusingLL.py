#implementation of stack using linked list
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self):
        data=int(input("enter data:"))
        ne=Node(data)
        ne.next=self.head
        self.head=ne
    def pop(self):
        temp=self.head
        if(temp==None):
            print("Stack is Underflow/Empty:")
        else:
            self.head=temp.next
            print("The deleted ele is:",temp.data)
    def display(self):
        temp=self.head
        if(self.head is None):
            print("empty single linked list:")
        else:
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
    def peek(self):
        temp=self.head
        print("The top ele is:",temp.data)
s1=Stack()
print("*****************STACK*******************")
while(True):
    print("1.Push,2.Pop,3.Display,4.Peek,5.Exit")
    Opt=int(input("Enter your option:"))
    if(Opt==1):
        s1.push()
    elif(Opt==2):
        s1.pop()
    elif(Opt==3):
        s1.display()
    elif(Opt==4):
        s1.peek()
    elif(Opt==5):
        break
    else:
        print("Invalid option/Please try again")'''

#trailing zeroes
'''n=int(input())
c=0
fa=1
for i in range(1,n + 1):
    fa=fa*i
while fa%10==0:
    c=c+1
    fa=fa//10
print("The number of zeroes is",c)'''

#implementation of queue using linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rare=None
    def enqueue(self):
        data=int(input("enter value:"))
        ne=Node(data)
        if(self.rare==None):
            self.front=ne
            self.rare=ne
        else:
            self.rare.next=ne
            self.rare=ne
    def dequeue(self):
        temp=self.front
        if(temp==None):
            print("Queue is empty")
        else:
            print("The del ele is",temp.data)
            self.front=temp.next
    def display(self):
        temp=self.front
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    def peek(self):
        temp=self.front
        print("The top ele is",temp.data)
q1=Queue()
print("*****************QUEUE*******************")
while(True):
    print("1.enqueue,2.dequeue,3.Display,4.Peek,5.Exit")
    Opt=int(input("Enter your option:"))
    if(Opt==1):
        q1.enqueue()
    elif(Opt==2):
        q1.dequeue()
    elif(Opt==3):
        q1.display()
    elif(Opt==4):
        q1.peek()
    elif(Opt==5):
        break
    else:
        print("Invalid option/Please try again")










































    

