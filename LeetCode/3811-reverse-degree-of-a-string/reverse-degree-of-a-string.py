class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i,c in enumerate(s):
            total+=(i+1)*(ord('z')-ord(c)+1)
        return total
        