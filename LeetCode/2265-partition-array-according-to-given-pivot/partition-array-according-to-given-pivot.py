class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        l=[]
        r=[]
        count=0
        for i in nums:
            if i<pivot:
                l.append(i)
            if i>pivot:
                r.append(i)
            if i==pivot:
                count+=1
        return l+[pivot]*count+r