class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
                return '1'
        
        def cas(num):
            
            num=str(num)    
            a=0
            ans=''
            while a<len(num):
                c=1
                v=num[a]
                while a<len(num)-1 and num[a]==num[a+1] :
                     c+=1
                     a+=1

                ans+=str(c)
                ans+=str(v)
                a+=1
            return ans

        ans=1
        for i in range(n-1):
            ans=cas(ans) 
            print(ans)

        return ans 