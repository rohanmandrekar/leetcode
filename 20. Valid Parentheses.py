class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stack=[]
        dic={')':'(',']':'[','}':'{'}
        for val in s:
            if (val=='{' or val=='[' or val=="("):
                
                stack.append(val)
            if (val=="}" or val ==')' or val==']'):
                if not stack:
                    return False
                if stack and stack[-1]!=dic[val]:
                    return False
                elif stack and stack[-1]==dic[val] :
                    stack.pop()
       
        return not stack
                    