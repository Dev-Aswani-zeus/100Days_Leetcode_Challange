class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        need = [0, 0, 0, 0]  # powers needed for 2, 3, 5, 7

        for i, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                need[i] += 1
                t //= p

        # Digits 1..9 cannot provide any other prime factor.
        if t != 1:
            return "-1"

        # Prime-factor contribution of each digit.
        factors = [
            (0, 0, 0, 0),  # 0 (not allowed)
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        def remaining(req, digit):
            f = factors[digit]

            return (
                max(0, req[0] - f[0]),
                max(0, req[1] - f[1]),
                max(0, req[2] - f[2]),
                max(0, req[3] - f[3]),
            )

        # Minimum number of digits required to satisfy req.
        def min_digits(req):
            a, b, c, d = req

            # 5 and 7 each require their own digit.
            base = c + d

            # Minimum digits needed for factors 2 and 3.
            best = 10**9

            # Use some 6s (2*3), then cover remaining
            # 2s using 8/4/2 and 3s using 9/3.
            for six in range(min(a, b) + 1):
                left2 = a - six
                left3 = b - six

                count = (
                    six
                    + (left2 + 2) // 3
                    + (left3 + 1) // 2
                )

                best = min(best, count)

            return base + best

        n = len(num)

        # Prefix requirements:
        # req_before[i] = remaining factors before num[i].
        req_before = [None] * (n + 1)
        req_before[0] = tuple(need)

        zero_pos = -1

        for i in range(n):
            if num[i] == '0':
                zero_pos = i
                break

            req_before[i + 1] = remaining(
                req_before[i],
                int(num[i])
            )

        # num itself already works.
        if zero_pos == -1 and req_before[n] == (0, 0, 0, 0):
            return num

        # Try changing a digit from right to left.
        #
        # Keep prefix same, increase this digit,
        # then fill suffix with smallest possible digits.

        start = n - 1

        if zero_pos != -1:
            start = zero_pos

        for i in range(start, -1, -1):

            # If prefix contains zero, it cannot be preserved.
            if req_before[i] is None:
                continue

            current = int(num[i])

            # If current is 0, start from 1.
            first = max(1, current + 1)

            for d in range(first, 10):
                req = remaining(req_before[i], d)

                slots = n - i - 1

                if min_digits(req) > slots:
                    continue

                # Construct lexicographically smallest suffix.
                suffix = []
                cur_req = req

                for pos in range(slots):
                    left = slots - pos - 1

                    for x in range(1, 10):
                        nxt = remaining(cur_req, x)

                        if min_digits(nxt) <= left:
                            suffix.append(str(x))
                            cur_req = nxt
                            break

                return num[:i] + str(d) + ''.join(suffix)

        # Cannot make a same-length answer.
        # Build the smallest longer answer.

        length = n + 1

        while min_digits(tuple(need)) > length:
            length += 1

        answer = []
        req = tuple(need)

        for i in range(length):
            left = length - i - 1

            for d in range(1, 10):
                nxt = remaining(req, d)

                if min_digits(nxt) <= left:
                    answer.append(str(d))
                    req = nxt
                    break

        return ''.join(answer)