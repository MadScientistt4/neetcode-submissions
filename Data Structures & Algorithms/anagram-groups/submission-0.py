class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        while strs:
            arr = [strs[0]]
            to_remove = [strs[0]]
            for j in range(1, len(strs)):
                if self.checkIfAnagrams(strs[0], strs[j]):
                    arr.append(strs[j])
                    to_remove.append(strs[j])
            
            for item in to_remove:  # Safely remove tracked strings
                strs.remove(item)
            print(arr)
            print(strs)
            res.append(arr)
        return res
    def checkIfAnagrams(self, str1, str2):
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
        