class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = {}
        need = {}
        for i in range(len(t)):
            need[t[i]] = 1 + need.get(t[i], 0)
            if t[i] not in have:
                have[t[i]] = 0
        print(need)
        print(have)
        left, right = 0, 0
        cnt, total = 0, len(need)
        mini = float("infinity")
        res = [-1, -1]
        while left <= right and right < len(s):
            have[s[right]] = 1 + have.get(s[right], 0)
            if s[right] in need and have[s[right]] == need[s[right]]:
                cnt += 1
                
            while cnt == total:
                if (right -left + 1) < mini:
                    res = [left, right]
                    mini = right - left + 1
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    cnt -= 1
                left += 1
            right += 1
        left, right = res
        return s[left: right + 1] if mini != float("infinity") else ""
         