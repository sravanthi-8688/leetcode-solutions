class Solution(object):
    def minimumPushes(self, word):
        freq={}
        for ch in word:
            freq[ch]=freq.get(ch, 0)+1
        counts=sorted(freq.values(),reverse=True)
        pushes=0
        for i in range(len(counts)):
            pushes+=counts[i]*(i//8+1)
        return pushes