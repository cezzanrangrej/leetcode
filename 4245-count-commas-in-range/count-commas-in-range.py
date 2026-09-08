class Solution:
    def countCommas(self, n: int) -> int:
        if n>=1000:
            return(n-1000+1)
        else:
            return 0