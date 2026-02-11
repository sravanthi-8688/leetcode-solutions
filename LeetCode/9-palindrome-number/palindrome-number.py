class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1=str(x)
        x1=x1[::-1]
        if str(x)==x1:
            return True
        return False