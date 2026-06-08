class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"
        
        num &= 0xffffffff
        return format(num, 'x')