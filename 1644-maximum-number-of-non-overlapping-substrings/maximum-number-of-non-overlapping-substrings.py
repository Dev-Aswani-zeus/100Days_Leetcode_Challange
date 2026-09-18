class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26
        for i in range(n):
            x = ord(s[i]) - ord('a')

            if first[x] == n:
                first[x] = i

            last[x] = i

        intervals = []
        for i in range(n):
            x = ord(s[i]) - ord('a')
            if first[x] != i:
                continue

            left = i
            right = last[x]
            valid = True

            j = left

            while j <= right:
                y = ord(s[j]) - ord('a')
                if first[y] < left:
                    valid = False
                    break
                right = max(right, last[y])

                j += 1

            if valid:
                intervals.append((left, right))
        intervals.sort(key=lambda x: (x[1], -x[0]))

        answer = []
        previous_end = -1

        for left, right in intervals:
            if left > previous_end:
                answer.append(s[left:right + 1])
                previous_end = right

        return answer