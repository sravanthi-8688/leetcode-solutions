class Solution(object):
    def romanToInt(self, s):
        D = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        prev = 0
        for ch in s[::-1]:
            val = D[ch]
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        return total
