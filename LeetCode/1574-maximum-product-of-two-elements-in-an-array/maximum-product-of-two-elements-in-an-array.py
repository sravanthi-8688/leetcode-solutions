class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ms=0
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i]-1)*(nums[j]-1)>ms:
                    ms=(nums[i]-1)*(nums[j]-1)
        return ms

        