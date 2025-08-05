def permu(list1,list2):
    if len(list1)!=len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False
list1=['a','b','c','d','e']
list2=['a','b','c','d','e']
print(permu(list1,list2))


# def permu(list1,list2):
#     list1.sort()
#     list2.sort()
#     print(list1,list2)
#     if list1==list2:
#         print("permutation")
#     else:
#         print("not ")
# list1=['a','c','b']
# list2=['a','b','d']
# permu(list1,list2)
