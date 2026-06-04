class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ans = 1
        # if n >= 0:
        #     for i in range(n):
        #         ans = ans*x
        # else:
        #     for i in range(-n):
        #         ans = ans*x
        #     ans = 1/ans
        # return ans

        # commenting my logic code and pasting gpt code because time limit exceeded :(


        if n < 0:
            x = 1 / x
            n = -n

        ans = 1

        while n > 0:

            if n % 2 == 1:
                ans = ans * x

            x = x * x

            n = n // 2

        return ans

        
        