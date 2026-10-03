class Solution:
    def strStr(self, h: str, n: str) -> int:
        hl=len(h)
        nl=len(n)
        temp=nl
        left=0
        while left<hl:
            if h[left:temp]==n:
                return left
            else:
                left+=1
                temp+=1
        return -1