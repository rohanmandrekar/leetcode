class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maximum=0
        
        for n in nums:
            if (n-1) not in numset:
                m=1
                while (n+m) in numset:
                    m+=1
                maximum=max(maximum,m)
        return maximum          
    