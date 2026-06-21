class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """ 
        costs.sort()
        sum=0
        count=0
        if coins<min(costs):
            return 0
        else:
            for i in costs:
               if sum+i>coins:
                break
               sum+=i
               count+=1
        return count


        