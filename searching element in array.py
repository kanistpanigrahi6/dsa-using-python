import array
arr1=array.array('i',[4,5,2,7,8])
def search(array,targett):
    for i in range(len(array)):
        if array[i]==targett:
            return i
    return -1
print(search(arr1,7))