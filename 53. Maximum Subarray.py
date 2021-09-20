class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest=sum(nums)
        # temp=0
        for j in range (0,len(nums)):
            temp=0
            for i in range(j, len(nums)):
                temp=temp+nums[i]
                if temp>largest:
                    largest=temp
                if temp<0:
                    break
                
        return largest   