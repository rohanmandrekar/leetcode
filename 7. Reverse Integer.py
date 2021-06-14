class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        flag=0
        if x<0:
            x=x*(-1)
            flag=1
        while x>1:
            ans=(ans*10)+x%10
            x/=10
            x=int(x)
        if x!=0:    
            ans=(ans*10)+x
        if flag==1:
            ans=ans*(-1)
        if ans>(2**31)-1 or ans<-(2**31):
            ans=0 
        return ans