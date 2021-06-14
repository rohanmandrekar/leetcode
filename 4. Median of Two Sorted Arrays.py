import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged=[]
        
        
        while len(nums1)!=0 and len(nums2)!=0:
            
            if nums1[0]<nums2[0]:
                merged.append(nums1[0])
                nums1.pop(0)
            elif nums1[0]>nums2[0]:
                merged.append(nums2[0])
                nums2.pop(0)
            else:
                merged.append(nums1[0])
                nums1.pop(0)
                    
            # else:
            #     break
        if len(nums1)==0:
            for i in nums2:
                merged.append(i)
            
        elif len(nums2)==0:
            for i in nums1:
                merged.append(i)
        
        print(merged)
        if len(merged)%2==1:
            median=merged[int(len(merged)/2)]
        if len(merged)%2==0:
            print(math.floor(len(merged)/2))
            print(math.ceil(len(merged)/2))
            median=(merged[math.floor(len(merged)/2)-1]+merged[math.ceil(len(merged)/2)])/2
            
        return float(median)    