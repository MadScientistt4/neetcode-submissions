class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        res = []
        cnt0 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt0 += 1
            else:
                mul *= nums[i]
        for i in range(len(nums)):
            if cnt0 == 1:
                if nums[i] == 0:
                    res.append(mul)
                else:
                    res.append(0)
            if cnt0 > 1:
                res.append(0)
            if cnt0 == 0:
                res.append(mul//nums[i])
            
        return res