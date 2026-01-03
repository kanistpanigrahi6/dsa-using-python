def middle(myList):
    arr=[]
    for i in range(1,len(myList)-1):
        arr.append(myList[i])
    return arr
myList=[1,2,0,5,6,8,93]
print(middle(myList))
        