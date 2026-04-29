# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left greater than the node's key.
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.val = 0
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            self.count += 1
            if self.count == k:
                self.val = root.val
            dfs(root.right)
        dfs(root)
        return self.val