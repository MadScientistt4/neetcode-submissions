class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, 1
        prefix = []
        suffix, maxi = [0]*len(height), 0
        water = 0
        for i in range(len(height)):
            prefix.append(maxi)
            maxi = max(maxi, height[i])
        maxi = 0
        for i in range(len(height)-1, -1, -1):
            suffix[i] = maxi
            maxi = max(maxi, height[i])
        for i in range(len(height)):
            val = min(prefix[i], suffix[i])-height[i] 
            water += val if val > 0 else 0
        return water
        

