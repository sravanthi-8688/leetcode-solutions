class Solution(object):
    def firstMissingPositive(self, nums):
        nums = sorted(nums)
        missing = 1
        
        for num in nums:
            if num == missing:
                missing += 1
        
        return missing