class Solution(object):
    def findClosest(self, x, y, z):
        diff1=abs(z-x)
        diff2=abs(z-y)
        if diff1 < diff2:
            return 1
        elif diff2 < diff1:
            return 2
        elif diff1==diff2:
            return 0
        
        
