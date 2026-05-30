from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))
        print(adj_list)

        costs = [[10**9] * (k+2) for _ in range(n)]
        costs[src][0] = 0

        heap = [(0, 0, src)]
        heapq.heapify(heap)
        min_cost = 10**9
        while heap:
            cur_cost, stops, node = heapq.heappop(heap)
            
            if node == dst:
                min_cost = min(min_cost, cur_cost)
            if stops == k+1:
                continue

            for nei, cost in adj_list[node]:
                if cur_cost + cost < costs[nei][stops+1]:
                    costs[nei][stops+1] = cur_cost + cost
                    heapq.heappush(heap, (cost + cur_cost, stops+1, nei))
        return -1 if min_cost == 10**9 else min_cost
