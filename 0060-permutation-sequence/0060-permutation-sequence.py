class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        permu =''
        k -=1
        for i in range(n,0,-1):
            fac = math.factorial(i - 1)
            index = k//fac
            permu +=str(numbers.pop(index))
            k %= fac
        return permu
        