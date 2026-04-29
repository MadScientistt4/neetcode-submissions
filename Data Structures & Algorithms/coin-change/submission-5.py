class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        n = len(coins)
        dp = [[-1]*(target+1) for _ in range(n)]
        print(dp)
        def dfs(i, amount):
            if i == n - 1:
                if amount % coins[n-1] == 0:
                    return amount // coins[n-1]
                else:
                    return float('inf')
            if dp[i][amount] != -1:
                return dp[i][amount]
            not_take = dfs(i+1, amount)
            take = float('inf')
            if coins[i] <= amount:
                take = 1 + dfs(i, amount-coins[i])
            dp[i][amount] = min(not_take, take)
            return dp[i][amount]
        ans = dfs(0, target)
        if ans == float('inf'):
            return -1
        else:
            return ans