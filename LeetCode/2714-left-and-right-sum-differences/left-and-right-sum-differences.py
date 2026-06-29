class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)

        pre=[0]*n
        suf=[0]*n
        ans=[0]*n

        for i in range(1,n):
            pre[i]=pre[i-1]+nums[i-1]
        for i in range(n-2,-1,-1):
            suf[i]=suf[i+1]+nums[i+1]
        for i in range(n):
            ans[i]=abs(pre[i]-suf[i])

        return ans
        
        