class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans=sum(nums[:3])
        
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if abs(s-target)<abs(ans-target):
                    ans=s
                if s<target:
                    l+=1
                else:
                    r-=1
        return ans                    
        