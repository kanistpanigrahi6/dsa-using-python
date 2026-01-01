n=int(input("Enter the no of days="))
total=0
temperatures=[]
for i in range(n):
    nxtday=int(input("enter the temp on day"+str(i+1)))
    temperatures.append(nxtday)
    total=total+temperatures[i]
avg=total//n
print("average temp is="+str(avg))

res=0
for i in range(len(temperatures)):
    if temperatures[i]>avg:
        res=res+1
print("no of days above average temp="+str(res))