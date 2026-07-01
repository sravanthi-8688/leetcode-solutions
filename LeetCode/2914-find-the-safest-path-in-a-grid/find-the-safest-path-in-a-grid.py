from collections import deque

class Solution:
    def isPossible(self, dist, target):
        n = len(dist)

        if dist[0][0] < target:
            return False

        vis = [[False] * n for _ in range(n)]
        q = deque([(0, 0)])
        vis[0][0] = True

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            r, c = q.popleft()

            if r == n - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and
                    0 <= nc < n and
                    not vis[nr][nc] and
                    dist[nr][nc] >= target):

                    vis[nr][nc] = True
                    q.append((nr, nc))

        return False

    def maximumSafenessFactor(self, grid):
        n = len(grid)

        if grid[0][0] or grid[n-1][n-1]:
            return 0

        dist = [[float('inf')] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and
                    0 <= nc < n and
                    dist[r][c] + 1 < dist[nr][nc]):

                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        low, high = 0, 2 * n
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if self.isPossible(dist, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans