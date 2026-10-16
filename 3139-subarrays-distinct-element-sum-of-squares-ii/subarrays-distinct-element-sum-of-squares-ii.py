class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree
        total = [0] * (4 * n)
        square = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def add(node, left, right, value):
            length = right - left + 1

            square[node] += 2 * value * total[node] + value * value * length
            total[node] += value * length
            lazy[node] += value

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            value = lazy[node]

            add(node * 2, left, mid, value)
            add(node * 2 + 1, mid + 1, right, value)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                add(node, left, right, 1)
                return

            push(node, left, right)

            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = total[node * 2] + total[node * 2 + 1]
            square[node] = square[node * 2] + square[node * 2 + 1]

        last = {}
        answer = 0

        for right in range(n):
            num = nums[right]

            previous = last.get(num, -1)

            # Add 1 distinct element to this range
            update(1, 0, n - 1, previous + 1, right)

            last[num] = right

            # All subarrays ending at 'right'
            answer += square[1]
            answer %= MOD

        return answer
        