class Solution:
    def romanToInt(self, s: str) -> int:
        {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        
        i=0
        ans=0
        while i<len(s):
            if i<len(s)-1 and s[i]=='C' and s[i+1]=="M":
                ans+=900
                i+=2
            elif s[i] =='M':
                ans+=1000
                i+=1
            elif i<len(s)-1 and s[i]=='C' and s[i+1]=="D":
                ans+=400
                i+=2
            elif s[i] =='D':
                ans+=500
                i+=1
            elif i<len(s)-1 and s[i]=='X' and s[i+1]=="C":
                ans+=90
                i+=2
            elif s[i] =='C':
                ans+=100
                i+=1    
            elif i<len(s)-1 and s[i]=='X' and s[i+1]=="L":
                ans+=40
                i+=2
            elif s[i] =='L':
                ans+=50
                i+=1
            elif i<len(s)-1 and s[i]=='I' and s[i+1]=="X":
                ans+=9
                i+=2
            elif s[i] =='X':
                ans+=10
                i+=1   
            elif i<len(s)-1 and s[i]=='I' and s[i+1]=="V":
                ans+=4
                i+=2
            elif s[i] =='V':
                ans+=5
                i+=1
            elif s[i]=='I':
                ans+=1
                i+=1
                
        return ans        