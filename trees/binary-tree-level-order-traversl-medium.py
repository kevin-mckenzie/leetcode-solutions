# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        def dfs(p, level):
            if not p:
                return
            if level >= len(levels):
                levels.append([])
            levels[level].append(p.val)
            dfs(p.left, level + 1)
            dfs(p.right, level + 1)
        
        dfs(root, 0)
        return levels
    