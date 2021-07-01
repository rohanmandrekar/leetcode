class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans=[]
        stack=[]
        def run(openn,closen):
            
            if openn==closen==n:
                ans.append("".join(stack)) 
                return
            if openn<n:
                stack.append('(')
                run(openn+1,closen)
                stack.pop()
            if closen<openn:
                stack.append(')')
                run(openn,closen+1)
                stack.pop()
            
        run(0,0)
        return ans