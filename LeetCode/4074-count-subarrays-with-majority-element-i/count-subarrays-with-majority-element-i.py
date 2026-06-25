class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        prefix = 0
        count = 0    
        freq = {0: 1}
        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1
            for k in freq:
                if k < prefix:
                    count += freq[k]
            freq[prefix] = freq.get(prefix, 0) + 1
        return count
        