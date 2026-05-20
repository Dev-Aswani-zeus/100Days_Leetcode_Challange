class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        arr1 = []
        arr2 = []

        for i in range(1, n+1):
            if i % m != 0:
                arr1.append(i)
            else:
                arr2.append(i)
        num1 = 0
        for j in range(len(arr1)):
            num1 += arr1[j]


        num2 = 0
        for k in range(len(arr2)):
            num2 += arr2[k]


        return num1 - num2
                 


