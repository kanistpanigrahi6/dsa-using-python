class solution
  def diagonal_sum(self,matrix):
      sum1 = 0
      for i in range(len(matrix)):
          sum1 += matrix[i][i]
      print(sum1)
 

