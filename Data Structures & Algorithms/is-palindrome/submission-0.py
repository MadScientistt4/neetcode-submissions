class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = s[::-1]
        res = ""
        temp = ""
        for char in s:
            if char.isalnum():
                temp += char
        for char in rev:
            if char.isalnum():
                res += char
            
        if res.lower() == temp.lower():
            return True
        return False