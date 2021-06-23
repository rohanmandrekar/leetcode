class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1 or numRows>=len(s):
            return s
        
        r=[[] for num in range(0,numRows)]
        flag=-1
        row=0
        
        for char in s:
            r[row].append(char)
            if row==0 or row==numRows-1:
                flag=flag*(-1)
            row+=flag
        ans=''    
        for row in r:
            for char in row:
                ans+=char            
        return ans
                
            
            