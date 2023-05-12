# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #ITERATIVE
        
        ans=[]
        stack=[]
        curr=root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left 
            curr=stack.pop()
            ans.append(curr.val)
            curr=curr.right
        return ans        

        #RECURSION

        # ans=[]
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     ans.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return ans        