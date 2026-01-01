import array
#create an array and traverse
arr=array.array('i',[1,2,3,4,5])
for i in arr:
    print(i)
#access elements by index
print(arr[0])
#append elements
arr.append(6)
print(arr)
#insert elements at specific position
arr.insert(0,10)
print(arr)
#extend array
arr1=array.array('i',[7,8,9])
arr.extend(arr1)
print(arr)
#add elements from list using fromlist()
list=[10,11,12]
arr.fromlist(list)
print(arr)
#remove elements using remove()
arr.remove(3)
print(arr)
#remove elements using pop()
arr.pop()
print(arr)
#fetch index of an element using index()
print(arr.index(4))
#reverse the array
arr2=array.array('i',[30,31,32,33])
arr2.reverse()
print(arr2)
#buffer info
print(arr2.buffer_info())
#count occurrences of an element
print(arr.count(10))
#convert array to list using tolist()
print(arr.tolist())
#slice elements from array
print(arr[2:6])