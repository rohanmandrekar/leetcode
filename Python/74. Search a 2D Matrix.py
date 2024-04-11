class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return false
        for i in range (len(matrix)):
            if target<matrix[i][-1] and target>matrix[i][0]:
                l=0
                r=len(matrix[i])  
                while l<r:
                    m=(l+r)//2  
                    if matrix[i][m]==target:
                        return True
                    elif matrix[i][m]>target:
                        r=m-1
                    else:
                        l=m+1
        return False