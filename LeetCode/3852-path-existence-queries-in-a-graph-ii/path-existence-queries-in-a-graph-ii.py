class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        order = list(range(n))
        order.sort(key=lambda i: nums[i])
        sortedNums = [nums[i] for i in order]
        pos = [0]*n
        for i, orig in enumerate(order):
            pos[orig] = i

        compId = [0]*n
        for i in range(1, n):
            if sortedNums[i] - sortedNums[i-1] <= maxDiff:
                compId[i] = compId[i-1]
            else:
                compId[i] = compId[i-1] + 1

        nextMax = [0]*n
        r = 0
        for i in range(n):
            if r < i: r = i
            while r+1 < n and sortedNums[r+1] - sortedNums[i] <= maxDiff:
                r += 1
            nextMax[i] = r

        LOG = n.bit_length()
        up = [nextMax[:]]
        for k in range(1, LOG):
            prev = up[k-1]
            curr = [prev[prev[i]] for i in range(n)]
            up.append(curr)

        context = nums[:]

        ans = []
        for u, v in queries:
            su, sv = pos[u], pos[v]
            if compId[su] != compId[sv]:
                ans.append(-1)
                continue
            if su == sv:
                ans.append(0)
                continue
            if su > sv:
                su, sv = sv, su

            cur, dist = su, 0
            for k in range(LOG-1, -1, -1):
                nxt = up[k][cur]
                if nxt < sv:
                    cur = nxt
                    dist += 1<<k

            dist += 1
            ans.append(dist)

        return ans