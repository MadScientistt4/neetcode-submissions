class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        maxheap = [(-freq[num], num) for num in freq]
        heapq.heapify(maxheap)
        print(maxheap)
        output = []
        for i in range(k):
            cnt, num = heapq.heappop(maxheap)
            output.append(num)
        return output