a = []
def enqueue(a,val):
    a.append(val)
    if len(a) == 1:
        front = rear = 0
    else:
        rear = (len(a)-1)

def dequeue(a):
    if len(a) == 0:
        print("bruh kuch ni h vha")
    else:
     s = a.pop()
     print("the element deleted was",s)
     if len(a) == 0:
        front = rear = None



def peek(a):
    if len(a) == 0:
        print("bruh kuch ni h vha")
    else:
       front = 0
       print(a[front])
def display(a):
    if len(a) == 0:
        print("bruh kuch ni h vha")
    else:
        for i in range(len(a)):
            print(a[i])

fornt = rear =  None
while True:
    ch =  int(input('1->Enqueue \n2->dequeue \n3->Peek \n4->Display \n5->exit \n :'))
    if ch == 1:
        val =  int(input("Enter The Value to enter into List: "))
        enqueue(a,val)
    elif ch == 2:
        dequeue(a)
    elif ch == 3:
        peek(a)
    elif ch == 4:
        display(a)
    elif ch == 5:
        print("ok breaking it...")
        break
