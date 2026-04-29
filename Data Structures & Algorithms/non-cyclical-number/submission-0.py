class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsqdigits(digit):
            sums = 0
            while digit != 0:
                rem = digit % 10
                sums += rem*rem
                digit = digit // 10
            return sums
        sets = set()
        sets.add(n)
        while n != 1:
            n = sumofsqdigits(n)
            if n in sets:
                return False
            sets.add(n)
        return True
