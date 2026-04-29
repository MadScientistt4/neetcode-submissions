class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.mini = 999
        def dfs(i, total_cost):
            if i < n:
                total_cost += cost[i]
            else:
                self.mini = min(self.mini, total_cost)
                return
            dfs(i+1, total_cost)
            dfs(i+2, total_cost)
        dfs(0, 0)
        dfs(1, 0)
        return self.mini