class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_string = ""
            for i in range(0, len(s), k):
                group_sum = 0
                for j in range(i, min(i + k, len(s))):
                    group_sum += int(s[j])
                new_string += str(group_sum)
            s = new_string
        return s
