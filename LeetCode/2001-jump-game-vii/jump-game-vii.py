class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n=len(s)
        if s[-1]!='0':
            return False
        dp=[False]*n
        dp[0]=True
        active_jumps=0
        for i in range(1,n):
            if i>=minJump and dp[i-minJump]:
                active_jumps+=1
            if i>maxJump and dp[i-maxJump-1]:
                active_jumps-=1
            if s[i]=='0' and active_jumps>0:
                dp[i]=True
        return dp[-1]      