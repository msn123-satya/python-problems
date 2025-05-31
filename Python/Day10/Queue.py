front=-1
rear=-1
size=int(input("enter size:"))
q=[]
def enqueue():
    global front,rear
    if(rear==size-1):
        print("Queue is overflow")
    else:
        if(front==-1):
            front=0
        rear=rear+1
        ele=int(input("enter value:"))
        q.append(ele)
def dequeue():
    global front,rear
    if(front==-1):
        print("Queue is underflow/empty")
    elif(front!=rear):
        ele=q.pop(0)
        print("The del ele is:",ele)
        front=front+1
    else:
        ele=q.pop(0)
        print("The del ele is:",ele)
        front=-1
        rear=-1
def display():
    if(front!=-1):
        for p in range(0,len(q)):
            print(q[p],end=" ")
        print()
    else:
        print("Queue is empty, no ele is in the list")
def peek():
    if(front!=-1):
        print("The top ele is:",q[0])
    else:
        print("Queue is empty, no top ele is in the list")
print("******************QUEUE******************")

while(True):
    print("1.enqueue,2.dequeue,3.display,4.peek,5.exit")
    opt=int(input("Select your operation for the QUEUE:"))
    if(opt==1):
        enqueue()
    elif(opt==2):
        dequeue()
    elif(opt==3):
        display()
    elif(opt==4):
        peek()
    elif(opt==5):
        break
    else:
        print("Invalid option")
        
    
