class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        p=2
        pp=1
        ans=0

        for i in range(3,n+1):
            ans=p+pp
            pp=p
            p=ans

        return ans