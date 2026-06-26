class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: transform to +1 / -1
        arr = [1 if x == target else -1 for x in nums]
        
        # Step 2: prefix sum
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + arr[i]
        
        # Step 3: coordinate compression
        vals = sorted(set(pref))
        comp = {v:i+1 for i,v in enumerate(vals)}
        
        # Fenwick Tree
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
        
        # Step 4: count valid pairs
        ans = 0
        for p in pref:
            idx = comp[p]
            ans += query(idx - 1)   # count smaller prefix
            update(idx)
        
        return ans
        