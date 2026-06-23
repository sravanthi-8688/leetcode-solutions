class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # letters="qwertyuiopasdfghjlzxcvbnm"
        # for i in letters:
        #     if s.count(i)!=t.count(i):
        #         return False
        # return True
        return sorted(s)==sorted(t)

        