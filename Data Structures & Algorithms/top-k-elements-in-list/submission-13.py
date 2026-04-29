
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        print(freq)
        heap = []
        for num in freq:
            heapq.heappush(heap, (-freq[num], num))
        print(heap)
        res = []
        for i in range(k):
            num = heapq.heappop(heap)
            res.append(num[1])
        return res

            