# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = { value: index for index, value in enumerate(inorder)} #inorder_map[value of inorder] returns index
        pre_index = 0 # start at root

        def helper_rec(in_left, in_right):
            nonlocal pre_index
            # base case of window collapsed and nothing more to process
            if in_left > in_right: return None 

            # grab root from pre-order, find index in inorder_map, and  create new root node
            root_value = preorder[pre_index]
            pre_index +=1
            root = TreeNode(root_value)

            # Locate root in inorder to split left and right subtrees
            mid = inorder_map[root_value]
            root.left = helper_rec(in_left, mid-1)
            root.right = helper_rec( mid + 1, in_right)

            return root

        return helper_rec(0, len(inorder) - 1)      