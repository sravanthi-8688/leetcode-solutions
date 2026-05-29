class Solution(object):
    def minElement(self, nums):
        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        return min(digit_sum(i) for i in nums)