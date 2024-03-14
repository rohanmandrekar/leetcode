##class Solution:
##    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
##        dic={}
##        ans=[]
##        for num in nums:
##            if num not in dic:
##                dic[num]=1
##            else:
##                dic[num]+=1
##        for i in range(0,k):
##            ans.append(max(dic,key=dic.get))
##            del dic[max(dic,key=dic.get)]
##        return ans   

##class Solution:
##    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
##        dic={}
##        ans=[]
##        freq=[[] for i in range(len(nums)+1)]
##        for num in nums:
##            dic[num]=1+dic.get(num,0)
##        for n,c in dic.items():
##            freq[c].append(n)
##
##        for i in range(len(nums),0,-1):
##            for val in freq[i]:
##                ans.append(val)
##                if len(ans)==k:
##                    return ans        

           
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dic={}
#         for n in nums:
#             dic[n]=1+dic.get(n,0)  
#         ans=dict(sorted(dic.items(), key=lambda item: item[1])[-k:])
#         return ans.keys()

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        ans=sorted(dic.keys(),key=dic.get,reverse=True)
        return ans[:k]       