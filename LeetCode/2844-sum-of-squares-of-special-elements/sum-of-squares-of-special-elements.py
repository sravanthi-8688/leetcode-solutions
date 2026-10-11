class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        squ=0
        for i in range(1,n+1):
            if n%i==0:
                squ+=nums[i-1]**2
        return squ