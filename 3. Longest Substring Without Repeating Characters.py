class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        temp=[]
        templist=[]
        
        if s=="":
            return 0
        elif len(s)==1:
            return 1
        else:
            string=list(s)
            # print(string)
        
            for i in range (0,len(string)):
            
                for j in range(i,len(string)):
                    # print(string[j])
                    # print(temp)
                    if string[j] not in temp:
                        temp.append(string[j])
                    elif string[j] in temp:
                        templist.append(len(temp))
                        temp.clear()
                        break
         
            ans=max(templist)
            return ans
                           
                    
            
            