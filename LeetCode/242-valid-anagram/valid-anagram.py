class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters="abcdefghijklmnopqrstuvwxyz"
        for i in letters:
            if s.count(i)!=t.count(i):
                return False
        return True

        