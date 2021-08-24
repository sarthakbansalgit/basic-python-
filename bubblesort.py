list = [21,4,32,1  ,5,6,7,99,43,11]
for i in range (len(list)-1,0,-1):
    for j in range (i):
        if list[j]>list[j+1]:
            list[j],list[j+1] = list[j+1] , list[j]

print(list)
