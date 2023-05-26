class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if haystack==needle:
            return 0
        if not needle:
            return 0
        a=len(needle)
        for i in range (len(haystack)-len(needle)+1):
            if haystack[i:i+a]==needle:
                return i
                
                
            
        return -1    