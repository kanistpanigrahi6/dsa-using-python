import array
arr1=array.array('i',[2,4,5,6,7,8])
def traverse(array):
    for i in range(len(array)):
        print(array[i])
traverse(arr1)