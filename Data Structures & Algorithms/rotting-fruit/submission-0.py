class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(queue):
            time = 0
            q = collections.deque(queue)
            print(q)
            no_of_oragnes_currect_lvl = len(q)
            no_of_oragnes_next_lvl = 0
            while q:
                if no_of_oragnes_currect_lvl == 0:
                    print(q)
                    time += 1
                    no_of_oragnes_currect_lvl = no_of_oragnes_next_lvl
                    no_of_oragnes_next_lvl = 0
                no_of_oragnes_currect_lvl -= 1
                i, j = q.popleft()
                traverse = 0
                if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                    traverse += 1
                    grid[i][j+1] = 2
                    q.append((i, j+1))
                if i + 1 < len(grid) and grid[i+1][j] == 1:
                    traverse += 1
                    grid[i+1][j] = 2
                    q.append((i+1, j))
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    traverse += 1
                    grid[i][j-1] = 2
                    q.append((i, j-1))
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    traverse += 1
                    grid[i-1][j] = 2
                    q.append((i-1, j))
                no_of_oragnes_next_lvl += traverse
            return time
        maxi = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        time = bfs(queue)
        has_one = any(1 in row for row in grid)
        if has_one:
            return -1
        return time