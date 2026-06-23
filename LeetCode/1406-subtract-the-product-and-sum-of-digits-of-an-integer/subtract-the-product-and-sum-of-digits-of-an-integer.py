class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        prod=1
        while(n>0):
            rem=n%10
            sum+=rem
            prod*=rem
            n=n//10
        return prod-sum
        