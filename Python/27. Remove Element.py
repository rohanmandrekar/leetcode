class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            for i in range(len(nums)):
                if nums[i]==val:
                    nums[i]=None
                    for j in range(i,len(nums)-1):
                        temp=nums[j]
                        nums[j]=nums[j+1]
                        nums[j+1]=temp
                    
        ans=[]
        for v in nums:
            if v!=None:
                ans.append(v)
        return len(ans)