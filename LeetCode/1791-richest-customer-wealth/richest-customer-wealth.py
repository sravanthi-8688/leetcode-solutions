class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth=0
        for i in accounts:
            curr_sum=0
            for j in i:
                curr_sum+=j
                max_wealth=max(curr_sum,max_wealth)
        return max_wealth
