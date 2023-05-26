class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        if len(t)>len(s):
            return ""
        if t==s:
            return s    
        l=0
        
        countT={}
        window={}
        have=0

        ans=[-1,-1]

        anslen=float("infinity")
        s1=set()
        for c in t:
            s1.add(c)
            countT[c] = 1 + countT.get(c,0)

        need=len(s1)    

        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in countT and countT[c]==window[c]:
                have+=1
            while have==need:
                #window[l]=window.get(l,0)-1
                if (r-l+1)<anslen:
                    anslen=r-l+1
                    ans=[l,r]
                window[s[l]]-=1

                if s[l] in countT and countT[s[l]]>window[s[l]]:
                    have-=1
                l+=1    

        l,r=ans
        if anslen==float("infinity"):
            return ""
        else:
            return s[l:r+1]    
                