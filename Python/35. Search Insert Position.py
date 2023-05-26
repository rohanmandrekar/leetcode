class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(0,len(nums)):
            if target==nums[i]:
                return i
            elif nums[0]>target:
                return 0
            elif nums[len(nums)-1]<target:
                return len(nums)
            elif i!= len(nums)-1:
                if nums[i]<target and nums[i+1]> target:
                    return i+1