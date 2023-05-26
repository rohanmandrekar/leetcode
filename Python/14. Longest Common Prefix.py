class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        
        l=999
        
        for word in strs:
            if len(word)<l:
                l=len(word)
        
        for i in range(0,l):
            flag=0
            x=strs[0]
            y=x[i]
            
            for word in strs:
                if word[i]==y:
                    flag+=1
            if flag==len(strs):
                ans+=y
            elif flag<len(strs):
                break
                
        return ans       
                