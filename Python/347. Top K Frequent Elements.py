class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        ans=[]
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        for i in range(0,k):
            ans.append(max(dic,key=dic.get))
            del dic[max(dic,key=dic.get)]
        return ans   