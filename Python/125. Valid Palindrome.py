class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for val in s:
            if val.isalnum():
                a.append(val.lower())
        return a==a[::-1]           
            
        