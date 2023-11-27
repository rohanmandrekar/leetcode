class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic={0:0}
        for row in wall:
            s=0
            for i in range(len(row)-1):
                s+=row[i]
                dic[s]=1+dic.get(s,0)
        
        return len(wall)-max(dic.values())