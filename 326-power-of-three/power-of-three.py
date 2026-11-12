class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def fun(n):
            if n==1:
                return True
            if n<=0 or n%1!=0:
                return False
            n=n/3
            return (fun(n))
        return fun(n)