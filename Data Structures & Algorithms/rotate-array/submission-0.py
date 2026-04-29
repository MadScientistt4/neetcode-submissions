class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        count = start = 0
        while count < n:
            cur = start
            prev = nums[start]
            while True:
                nxt = (cur+k)%n 
                nums[nxt], prev = prev, nums[nxt]
                cur = nxt
                count += 1
                if start == cur:
                    break
            start += 1           
            
        