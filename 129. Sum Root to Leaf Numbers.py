# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, current_sum):
        if not node:
            return 0  
        current_sum = current_sum * 10 + node.val     
        if not node.left and not node.right:
            return current_sum   
        return self.dfs(node.left, current_sum) + self.dfs(node.right, current_sum)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        return self.dfs(root, 0)
        