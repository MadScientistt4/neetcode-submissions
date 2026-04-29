class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seq = []
        arr = []
        def dfs(used):
            if len(seq) == len(nums):
                res.append(seq.copy())
                return
            for j in range(len(nums)):
                if used[j]:
                    continue
                used[j] = True
                seq.append(nums[j])
                dfs(used)
                seq.pop()
                used[j] = False
        dfs([False] * len(nums))
        return res