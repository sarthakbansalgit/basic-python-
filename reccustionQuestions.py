# sum from 1 to n by recurssion
def sum(n):
    if n == 1:
        return 1
    else:
        return (n+sum(n-1))
n =  int(input("Enter The Number: "))
R = sum(n)
print(R)

# print one string in reverse order using recurssion

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))

