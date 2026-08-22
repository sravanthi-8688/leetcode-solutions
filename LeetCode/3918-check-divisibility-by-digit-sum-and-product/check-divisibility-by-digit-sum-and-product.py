class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s,p,x=0,1,n
        while x>0:
            x,r=divmod(x,10)
            s+=r
            p*=r
        return n%(s+p)==0
        
        