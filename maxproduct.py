def maxproduct(arr):
    res=sorted(arr)
    x=res[-1]
    y=res[-2]
    return x*y
print(maxproduct([1,7,3,4,9,5]))

def maxproduct(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i] 
    return arr[0]*arr[1]
print(maxproduct([1,7,3,4,9,5]))


