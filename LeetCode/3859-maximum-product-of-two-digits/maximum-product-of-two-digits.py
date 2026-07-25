class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1=str(n)
        l=n1.strip()
        l2=[]
        for i in l:
            l2.append(int(i))
        l2.sort()
        return l2[-1]*l2[-2]
        
        