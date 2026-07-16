class Solution(object):
    def gcdSum(self, nums):
        def prefixGcd(maxi,mini):
            while mini!=0:
                maxi,mini=mini,maxi%mini
            return maxi
        r=[]
        m=0
        for i in nums:
            m=max(m,i)
            r.append(prefixGcd(i,m))
        r.sort()
        s=0
        for i in range(len(r)//2):
            s+=prefixGcd(r[i],r[len(r)-1-i])
        return s
