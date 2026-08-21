# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            if left_height == -1: 
                return -1

            right_height = dfs(node.right)
            if right_height == -1: 
                return -1
            # Are the two sides unbalanced at THIS node?
            if abs(left_height - right_height) > 1:
                return -1
            
            # If it is balanced, return the actual height of this node
            return 1 + max(left_height, right_height)

        return dfs(root) != -1

