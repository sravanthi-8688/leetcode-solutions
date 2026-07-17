class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_value=max(nums)
        frequency=[0]*(max_value+1)
        for num in nums:
            frequency[num]+=1
        exact_gcd=[0]*(max_value+1)
        for g in range(max_value,0,-1):
            divisible_count=0
            for multiple in range(g,max_value+1,g):
                divisible_count+=frequency[multiple]
            pairs=divisible_count*(divisible_count-1)/ 2
            for multiple in range(2*g,max_value+1,g):
                pairs-=exact_gcd[multiple]
            exact_gcd[g]=pairs
        prefix=[0]*(max_value+1)
        for g in range(1,max_value+1):
            prefix[g]=prefix[g-1]+exact_gcd[g]
        answer=[]
        for query in queries:
            left=1
            right=max_value
            while left<right:
                mid=(left + right) // 2
                if prefix[mid]>query:
                    right=mid
                else:
                    left=mid + 1
            answer.append(left)
        return answer