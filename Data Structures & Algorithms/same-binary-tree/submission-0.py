# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.issame = True
        def preorder(p, q):
            if not p and not q:
                return None
            if (not p and q) or (not q and p):
                self.issame = False
                return None
            if p.val != q.val:
                self.issame = False
                return None
            print(p.val, q.val)
            preorder(p.left, q.left)
            preorder(p.right, q.right)
        preorder(p, q)
        return self.issame
            
