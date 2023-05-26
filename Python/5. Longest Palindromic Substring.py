class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=''
        for i in range(0,len(s)):
            l=i
            r=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
                
            if len(s[l+1:r])>len(ans):
                ans=s[l+1:r]
            
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
                
            if len(s[l+1:r])>len(ans):
                ans=s[l+1:r]
            
        return ans       
    
            
        
        
        