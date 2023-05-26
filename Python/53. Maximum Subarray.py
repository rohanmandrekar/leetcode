class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans=nums[0]
        temp=0
        
        for n in nums:
            temp+=n
            ans=max(ans,temp)
            if temp<0:
                temp=0
        return ans 