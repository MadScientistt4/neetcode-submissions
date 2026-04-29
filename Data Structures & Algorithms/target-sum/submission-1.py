class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(i, sums):
            if i == n:
                return 1 if sums == target else 0
            if (i, sums) in dp:
                return dp[(i, sums)]
            minus = dfs(i+1, sums - nums[i])
            plus = dfs(i+1, sums + nums[i])
            dp[(i,sums)] = minus + plus
            return dp[(i,sums)] 
        return dfs(0, 0)
        