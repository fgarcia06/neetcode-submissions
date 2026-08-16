# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we would want to use dfs

        # get the depth, give the child's depth to the parent

        # diameter would be the maximum left + right path

        diameter = 0

        def dfs(node):
            if node is None:
                return 0
            
            nonlocal diameter
            
            left = dfs(node.left)
            right = dfs(node.right)

            # longest path
            diameter = max(diameter, left+right)

            # height of this subtree
            return 1 + max(left, right)
        
        dfs(root)

        return diameter