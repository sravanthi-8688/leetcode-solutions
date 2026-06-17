class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        if len(res)==0:
            res.append(-1)
            res.append(-1)
        if len(res)==1:
            res.append(res[0])
        if len(res)>2:
            res=res[0],res[len(res)-1]
        return res
        