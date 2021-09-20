class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        i=len(digits)-1
        for num in digits:
            a=a+(num*(10**i))
            i=i-1
            
        a+=1
        a=str(a)
        # a=a.split()
        ans=[]
        
        for num in a:
            ans.append(num)
        
        return ans