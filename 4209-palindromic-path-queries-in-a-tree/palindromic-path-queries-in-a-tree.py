class Solution:
    def palindromePath(self, n: int, edges: list[list[int]],
                       s: str, queries: list[str]) -> list[bool]:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            biggest = 0

            for v in graph[u]:
                if parent[v] == u and v != u:
                    size[u] += size[v]

                    if size[v] > biggest:
                        biggest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u] and v != u:
                        stack.append((v, v))

                u = heavy[u]

        bit = [0] * (n + 1)

        def update(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def prefix(i):
            result = 0
            i += 1

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        def range_xor(l, r):
            result = prefix(r)

            if l > 0:
                result ^= prefix(l - 1)

            return result

        letters = list(s)

        def mask(c):
            return 1 << (ord(c) - ord('a'))

        for u in range(n):
            update(pos[u], mask(letters[u]))

        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])
            return result

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                old_mask = mask(letters[u])
                new_mask = mask(new_char)

                update(pos[u], old_mask ^ new_mask)
                letters[u] = new_char

            else:
                u = int(parts[1])
                v = int(parts[2])

                value = path_xor(u, v)

                answer.append(
                    value == 0 or (value & (value - 1)) == 0
                )

        return answer