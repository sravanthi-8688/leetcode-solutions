class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        size=n/3
        res=[]
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for k,v in freq.items():
            if v>n/3:
                res.append(k)
        return res
        