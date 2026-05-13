class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        heap = []
       
        heapq.heapify(heap)
        print(heap)
        output = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k-1:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)

                output.append(-heap[0][0])
        return output
        
