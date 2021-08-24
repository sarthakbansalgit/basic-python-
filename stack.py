stk = []
def push(val,stk):
    stk.append(val)

def peek(stk):
    index = len(stk)-1
    print("Element = ", index)

def isEmpty(stk):
    if len(stk) == 0 :
        print("its underflow")
    else:
        print("hai abhi maal")

def display(stk):
     for i in range (len(stk)-1,-1,-1):
         print(stk[i])

def pop(stk):
    vall= stk.pop()
    print("The Poped Item is = ", vall)


while True:
    print("Its a Stack Python Program")
    print("1.push")
    print("2.peek")
    print("3.display")
    print("4.pop")
    print("5.exit")
    a = int(input("Enter Your Choice: "))
    print(a)
    if a == 1:
     val = int(input("Enter The Value to Push: "))
     push(val,stk)
    elif a == 2:
     if len(stk)== 0:
         print("Its Empty Bro Kya Dhekoge? ")
     else:
         peek(stk)
    elif a == 3:
     if len(stk) == 0:
         print("Khalli h Bro")
     else:
         display(stk)
    elif a == 4:
     if len(stk) == 0:
        print("Khalli h Bro")
     else:
        pop(stk)
    elif a == 5:
        print("exiting.....")
        break
