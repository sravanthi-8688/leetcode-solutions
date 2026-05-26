class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        u=[]
        nu=[]
        for i in word:
            if i not in u:
                u.append(i)
            else:
                nu.append(i)
        count=0
        for i in range(len(u)):
            if u[i].islower():
                if u[i].upper() in u:
                    count+=1
        return count

        