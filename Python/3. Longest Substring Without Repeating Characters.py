class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans=0
        repeat=set()
        for i in range(len(s)):
            while s[i] in repeat:
                repeat.remove(s[l])
                l+=1
            repeat.add(s[i])
            ans=max(ans,i-l+1)
            
        return ans    
                
        