class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)
        visited = set()
        def dfs(node):
            for nei in adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res
                