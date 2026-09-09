class Solution:
    def countCommas(self, n: int) -> int:
        if n<=999:
            return 0
        t=0
        s=1000
        while s<=n:
            t+=n-s+1
            s*=1000
        return t