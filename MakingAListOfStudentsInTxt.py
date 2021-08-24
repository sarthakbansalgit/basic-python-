#Open A  Txt File And Write The Following Data
#  Names (By Input)
# And Their RollNumbers
p =  open("example.txt",'w')
num =  int(input("Enter The Number OF Students: "))
for i in range(num):
    r = int(input("Enter Your Roll Number: "))
    n = input("Enter The Name: ")
    s = (str(r)+""+'-'+""+n)
    p = open("example.txt",'w')
    p.write(s)
    p.close()
