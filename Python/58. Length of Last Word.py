class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # a= s.split()
        # a=a[-1]
        # return len(a)
        ptr=len(s)-1
        while s[ptr]==" ":
            ptr-=1
        c=0
        for i in range(ptr,-1,-1):
            if s[i]==" ":
                return c
            c+=1
        return c  
