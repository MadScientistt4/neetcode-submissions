class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        right = max(piles)
        left = 1
        mini = right
        while left < right:
            mid = (left+right)//2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/mid)

            print(left, mid, right, hrs)
            if hrs <= h:
                right = mid
                mini = min(mid, mini)
            else:
                left = mid + 1
        return mini
            
