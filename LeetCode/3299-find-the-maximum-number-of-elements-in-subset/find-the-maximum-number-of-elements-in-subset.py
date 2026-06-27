class Solution(object):
    def maximumLength(self, nums):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        ans = 1

        for x in freq:
            if x == 1:
                if freq[x] % 2 == 1:
                    ans = max(ans, freq[x])
                else:
                    ans = max(ans, freq[x] - 1)
                continue

            cur = x
            length = 0

            while True:
                if freq.get(cur, 0) >= 2:
                    length += 2
                    cur = cur * cur
                elif freq.get(cur, 0) == 1:
                    length += 1
                    break
                else:
                    break

            if length % 2 == 0:
                length -= 1

            ans = max(ans, length)

        return ans