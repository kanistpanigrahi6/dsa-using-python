def printunorder(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]<arr2[j]:
                print(arr1[i],arr2[j])

inp1=list(map(int,input().split()))
inp2=list(map(int,input().split()))
printunorder(inp1,inp2)

####### o(ab) runtime complexity
