class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
        s1= [""]*len(s)
        for i in range(len(indices)):
            s1[indices[i]]=s[i]
        return "".join(s1)
        