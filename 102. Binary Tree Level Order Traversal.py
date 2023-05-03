# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        q=collections.deque()
        q.append(root)

        while q:
            l=len(q)
            level=[]
            for i in range(l):
                n=q.popleft()
                if n:
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if level!=[]:        
                ans.append(level)
        return ans            