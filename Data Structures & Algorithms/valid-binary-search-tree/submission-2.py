# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.state = True
        def dfs(root, l, r):
            if not root:
                return
            if l < root.val < r:
                dfs(root.left, l, root.val)
                dfs(root.right, root.val, r)
            else:
                self.state = False
                return
        dfs(root, float("-inf"), float("inf"))
        return self.state
                 