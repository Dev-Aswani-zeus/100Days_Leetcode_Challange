import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        tree = [0] * (4 * k)

        def build(node, left, right):
            if left == right:
                tree[node] = 1
                return
            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]
        def update(node, left, right, index, value):
            if left == right:
                tree[node] = value
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, right, index, value)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]
        def find_first(node, left, right, ql, qr):
            if right < ql or left > qr or tree[node] == 0:
                return -1

            if left == right:
                return left

            mid = (left + right) // 2

            result = find_first(node * 2, left, mid, ql, qr)

            if result != -1:
                return result

            return find_first(node * 2 + 1, mid + 1, right, ql, qr)

        build(1, 0, k - 1)
        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            time = arrival[i]
            while busy and busy[0][0] <= time:
                finish, server = heapq.heappop(busy)
                update(1, 0, k - 1, server, 1)
            preferred = i % k

            server = find_first(1, 0, k - 1, preferred, k - 1)
            if server == -1:
                server = find_first(1, 0, k - 1, 0, preferred - 1)
            if server == -1:
                continue
            count[server] += 1
            update(1, 0, k - 1, server, 0)
            finish_time = time + load[i]
            heapq.heappush(busy, (finish_time, server))
        maximum = max(count)

        answer = []

        for i in range(k):
            if count[i] == maximum:
                answer.append(i)

        return answer