class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')
        
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                
                finish1 = max(waterStartTime[j], landStartTime[i] + landDuration[i]) + waterDuration[j]
                finish2 = max(landStartTime[i], waterStartTime[j] + waterDuration[j]) + landDuration[i]
                
                ans = min(ans, finish1, finish2)
        
        return ans