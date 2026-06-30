class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last1=last2=last3=-1
        total=0
        for i,ch in enumerate(s):
            if ch=='a':
                last1=i
            elif ch=='b':
                last2=i
            else:
                last3=i
            if last1!=-1 and last2!=-1 and last3!=-1:
                total+=min(last1,last2,last3)+1
        return total
        