class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        nums.sort()
        small=nums[0]
        large=nums[-1]
        for i in range(1,large+1):
            if small%i==0 and large%i==0:
                res.append(i)
        return res[-1]


