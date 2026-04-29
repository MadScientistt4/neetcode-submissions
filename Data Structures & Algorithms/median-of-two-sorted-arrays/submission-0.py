class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        if len(num1) > len(nums2):
            num1, num2 = num2, num1
        l, r = 0, len(num1)-1
        total = len(num1) + len(num2)
        half = total // 2
        while True:
            mid1 = (l+r)//2
            mid2 = half - mid1 - 2 

            left1 = num1[mid1] if mid1 >= 0 else -float("inf")
            right1 = num1[mid1+1] if mid1+1 < len(num1) else float("inf")
            left2 = num2[mid2] if mid2 >= 0 else -float("inf")
            right2 = num2[mid2+1] if mid2+1 < len(num2) else float("inf")

            if left1 <= right2 and left2 <= right2:
                if total % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2))/2
            elif left1 > right2:
                r = mid1 - 1
            else:
                l = mid1 + 1