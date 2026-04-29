class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq and i - freq[nums[i]] <= k:
                return True
            freq[nums[i]] = i
        return False