class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod=1
        for i in nums:
            prod=prod*i
        if prod>0:
            return 1
        if prod==0:
            return 0
        if prod<0:
            return -1
        