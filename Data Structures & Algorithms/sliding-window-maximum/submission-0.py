class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        heap = []
        output = []
        for i in range(len(nums)-k+1):
            l1 = nums[i:i+k]
            output.append(max(l1))
        return output
        
