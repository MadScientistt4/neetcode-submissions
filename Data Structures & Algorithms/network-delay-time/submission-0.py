from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        costs = [float('inf')] * (n+1)
        costs[k] = 0

        heap = [(0, k)]
        heapq.heapify(heap)
        while heap:
            time, node = heapq.heappop(heap)
            if time > costs[node]:
                continue
            for nei, cost in adj[node]:
                if time + cost < costs[nei]:
                    costs[nei] = time + cost
                    heapq.heappush(heap, (time+cost, nei))
        
        return max(costs[1:]) if max(costs[1:]) != float('inf') else -1


        