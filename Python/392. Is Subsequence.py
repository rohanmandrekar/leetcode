class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s=="":
            return True

        ptr=0

        for val in t:
            if s[ptr]==val:
                ptr+=1
                if ptr==len(s):
                    return True
        return False   