class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        prev, prev2 = 2, 1
        for i in range(3, n+1):
            cur = prev + prev2
            prev2 = prev
            prev = cur
        return cur