class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        m, n = len(heights), len(heights[0])
        
        def dfs(i, j, visit, prev):
            if (i < 0 or i >= m) or (j < 0 or j >= n) or (i, j) in visit or heights[i][j] < prev:
                return
            visit.add((i, j))
            direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dx, dy in direc:
                nx, ny = i + dx, j + dy
                dfs(nx, ny, visit, heights[i][j])
        res = []
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n-1, atlantic, heights[i][n-1])

        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m-1, j, atlantic, heights[m-1][j])

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])                
        return res
