class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        # Find S and number every L
        start_r = 0
        start_c = 0
        litter = {}

        count = 0

        for r in range(m):
            for c in range(n):

                if classroom[r][c] == 'S':
                    start_r = r
                    start_c = c

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = count
                    count += 1

        # No litter
        if count == 0:
            return 0

        # All litter collected
        all_mask = (1 << count) - 1

        # best[r][c][mask] = maximum energy we had
        # at this position after collecting this mask
        best = [
            [
                [-1] * (1 << count)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        # BFS queue
        queue = [(start_r, start_c, energy, 0)]

        best[start_r][start_c][0] = energy

        moves = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while queue:

            # Process one BFS level
            next_queue = []

            for r, c, current_energy, mask in queue:

                # We collected everything
                if mask == all_mask:
                    return moves

                # No energy means we cannot move
                if current_energy == 0:
                    continue

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Wall
                    if classroom[nr][nc] == 'X':
                        continue

                    # One move costs one energy
                    new_energy = current_energy - 1

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # Update litter mask
                    new_mask = mask

                    if (nr, nc) in litter:

                        bit = litter[(nr, nc)]

                        new_mask = new_mask | (1 << bit)

                    # IMPORTANT:
                    # If we have already reached this position
                    # with the same litter collected and MORE energy,
                    # this new state is useless.
                    if new_energy <= best[nr][nc][new_mask]:
                        continue

                    # Save the better energy
                    best[nr][nc][new_mask] = new_energy

                    next_queue.append(
                        (nr, nc, new_energy, new_mask)
                    )

            queue = next_queue
            moves += 1

        return -1