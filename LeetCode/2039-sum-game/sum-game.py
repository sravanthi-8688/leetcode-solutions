class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        s1=num[:len(num)//2]
        s2=num[len(num)//2:]
        i=0
        q1,S1=0,0
        q2,S2=0,0
        while(i<len(s1)):
            if s1[i]=="?":
                q1+=1
            else:
                S1+=int(s1[i])
            if s2[i]=="?":
                q2+=1
            else:
                S2+=int(s2[i])
            i+=1
        if (q1+q2)%2!=0 or (S1-S2+4.5*(q1-q2))!=0:
            return True
        return False
        