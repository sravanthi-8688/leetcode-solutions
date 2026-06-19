class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1=[]
        num2=[]
        for i in range(1,n+1):
            if i %m!=0:
                num1.append(i)
            if i%m==0:
                num2.append(i)
        return sum(num1)-sum(num2)
        