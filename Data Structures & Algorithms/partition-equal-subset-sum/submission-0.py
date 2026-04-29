class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        sums = sum(nums)//2
        dp = [[-1] * (sums+1) for _ in range(len(nums))]
        def dfs(i, target):
            if target == 0:
                return True
            if i == len(nums)-1:
                return nums[i] == target
            if dp[i][target] != -1:
                return dp[i][target]
            notTake:bool = dfs(i+1, target)
            take = False
            if target >= nums[i]:
                take = dfs(i+1, target-nums[i])
            dp[i][target] = notTake or take
            return dp[i][target]
        return dfs(0, sums)
        