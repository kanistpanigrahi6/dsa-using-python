
# def missing_number(arr, n):
#     for i in range(1,n+1):
#         if i not in arr:
#             print("The missing number is:", i)
#             return i

# print(missing_number([1, 2, 3, 4, 6], 6))

def missing_number_sum(arr, n):
    s=set(arr)
    for i in range(1,n+1):
        if i not in s:
            print("The missing number is:", i)
            return i

print(missing_number_sum([1, 2, 3, 4, 6], 6))
