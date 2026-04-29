class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = s[::-1]
        res = ""
        temp = ""
        for i in range(len(s)):
            if s[i].isalnum():
                temp += s[i]
            if rev[i].isalnum():
                res += rev[i]    
        if res.lower() == temp.lower():
            return True
        return False