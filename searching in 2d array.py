import numpy as np
arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
def search(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==target:
                return str(i)+ str(j)
    return "element not found"
print(search(arr1,7))

