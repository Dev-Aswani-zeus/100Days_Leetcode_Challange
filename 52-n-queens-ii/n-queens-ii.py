class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        board = []
        def is_safe(row, col):
            for r in range(row):
                c = board[r]
                if c == col:
                    return False
                if abs(r - row) == abs(c - col):
                    return False
            return True
        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if is_safe(row, col):
                    board.append(col)
                    backtrack(row + 1)
                    board.pop()
        backtrack(0)
        return count