class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return "0"

        ans=[0]*(len(num1)+len(num2))

        num1,num2=num1[::-1],num2[::-1]

        for i1 in range (len(num1)):
            for i2 in range (len(num2)):
                d=int(num1[i1])*int(num2[i2])
                ans[i1+i2]+=d
                ans[i1+i2+1]+=ans[i1+i2]//10
                ans[i1+i2]=ans[i1+i2]%10

        ans=ans[::-1]
        s=0

        while s<len(ans)  and ans[s]==0:
            s+=1
        ans=map(str,ans[s:])      
        return ''.join(ans)    
