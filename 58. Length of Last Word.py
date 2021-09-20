class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a= s.split()
        a=a[-1]
        return len(a)