def mergeTwoLists(list1, list2):
    res=list1+list2
    print(res)
    for i in range(len(res)):
        for j in range(i+1,len(res)):
            if res[i]>res[j]:
                res[i],res[j]=res[j],res[i]
    return res
print(mergeTwoLists([1,2,4],[1,3,4])) 