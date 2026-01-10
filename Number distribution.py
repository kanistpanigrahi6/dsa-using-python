n=int(input())
arr=list(map(int,input().split()))
pos=0
neg=0
nue=0
for num in arr:
    if num==0:
        nue=nue+1
    elif num>0:
        pos=pos+1
    else:
        neg=neg+1
print(nue,pos,neg)
