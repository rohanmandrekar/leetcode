class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if len(heights)==1:
            return heights[0]

        ans=heights[0]
        # for i in range (len(heights)):
        #     j=i
        #     width=1
        #     while j+1<len(heights) and (heights[j]<=heights[j+1]):
        #             j+=1
        #             width+=1
        #     ans=max(ans,width*heights[i])
        # return ans
        stack=[]
        for i in range(len(heights)):
            start=i

            while stack and stack[-1][0]>heights[i]:
                h,pos=stack.pop()
                ans=max(ans,(i-pos)*h)
                start=pos
            stack.append([heights[i],start])

        for h,i in stack:
            ans=max(ans,h*(len(heights)-i))
        return ans    
