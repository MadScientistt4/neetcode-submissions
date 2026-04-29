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
        for char1, char2 in zip(s1, s2):
            map1[char1] = 1 + map1.get(char1, 0)
            map2[char2] = 1 + map2.get(char2, 0)
        for key in map1:
            if key not in map2 or map1[key] != map2[key]:
                return False
        return True

