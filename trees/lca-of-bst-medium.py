# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #leetcode does not guarentee which of p and q will be higher/lower
        if p.val > q.val:
            p, q = q, p
            
        if p.val <= root.val <= q.val:
            return root

        if p.val < q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)