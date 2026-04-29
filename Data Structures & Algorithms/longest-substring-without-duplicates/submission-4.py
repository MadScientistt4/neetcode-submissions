class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        duplicate = {s[0]: 0}
        i, j = 0, 1
        res, maxi = 1, 1
        while i <= j and j < len(s):
            if s[j] in duplicate and duplicate[s[j]] >= i:
                i = duplicate[s[j]] + 1
            duplicate[s[j]] = j 
            maxi = max(maxi, j-i+1)
            print(i, j, s[j], maxi)
            j += 1

        return maxi


            
            