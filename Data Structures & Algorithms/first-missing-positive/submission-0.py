class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sets = set(nums)
        cur = 1
        for i in range(1, len(nums)+1):
            if i not in sets:
                return i
        return len(nums)+1