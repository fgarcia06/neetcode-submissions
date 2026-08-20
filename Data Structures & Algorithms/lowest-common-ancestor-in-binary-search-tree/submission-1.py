# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
    
        if node is None or node is p or node is q:
            return node
        
        left = self.lowestCommonAncestor(node.left, p, q)
        right = self.lowestCommonAncestor(node.right, p, q)

        if left is not None and right is not None:
            return node
        
        if left is not None:
            return left
        
        return right