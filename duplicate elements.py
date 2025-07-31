class solution
  def remove_duplicates(self,arr):
      arr.sort()
      for i in range(len(arr)-1):
          if arr[i]!=arr[i+1]:
              print(arr[i])
      print(arr[-1])
  
 
