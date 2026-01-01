class solution
  def pair_sum(myList, sum):
      count=[]
      for i in range(len(myList)):
          for j in range(i+1,len(myList)):
              if myList[i]+myList[j]==sum:
                  count.append((myList[i],myList[j]))
      print(count)
