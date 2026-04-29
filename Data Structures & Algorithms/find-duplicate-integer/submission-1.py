class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sums = sum(nums)
        for i, value in enumerate(nums):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1
              