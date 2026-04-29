class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique = {}
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] not in unique:
                unique[s[right]] = 1
            else:
                unique[s[right]] += 1
            while (right - left + 1) - max(unique.values()) > k:
                unique[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res
            