class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            return  1./(self.myPow(x,-n))
        if  n%2==0:
            return self.myPow(x*x,n/2)
        else:
            return x*self.myPow(x,n-1)


class Solution:
    # what is cache?
    @functools.lru_cache(maxsize = None)
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        if n == 0:
            return 1
        
        half_pow = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half_pow*half_pow
        else:
            return x*half_pow*half_pow
        