class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=['+','-','*','/']
        stack=[]
        
        for val in tokens:
            if val not in op:
                stack.append(int(val))
            else:
                a=stack[-1]
                stack.pop()
                b=stack[-1]
                stack.pop()
                if val == '+':
                    stack.append(a+b)
                elif val=='-':
                    stack.append(b-a)
                elif val=='*':
                    stack.append(a*b)
                elif val=='/':
                    stack.append(int(b/a)) 
        return stack[0] 