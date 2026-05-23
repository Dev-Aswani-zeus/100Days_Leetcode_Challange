class Solution:
    def countPrimes(self, n: int) -> int:
        # count = 0
        # for num in range(2, n):

        #     is_prime = True
        #     for i in range(2, num):
        #         if num % i == 0:
        #             is_prime = False
        #             break
        #     if is_prime:
        #         count += 1
        # return count
        

        #chatgpt code because my logic throwed a time out just pasted it so i could submit
        if n <= 2:
            return 0

        prime = [True] * n

        prime[0] = False
        prime[1] = False


        for i in range(2, int(n**0.5)+1):

            if prime[i]:

                for j in range(i*i, n, i):
                    prime[j] = False


        return sum(prime)