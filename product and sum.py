def sumandpro(arr):
    sum=0
    product=1
    for num in arr:
        sum=sum+num
    for num in arr:
        product=product*num
    print("sum is:",str(sum)+  "\nproduct is:",str(product))
input=list(map(int,input().split()))
sumandpro(input)
