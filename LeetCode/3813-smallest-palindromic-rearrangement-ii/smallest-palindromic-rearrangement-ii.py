from collections import Counter

class Solution(object):
    def smallestPalindrome(self,s,k):
        n=len(s)
        m=n//2
        
        cnt=Counter(s)
        a=[cnt[chr(97+i)]//2 for i in range(26)]
        
        def comb_count(total,arr):
            res=1
            for x in arr:
                for j in range(1,x+1):
                    res=res*(total-x+j)//j
                    if res>=k:
                        return k
                total-=x
            return res
        
        if comb_count(m,a)<k:
            return ""
        
        ans=""
        
        for pos in range(m):
            for i in range(26):
                if a[i]==0:
                    continue
                
                a[i]-=1
                if comb_count(m-pos-1,a)>=k:
                    ans+=chr(97+i)
                    break
                k-=comb_count(m-pos-1,a)
                a[i]+=1
        
        return ans+(s[m] if n%2 else "")+ans[::-1]