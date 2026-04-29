class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        indeg = [0]*numCourses
        for dest, src in prerequisites:
            adj[src].append(dest)
            indeg[dest] += 1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        order = []
        while q:
            cur = q.popleft()
            order.append(cur)
            for nei in adj[cur]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return order if len(order) == numCourses else []
                
                