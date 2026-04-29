class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, 1
        prefix = []
        suffix, maxi = [], 0
        water = 0
        for i in range(len(height)):
            prefix.append(maxi)
            maxi = max(maxi, height[i])
        maxi = 0
        for i in range(len(height)-1, -1, -1):
            suffix.append(maxi)
            maxi = max(maxi, height[i])
        print(height)
        print(prefix)
        suffix.reverse()
        print(suffix)
        waters=[]
        for i in range(len(height)):
            val = min(prefix[i], suffix[i])-height[i] 
            water += val if val > 0 else 0
            waters.append(water)
        print(waters)
        return water
        

