def bsearch(n,key):
    low = 0
    mid = 0
    high = len(n)-1

    while low <= high:
        mid = (low+high)//2
        if n[mid]< key:
            low = mid+1
        elif n[mid]> key:
            high = mid-1
        else:
            return mid
    return -1
n = [1,2,3,4,5,6,7,8,9]
key = 7
result = bsearch(n,key)
if result == -1:
    print("Its Nor HERE mf")
else:
    print("Yes Its Here Mf  ", str(result)   )
