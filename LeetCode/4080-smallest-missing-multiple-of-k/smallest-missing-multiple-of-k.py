class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=set(nums)
        m=1
        while k*m in s:
            m+=1
        return m*k
        # for i in range(1,101):
        #     if i*k not  in nums:
        #         return i*k