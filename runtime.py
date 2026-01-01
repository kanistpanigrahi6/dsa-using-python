import array
arr1=array.array('i',[1,2,3,4,5])
def runtime(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            print(array[i],",",array[j])
runtime(arr1)