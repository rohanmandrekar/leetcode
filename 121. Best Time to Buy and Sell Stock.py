class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        ans=0
        for r in range(1,len(prices)):
            if prices[r]<prices[l]:
                l=r
            ans=max(ans,prices[r]-prices[l])
        return ans    