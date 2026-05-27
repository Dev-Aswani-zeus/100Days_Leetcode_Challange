class Solution:
    def calPoints(self, operations: List[str]) -> int:
        empty_list = []
        for operation in operations:
            if operation == "C":
                empty_list.pop()
            elif operation == "D":
                empty_list.append(empty_list[-1] * 2)
            elif operation == "+":
                empty_list .append(empty_list[-1] + empty_list[-2])
            else:
                empty_list.append(int(operation))
        return sum(empty_list)