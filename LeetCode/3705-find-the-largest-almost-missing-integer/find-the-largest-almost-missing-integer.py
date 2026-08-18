class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        for i in range(len(nums)-k+1):
            for x in set(nums[i:i+k]):
                count[x]+=1
        return max((x for x in count if count[x]==1),default=-1)
        