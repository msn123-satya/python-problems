top=-1
stack=[]
size=int(input("enter size:"))
def push():
    global top
    if (top>=size-1):
        print("Stack is full/Overflow")
    else:
        top=top+1
        ele=int(input("enter ele:"))
        stack.append(ele)
def display():
    for p in range (len(stack)-1,-1,-1):
        print(stack[p],end=" ")
def pop():
    global top
    if(top==-1):
        print("Empty")
    else:
        ele=stack.pop()
        print("The del ele is:",ele)
        top=top-1
def peek():
    ele=stack[top]
    print("The top ele is:",ele)
print("*****************STACK*******************")
while(True):
    print("1.Push,2.Pop,3.Display,4.Peek,5.Exit")
    Opt=int(input("Enter your option:"))
    if(Opt==1):
        push()
    elif(Opt==2):
        pop()
    elif(Opt==3):
        display()
    elif(Opt==4):
        peek()
    elif(Opt==5):
        break
    else:
        print("Invalid option/Please try again")
        
        
            
