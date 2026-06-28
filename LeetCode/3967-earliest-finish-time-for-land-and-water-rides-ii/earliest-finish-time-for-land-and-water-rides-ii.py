class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        land = sorted(zip(landStartTime, landDuration))
        water = sorted(zip(waterStartTime, waterDuration))
        
        n, m = len(land), len(water)
        
        preW = [0]*m
        sufW = [0]*m
        
        preW[0] = water[0][1]
        for i in range(1, m):
            preW[i] = min(preW[i-1], water[i][1])
        
        sufW[m-1] = water[m-1][0] + water[m-1][1]
        for i in range(m-2, -1, -1):
            sufW[i] = min(sufW[i+1], water[i][0] + water[i][1])
        
        def upper_bound(arr, target):
            l, r = 0, len(arr)
            while l < r:
                mid = (l + r) // 2
                if arr[mid][0] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        ans = float('inf')
        
        for s, d in land:
            finish = s + d
            idx = upper_bound(water, finish)
            
            if idx > 0:
                ans = min(ans, finish + preW[idx-1])
            if idx < m:
                ans = min(ans, sufW[idx])
        
        preL = [0]*n
        sufL = [0]*n
        
        preL[0] = land[0][1]
        for i in range(1, n):
            preL[i] = min(preL[i-1], land[i][1])
        
        sufL[n-1] = land[n-1][0] + land[n-1][1]
        for i in range(n-2, -1, -1):
            sufL[i] = min(sufL[i+1], land[i][0] + land[i][1])
        
        for s, d in water:
            finish = s + d
            idx = upper_bound(land, finish)
            
            if idx > 0:
                ans = min(ans, finish + preL[idx-1])
            if idx < n:
                ans = min(ans, sufL[idx])
        
        return ans