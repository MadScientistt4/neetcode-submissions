class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)-1
        while r < len(s2):
            if self.compare(s1, s2[l:r+1]):
                return True
            l += 1
            r += 1
        return False
    def compare(self, s1: str, s2: str):
        map1, map2 = {}, {}
        for char in s1:
            if char not in map1:
                map1[char] = 1
            else:
                map1[char] += 1
        for char in s2:
            if char not in map2:
                map2[char] = 1
            else:
                map2[char] += 1
        for key in map1:
            if key not in map2 or map1[key] != map2[key]:
                return False
        return True

