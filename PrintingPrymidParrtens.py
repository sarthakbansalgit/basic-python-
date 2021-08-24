# Simple Prymid Parrtens

def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print(" ")
n = 5
pypart(n)

# Reverse Prymid Parrtens

rows = 5
for i in range(rows + 1,0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
print(" ")

#Numeric pattern

k = 1
for i in range(0, 5):
    for j in range(0, i+1):
        print(k, end=" ")
        k = k + 1
    print()
#Repetiton Numeric Parrten in python

for num in range(10):
    for i in range(num):
        print (num, end=" ")
    print(" ")
#Character pattern

value = 65
for i in range(0, 5):
    for j in range(0, i+1):
        ch = chr(value)
        print(ch, end=" ")
        value = value + 1
    print()


#ABCD Character pattern

inc = 1
for i in range(0, 5):
    for j in range(0,inc):
        ch = chr(value)
        print(ch, end=" ")
        value = value + 1
        inc = inc + 2
    print()

# Square Pattern

square_side = int(input("Please Enter dimension of square  : "))
print("Star Square  Pattern")
for i in range(square_side):
    for i in range(square_side):
        print('*', end = '  ')
    print()
