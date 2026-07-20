class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n + 1):
            count = 0
            num = i
            while num > 0:
                if num % 2 == 1:
                    count += 1
                num //= 2
            answer.append(count)
        return answer