class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(',']':'[','}':'{'}
        for val in s:
            if val not in dic:
                stack.append(val)
            elif not stack or dic[val]!=stack.pop():
                return False    
        return not stack
                    
