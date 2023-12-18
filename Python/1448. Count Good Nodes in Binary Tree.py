# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root,biggest):
            if not root:
                return 0
            if root.val>=biggest:
                ans = 1
                biggest=root.val
            if root.val<biggest:
                ans=0
                

            ans+=dfs(root.left,biggest)    
            ans+=dfs(root.right,biggest)
            return ans
        return dfs(root,root.val)    