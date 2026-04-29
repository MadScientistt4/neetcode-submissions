# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def dfs(root, arr):
            if not root:
                return
            arr.append(root.val)
            if max(arr) == root.val:
                self.good += 1
            print(arr, root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)
            arr.pop()
        dfs(root, [])
        return self.good

