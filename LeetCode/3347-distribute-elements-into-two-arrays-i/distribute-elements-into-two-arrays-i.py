class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        A=[[nums[0]],[nums[1]]]
        for i in nums[2:]:
           A[A[0][-1]<=A[1][-1]].append(i)
        return A[0]+A[1]
        