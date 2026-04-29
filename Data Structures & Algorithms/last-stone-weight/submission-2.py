class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       
        max_heap = [-num for num in stones]
        heapq.heapify(max_heap)
        while max_heap:
            stone1 = heapq.heappop(max_heap)
            print(stone1*-1)
            if max_heap:
                stone2 = heapq.heappop(max_heap)
                print(stone2*-1)
            else:
                return stone1*-1
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(max_heap, abs(stone1-stone2)*-1)
        return 0