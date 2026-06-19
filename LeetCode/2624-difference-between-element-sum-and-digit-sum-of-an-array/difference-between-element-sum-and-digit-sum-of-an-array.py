class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum=sum(nums)
        digit_sum=0
        for i in nums:
            while i>0:
                digit_sum+=i%10
                i=i//10
        return element_sum-digit_sum
        