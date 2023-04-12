class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if nums==[]:
            return[-1,-1]
        
        def binarysearch1(nums,target,leftbias):
            l,r=0,len(nums)-1
            ans=-1
            
            while l<=r:
                mid=(l+r)//2

                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    ans=mid

                    if leftbias==True:
                        r=mid-1
                    else:
                        l=mid+1    
            
            return ans     

        left=binarysearch1(nums,target,True)
        right=binarysearch1(nums,target,False)
        
        return [left,right]    