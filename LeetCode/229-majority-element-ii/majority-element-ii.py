class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        size=n/3
        freq={}
        res=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for k,v in freq.items():
            if v>size:
                res.append(k)
        return res



        