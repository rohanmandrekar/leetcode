class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x<2:
            return x

        low,high=1,x

        while low<=high:
            mid=int((low+high)/2)
            
            y=mid*mid
            if y==x:
                return mid
            elif y<x:
                low=mid+1
            else:
                high=mid-1

        return high 
