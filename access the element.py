import array
# from operator import index
arr1=array.array('i',[1,2,3,4,5,6,7])
def access(array,index):
    if index>=len(array):
        print("index out of range")
    else:
        print(array[index])
access(arr1,5)