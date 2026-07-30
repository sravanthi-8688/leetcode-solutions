class Solution(object):
    def minimumPushes(self, word):
        pushes=0
        n=len(word)
        if n<=8:
            pushes=n
        elif n<=16:
            pushes=8+(n-8)*2
        elif n<=24:
            pushes=8+8*2+(n-16)*3
        else:
            pushes=8+8*2+8*3+(n-24)*4
        return pushes