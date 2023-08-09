class Solution:
    def countAsterisks(self, s: str) -> int:
        l=0
        c=0
        for val in s:
            if val=='|':
                l+=1
            elif l%2==0:
                if val=='*':
                    c+=1
        return c                