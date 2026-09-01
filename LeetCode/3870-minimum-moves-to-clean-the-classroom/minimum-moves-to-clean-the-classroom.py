from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        cells = m * n
        litter_bit = [0] * cells
        is_reset = [False] * cells
        start = 0
        litter_count = 0

        for r in range(m):
            for c in range(n):
                pos = r * n + c
                cell = classroom[r][c]
                if cell == "S":
                    start = pos
                elif cell == "L":
                    litter_bit[pos] = 1 << litter_count
                    litter_count += 1
                elif cell == "R":
                    is_reset[pos] = True

        if litter_count == 0:
            return 0

        mask_count = 1 << litter_count
        goal = mask_count - 1
        neighbors = [[] for _ in range(cells)]

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == "X":
                    continue
                pos = r * n + c
                if r > 0 and classroom[r - 1][c] != "X":
                    neighbors[pos].append(pos - n)
                if r + 1 < m and classroom[r + 1][c] != "X":
                    neighbors[pos].append(pos + n)
                if c > 0 and classroom[r][c - 1] != "X":
                    neighbors[pos].append(pos - 1)
                if c + 1 < n and classroom[r][c + 1] != "X":
                    neighbors[pos].append(pos + 1)

        best = bytearray(cells * mask_count)
        start_key = start * mask_count
        best[start_key] = energy + 1

        base = energy + 1
        queue = deque([start_key * base + energy])
        moves = 0

        while queue:
            for _ in range(len(queue)):
                packed = queue.popleft()
                remaining = packed % base
                key = packed // base
                pos, mask = divmod(key, mask_count)

                if remaining == 0:
                    continue

                for nxt in neighbors[pos]:
                    next_energy = energy if is_reset[nxt] else remaining - 1
                    next_mask = mask | litter_bit[nxt]

                    if next_mask == goal:
                        return moves + 1

                    next_key = nxt * mask_count + next_mask
                    stored_energy = next_energy + 1
                    if stored_energy > best[next_key]:
                        best[next_key] = stored_energy
                        queue.append(next_key * base + next_energy)

            moves += 1

        return -1