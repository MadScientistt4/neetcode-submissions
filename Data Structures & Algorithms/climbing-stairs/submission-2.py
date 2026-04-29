class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0
        def sol(step):
            if step == n:
                self.res += 1
                return
            elif step > n:
                return
            sol(step+1)
            sol(step+2)
        sol(0)
        return self.res