class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        heap = [(-nums[i], i) for i in range(k-1)]
       
        heapq.heapify(heap)
        print(heap)
        output = []
        for i in range(len(nums)-k+1):
            heapq.heappush(heap, (-nums[i+k-1], i+k-1))
            element, index = heap[0]
            while index < i:
                element, index = heapq.heappop(heap)
            heapq.heappush(heap, (element, index))
            output.append(-element)
        return output
        
