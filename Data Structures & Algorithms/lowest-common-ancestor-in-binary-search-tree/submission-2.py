# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxi = max(p.val, q.val)
        mini = min(p.val, q.val)
        if not root:
            return None
        if mini <= root.val <= maxi:
            return root
        if root.val > maxi:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < mini:
            return self.lowestCommonAncestor(root.right, p, q)

