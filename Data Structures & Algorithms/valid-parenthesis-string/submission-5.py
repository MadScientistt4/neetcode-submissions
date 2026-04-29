class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) != 0:
                    stack.pop()
                    continue
                if len(star) != 0:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        i = len(stack) - 1
        while len(stack) != 0 and len(star) != 0:
            if stack[-1] < star[-1]:
                stack.pop()
                star.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False
        