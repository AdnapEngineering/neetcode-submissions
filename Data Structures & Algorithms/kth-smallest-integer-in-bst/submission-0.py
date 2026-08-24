# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        result = None

        def inorderDfs(node: Optional[TreeNode]):
            nonlocal count, result
            if not node or result is not None: return
            # if result is set or node is None we have the answer 
            inorderDfs(node.left) # in order so start at bottom of left tree
            count += 1
            if count == k: 
                result = node.val
            inorderDfs(node.right) 
        inorderDfs(root)
        return result