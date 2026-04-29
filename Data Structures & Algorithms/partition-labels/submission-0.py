class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        end = 0
        start = 0
        arr = []
        for i in range(len(s)):
            hashmap[s[i]] = i
        for i in range(len(s)):
            end = max(end, hashmap[s[i]])
            if i == end:
                arr.append(end-start+1)
                start = end + 1
        return arr