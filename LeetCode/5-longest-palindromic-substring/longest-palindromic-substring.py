class Solution(object):
    def longestPalindrome(self, s):
        n=len(s)
        ans=""
        for i in range(n):
            for j in range(i, n):
                sub=s[i:j+1]
                if sub==sub[::-1] and len(sub)>len(ans):
                    ans=sub
        return ans