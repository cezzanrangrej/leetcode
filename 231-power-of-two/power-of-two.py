class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def p(n):
            if n==1:
                return True
            if n<=0 or n%2!=0:
                return False
            return p(n//2)
        return p(n)