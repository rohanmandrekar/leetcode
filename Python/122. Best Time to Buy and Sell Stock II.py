class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        j=0
        for i in range(1,len(prices)):
            if prices[i]>prices[j]:
                ans+=prices[i]-prices[j]
            j+=1    
        return ans        
