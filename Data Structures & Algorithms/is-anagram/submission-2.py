class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        freq1 = {}
        freq2 = {}
        for i in range(len(str1)):
            if str1[i] in freq1:
                freq1[str1[i]] += 1
            else:
                freq1[str1[i]] = 1
        for i in range(len(str2)):
            if str2[i] in freq2:
                freq2[str2[i]] += 1
            else:
                freq2[str2[i]] = 1
        return freq1 == freq2