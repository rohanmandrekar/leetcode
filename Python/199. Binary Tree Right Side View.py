# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        q=collections.deque([root])

        while q:
            l=len(q)
            right=None
            for i in range(l):
                n=q.popleft()
                if n:
                    right=n
                    q.append(n.left)
                    q.append(n.right)
            if right:
                ans.append(right.val)
        return ans      