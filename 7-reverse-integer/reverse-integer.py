class Solution:
    def reverse(self, x: int) -> int:
        y=x
        y=abs(y)
        y=str(y)
        z=y[::-1]
        z=int(z)
        if z<=-2**31 or z>=2**31-1:
            return 0

        elif x<0:
            return -1*z
        else:
            return z