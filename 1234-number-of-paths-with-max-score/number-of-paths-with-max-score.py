class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 1000000007
        n = len(board)

        # dp[i][j] = [maximum score, number of ways]
        dp = [[[ -1, 0 ] for _ in range(n)] for _ in range(n)]

        # Start from S
        dp[n-1][n-1] = [0, 1]

        # Traverse from bottom-right to top-left
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):

                # Skip blocked cells
                if board[i][j] == 'X':
                    continue

                # Skip S itself
                if i == n-1 and j == n-1:
                    continue

                bestScore = -1
                ways = 0

                # Three possible directions
                directions = [(1,0),(0,1),(1,1)]

                for dx, dy in directions:

                    ni = i + dx
                    nj = j + dy

                    if ni >= n or nj >= n:
                        continue

                    score, count = dp[ni][nj]

                    if score == -1:
                        continue

                    if score > bestScore:
                        bestScore = score
                        ways = count

                    elif score == bestScore:
                        ways = (ways + count) % MOD

                if bestScore == -1:
                    continue

                # Add current cell value
                if board[i][j].isdigit():
                    bestScore += int(board[i][j])

                dp[i][j] = [bestScore, ways]

        if dp[0][0][0] == -1:
            return [0,0]

        return [dp[0][0][0], dp[0][0][1] % MOD]