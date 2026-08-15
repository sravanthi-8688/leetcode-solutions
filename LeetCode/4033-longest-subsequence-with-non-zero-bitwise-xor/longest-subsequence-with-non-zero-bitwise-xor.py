class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n*[0]==nums:
            return 0
        x=0
        for i in nums:
            x^=i
        if x:
            return n
        else:
            return n-1