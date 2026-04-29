class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        closeToOpen = { ")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in closeToOpen:
                if arr and arr[-1] == closeToOpen[char]:
                    arr.pop()
                else:
                    return False
            else:
                arr.append(char)
        if len(arr) != 0:
            return False
        return True