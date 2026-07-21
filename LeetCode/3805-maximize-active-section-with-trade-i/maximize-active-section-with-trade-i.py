class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        ans=0
        pre=float("-inf")
        mx=0
        i=0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == "1":
                ans += length
            else:
                mx = max(mx, length + pre)
                pre = length

            i = j

        return ans + mx
        