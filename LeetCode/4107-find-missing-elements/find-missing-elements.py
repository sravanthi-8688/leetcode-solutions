class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mini=min(nums)
        maxi=max(nums)
        res=[]
        for i in range(mini,maxi+1):
            if i not in nums:
                res.append(i)
        return res

        