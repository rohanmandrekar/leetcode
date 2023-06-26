class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # c=0
        # while n:
        #     n=n&(n-1)
        #     c+=1
        # return c    
        
        ans=0
        while n:
            ans+=n%2
            n=n>>1
        return ans    