class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        value = 0
        for i in range(len(nums)):
            value = value ^ nums[i]
        return value 