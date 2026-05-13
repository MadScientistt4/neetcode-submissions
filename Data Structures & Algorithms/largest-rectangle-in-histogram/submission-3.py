class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = [] # [(element, index)]
        for i in range(n):
            index = i
            if not stack or heights[i] > stack[-1][0]:
                stack.append((heights[i], i))
                continue
            while stack and heights[i] < stack[-1][0]:
                height, index = stack.pop()
                max_area = max(max_area, height*(i-index))
            stack.append((heights[i], index))
        
        while stack:
            height, index = stack.pop()
            max_area = max(max_area, (i-index+1)*height)
        return max_area