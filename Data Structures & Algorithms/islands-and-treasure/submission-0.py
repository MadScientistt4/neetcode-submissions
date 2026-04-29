import collections
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        infinity = 2147483647
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        dis = 1
        while q:
            q_len = len(q)
            for _ in range(q_len):
                i, j = q.popleft()
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == infinity:
                        grid[nx][ny] = dis
                        q.append((nx, ny))
            dis += 1
        
                

                    