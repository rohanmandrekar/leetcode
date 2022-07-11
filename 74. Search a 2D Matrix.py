class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l1 in matrix:
            if l1[0]<=target and l1[-1]>=target:
                
                l=0
                r=len(l1)-1
                
                while l<=r:
                    mid=(l+r)//2
                    if l1[mid]==target:
                        return True
                    elif l1[mid]>target:
                        r=mid-1
                    else:
                        l=mid+1
        return False