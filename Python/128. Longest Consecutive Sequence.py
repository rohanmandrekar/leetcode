##class Solution:
##    def longestConsecutive(self, nums: List[int]) -> int:
##        numset=set(nums)
##        maximum=0
##        
##        for n in nums:
##            if (n-1) not in numset:
##                m=1
##                while (n+m) in numset:
##                    m+=1
##                maximum=max(maximum,m)
##        return maximum          
##    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        max_l=1
        l=1

        for i in range(1,len(nums)):
            if nums[i]-1==nums[i-1]:
                l+=1
            else:
                max_l=max(l,max_l)
                l=1
        max_l=max(l,max_l)        
        return max_l                   
    
