class Solution(object):
    def gcdOfOddEvenSums(self, n):
        odd=[]
        even=[]
        for i in range(1,2*n+1):
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        sumOdd=sum(odd)
        sumEven=sum(even)
        while sumEven:
            sumOdd,sumEven=sumEven,sumOdd%sumEven
        return sumOdd