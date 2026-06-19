class Solution(object):
    def triangleType(self, nums):
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        if len(set(nums)) == 1:
            return "equilateral"
        elif len(set(nums)) == 2:
            return "isosceles"
        else:
            return "scalene"