class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for ch in moves:
            if ch == "R" :
                y += 1
            elif ch == "L" :
                y -= 1
            elif ch == "U" :
                x += 1
            elif ch == "D" :
                x -= 1

        if x == 0 and y == 0:
            return True
        else:
            return False



        