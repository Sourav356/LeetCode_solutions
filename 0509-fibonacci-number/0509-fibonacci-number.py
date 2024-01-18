class Solution:
    def fib(self, n: int) -> int:
        i = 2
        first = 0
        second = 1
        if n == 0 or n == 1:
            return n
        while i <= n:
            fn = first + second
            first,second = second, fn
            i+=1
        return fn
        