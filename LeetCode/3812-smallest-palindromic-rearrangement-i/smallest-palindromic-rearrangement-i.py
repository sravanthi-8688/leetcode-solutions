class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        half=s[:len(s)//2]
        half=sorted(half)
        if len(s)%2==0:
            out=half+half[::-1]
        else:
            out=half+[s[len(s)//2]]+half[::-1]
        return "".join(out)    