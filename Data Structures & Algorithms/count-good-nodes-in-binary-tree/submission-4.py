# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxval):
            if not root:
                return 0
            good = 0
            if maxval <= root.val:
                good += 1
                maxval = root.val
            return good + dfs(root.left, maxval) + dfs(root.right, maxval)
        return dfs(root, root.val)

