class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        i=j=len(nums)-1
        while j>-1:
            if nums[j]==val:
                nums[i],nums[j]=nums[j],nums[i]
                count+=1
                i-=1
            j-=1    
        return len(nums)-count 