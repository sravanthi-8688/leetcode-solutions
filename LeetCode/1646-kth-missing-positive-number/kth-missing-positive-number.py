class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l,r=0,len(arr)
        while l<r:
            m=(l+r)/2
            if arr[m]-1-m<k:
                l=m+1
            else:
                r=m
        return l+k
        