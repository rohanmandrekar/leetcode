class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1 or len(s)<=numRows:
            return s
        ans=''
        r=[[] for num in range(0,numRows)]
        i=0
        flag=-1
        for letter in s:           
            r[i].append(letter)
            if i==0 or i==numRows-1 :
                flag=flag*(-1)
                
            if flag==-1:
                i-=1
            else:
                i+=1

        for row in r:
            for val in row:
                ans+=val
        return ans    
            
            
                
            
            