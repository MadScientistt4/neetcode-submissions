class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate = {}
        i, j = 0, 0
        res, maxi = 1, 0
        while i <= j and j < len(s):
            if s[j] in duplicate and duplicate[s[j]] >= i:
                i = duplicate[s[j]] + 1
            duplicate[s[j]] = j 
            maxi = max(maxi, j-i+1)
            j += 1

        return maxi


            
            