class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi, cum = nums[0], 0
        for i in range(len(nums)):
            if cum < 0:
                cum = 0
            cum += nums[i]
            maxi = max(maxi, cum)
        return maxi

        return maxi
        