class Solution(object):
    def canAliceWin(self, nums):
        single=0
        double=0
        for i in nums:
            if i<10:
                single+=i
            else:
                double+=i
        return single!=double