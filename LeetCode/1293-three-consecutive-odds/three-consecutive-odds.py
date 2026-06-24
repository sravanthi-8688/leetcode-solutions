class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        odd_count=0
        for i in range(len(arr)):
            if arr[i]%2==1:
                odd_count+=1
                if odd_count==3:
                    return True
            else:
                odd_count=0
        return False
        