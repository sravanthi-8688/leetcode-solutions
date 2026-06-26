class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        arr = [1 if x == target else -1 for x in nums]
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + arr[i]
        vals = sorted(set(pref))
        comp = {v:i+1 for i,v in enumerate(vals)}
        size = len(vals)
        bit = [0] * (size + 1)
        def update(i):
            while i <= size:
                bit[i] += 1
                i += i & -i
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        ans = 0
        for p in pref:
            idx = comp[p]
            ans += query(idx - 1)   
            update(idx)
        
        return ans
        