class Solution(object):
    def calPoints(self, operations):
        res = []
        for i in operations:
            if i.lstrip('-').isdigit():
                res.append(int(i))
            elif i == 'C':
                res.pop()
            elif i == 'D':
                res.append(2 * res[-1])
            elif i == '+':
                res.append(res[-1] + res[-2])
        
        return sum(res)