class Solution:
    def myAtoi(self, s: str) -> int:
        
        ans=0
        i=0
        a=set('0123456789')
        
        if s=="":
            return 0
        
        while i<len(s) and s[i]==' ':
            i+=1
        if i<len(s)-1 and s[i]=='-' and s[i+1]=='+':
            return 0
        if i<len(s)-1 and s[i]=='+' and s[i+1]=='-':
            return 0
        sign=1
        
        if i<len(s) and s[i]=='-':
            sign=-1
            i+=1
        if i<len(s) and s[i]=='+':
            sign=1
            i+=1
        
        
        while i<len(s) and s[i] in a:
            ans=(ans*10)+int(s[i])
            i+=1
        ans=ans*sign
        if ans<0:
            return max(ans,(-2**31))
        else:
            return min(ans,(2**31)-1)
            
        
        