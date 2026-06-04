class Solution(object):
    def productExceptSelf(self, nums):
        zero_count = nums.count(0)
        
        if zero_count > 1:
            return [0] * len(nums)
        
        total = 1
        for num in nums:
            if num != 0:
                total *= num
        
        res = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // num)
        
        return res