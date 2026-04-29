class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                value_l = s[:left] + s[left+1:]
                value_r = s[:right] + s[right+1:]
                if value_l == value_l[::-1] or value_r == value_r[::-1]:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        