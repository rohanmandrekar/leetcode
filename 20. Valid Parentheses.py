class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        dic={")":"(","}":"{","]":"["}
        
        for brac in s:
            if brac in dic and stack:
                if stack[-1]==dic[brac]:
                    stack.pop()
                else:
                    return False
             
            else:
                stack.append(brac)
         
        if not stack:
            return True