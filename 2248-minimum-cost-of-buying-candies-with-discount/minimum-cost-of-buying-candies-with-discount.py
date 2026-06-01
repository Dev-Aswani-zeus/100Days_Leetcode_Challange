class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        i = 0
        while i < len(cost):
            total += cost[i]
            if i + 1 < len(cost):
                total += cost[i + 1]
            i += 3
        return total