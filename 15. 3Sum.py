class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        ans1=set()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    ans.append([nums[i],nums[l],nums[r]])        
                    l=l+1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    while nums[r]==nums[r+1] and r>l:
                        r-=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                    while nums[r]==nums[r+1] and r>l:
                        r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans  