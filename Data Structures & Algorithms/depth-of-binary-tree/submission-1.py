# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # do a bfs and increase depth as we move to the next level
        queue = []
        depth = 0
        queue.append(root)

        if root is None:
            return 0

        while queue:
            
            for _ in range(len(queue)):
                node = queue.pop(0)

                # if there is a left child
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            depth += 1
        
        return depth