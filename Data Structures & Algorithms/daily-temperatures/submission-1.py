class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temp)
        for i in range(len(temp)):
            while stack and temp[i] > stack[-1][0]:
                ele = stack.pop()
                res[ele[1]] = i - ele[1]
            stack.append([temp[i], i])
            
        return res
