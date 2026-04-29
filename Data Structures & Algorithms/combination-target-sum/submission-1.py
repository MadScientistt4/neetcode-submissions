class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sums = []
        def dfs(i):
            if i >= len(nums):
                print(sums)
                if sum(sums) == target and sums not in res:
                    res.append(sums.copy())
                return
                        
            if sum(sums) == target and sums not in res:
                res.append(sums.copy()) 
                return
            elif sum(sums) > target:
                return
            sums.append(nums[i])
            dfs(i)
            sums.pop()
            dfs(i+1)
        dfs(0)
        return res
