class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxi = 0
        stack = []
        for i in range(n):
            
            if not stack or heights[i] > stack[-1][1]:
                stack.append([i, heights[i]])
            elif heights[i] < stack[-1][1]:
                while stack and heights[i] < stack[-1][1]:
                    index, height = stack.pop() 
                    maxi = max(maxi, (i-index)*height)
                stack.append([index, heights[i]])
        
        while stack:
            index, height = stack.pop()
            maxi = max(maxi, (i-index+1)*height)

        return maxi
            