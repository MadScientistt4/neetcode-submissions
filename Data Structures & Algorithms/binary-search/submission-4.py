class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (r-l)//2
        for i in range(len(nums)):
            print(mid, nums[mid], l, r)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            mid = (r+l)//2
            if l == r and nums[mid] != target:
                return -1
        return -1
