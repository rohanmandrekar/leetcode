class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h==len(piles):
            return max(piles)
        l=1
        r=max(piles)
        ans=r

        while l<=r:
            k=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            if hours<=h:
                ans=min(ans,k)
                r=k-1
            else:
                l=k+1
        return ans 