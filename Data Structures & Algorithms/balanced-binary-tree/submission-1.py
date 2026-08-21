# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node) -> (isBalanced, height):
            if node is None:
                return (True, 0)

            left_balance, left_height = dfs(node.left)
            right_balance, right_height = dfs(node.right)

            if abs(left_height - right_height) <= 1 and left_balance and right_balance:
                return (True, 1 + max(left_height, right_height))
            else:
                return (False, 1 + max(left_height, right_height))
        
        return dfs(root)[0]


