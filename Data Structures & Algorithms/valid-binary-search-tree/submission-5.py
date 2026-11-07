# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validTree(node, left, right):
            if not node: return True
            if not (left < node.val < right): return False
            return validTree(node.left, left, node.val) and validTree(node.right, node.val, right)

        return validTree(root, float("-inf"), float("inf"))
        
        
