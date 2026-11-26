class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        c=0
        m=10
        for _ in range(9):
            if n<0 and c%2!=0:
                return False
            elif n<0 and c%2==0:
                return True
            n-=m
            m-=1
            c+=1