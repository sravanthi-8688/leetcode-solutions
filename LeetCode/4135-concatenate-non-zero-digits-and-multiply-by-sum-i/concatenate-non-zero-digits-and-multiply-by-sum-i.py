class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        v=[]
        while n>0:
            d=n%10
            if d!=0:
                v.append(d)
                s+=d
            n//=10
        if not v:
            return 0
        x=v[0]
        place=10
        for i in range(1,len(v)):
            x+=v[i] *place
            place*= 10
        return x*s

        