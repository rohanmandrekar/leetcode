class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        dd=abs(dividend)
        dv=abs(divisor)
        ans=0

        while dd>=dv:
            temp=dv
            mul=1
            while dd>=temp:
                dd-=temp
                ans+=mul
                mul+=mul
                temp+=temp
        if (dividend<0 and divisor>0) or (divisor<0 and dividend>0):
            ans*=-1

        return min(2147483647,max(-2147483648,ans))     