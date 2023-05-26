class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z'],}
        
        if digits=='':
            return []
        
        ans=[]
        
        def backtrack(i,temp):
            if len(temp)== len(digits):
                ans.append(temp)
                return
            for char in dic[int(digits[i])]:
                backtrack(i+1,temp+char)
         
        backtrack(0,"")
        return ans
            