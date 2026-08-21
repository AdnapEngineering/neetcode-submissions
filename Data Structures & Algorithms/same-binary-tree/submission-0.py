# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      # base cases: 
      # both are empty > one is not the other is empty > values don't match
        if not p and not q:
            return True
        if not p or not q:
            return False
        if  p.val != q.val:
            return False

        left_match = self.isSameTree(p.left , q.left)
        right_match = self.isSameTree(p.right, q.right)
        return left_match and right_match

