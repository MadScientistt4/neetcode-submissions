class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maps = {}
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] in maps:
                continue
            else:
                maps[nums[i]] = i
        seq_start = []
        for key in maps:
            if key + 1 in maps and key-1 not in maps:
                seq_start.append(key)
        maxi = 1
        for start in seq_start:
            cnt = 1
            while start + 1 in maps:
                cnt += 1
                start += 1
            maxi = max(maxi, cnt)
        return maxi