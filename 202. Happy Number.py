class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        count=0
        while sum!=1:
            sum=0
            
            n=str(n)
            for num in n:
                sum += int(num)*int(num)
            # print(sum)
            count +=1
            if count==7:
                return False
            if sum==1:
                return True
            else:
                n=sum