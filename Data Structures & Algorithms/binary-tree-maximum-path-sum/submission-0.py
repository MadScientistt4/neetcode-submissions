# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = -float('inf')
        def dfs(node):
            if not node:
                return -1*float('inf')
            leftmaxsum = dfs(node.left)
            rightmaxsum = dfs(node.right)
            if leftmaxsum < 0:
                leftmaxsum = 0
            if rightmaxsum < 0:
                rightmaxsum = 0
            self.maxi = max(self.maxi, node.val + leftmaxsum + rightmaxsum)
            return node.val + max(leftmaxsum, rightmaxsum)
        dfs(root)
        return self.maxi