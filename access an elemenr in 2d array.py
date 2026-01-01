import numpy as np
arr1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
def acess(arr,rowindex,columnindex):
    if rowindex>=len(arr) or columnindex>=len(arr[rowindex]):
        print("incorrect element")
    else:
        print(arr[rowindex][columnindex])
acess(arr1,2,4)