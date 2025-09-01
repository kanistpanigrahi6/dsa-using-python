class Solution(object):
    def reverse(self, x):
        rev=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x>0:
            last_digit=x%10
            rev=rev*10+last_digit
            x//=10
        return sign*rev
        


        
