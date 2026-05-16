class Solution:
    def addDigits(self, num: int) -> int:
        # total = 0
        # while num > 10:
        #     for digit in str(num):
        #         total += int(digit)
        #     num = total
        # return num
        
        
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num = num // 10
            num = total
        return num