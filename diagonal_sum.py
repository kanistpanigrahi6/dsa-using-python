def diagonal_sum(myList2D):
    total=0
    for i in range(len(myList2D)):
        total=total+myList2D[i][i]
    return total
        
    
myList2D=   [[1,2,3],
            [4,5,6],
            [7,8,9]] 
diagonal_sum(myList2D)