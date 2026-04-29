class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps, cur_end = 0, 0
        farthest = 0
        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest
                if farthest >= len(nums) - 1:
                    break
        return jumps
            