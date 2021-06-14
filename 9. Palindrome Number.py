class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1=0
        b=x
        if x<0:
            # print('here')
            return False
        while x>0:
            s1=int((s1*10)+x%10)
            x/=10
            x=int(x)
        s1=int(s1)
        print(s1)
        if s1==b:
            print('here')
            return True
            