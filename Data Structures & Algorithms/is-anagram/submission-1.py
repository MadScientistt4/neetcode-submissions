class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                ind = t.index(i)
                t = t[:ind] + t[ind+1:]
            else:
                return False
        if len(t) == 0:
            return True
        else:
            return False