class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for char in s:
            if char == "{" or char == "(" or char == "[":
                arr.append(char)
            elif char == "}" or char == ")" or char == "]":
                if len(arr) == 0:
                    return False
                if self.check(arr[-1], char):
                    arr.pop()
                else:
                    return False
        if len(arr) != 0:
            return False
        return True
    
    
    def check(self, arr_top: str, char: str):
        if char == "}" and arr_top == "{":
            return True
        if char == "]" and arr_top == "[":
            return True
        if char == ")" and arr_top == "(":  
            return True
        return False