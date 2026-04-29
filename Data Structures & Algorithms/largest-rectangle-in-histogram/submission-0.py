class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxi = 0
        for i in range(n):
            area = heights[i]
            left, right = i-1, i+1
            while 0 <= left:
                if heights[left] >= heights[i]:
                    area += heights[i]
                    left -= 1
                else:
                    break
            while right < n :
                if heights[right] >= heights[i]:
                    area += heights[i]
                    right += 1
                else:
                    break
            maxi = max(maxi, area)
        return maxi
            