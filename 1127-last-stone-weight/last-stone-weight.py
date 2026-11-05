class Solution:
    def lastStoneWeight(self, s: list[int]) -> int:
        while len(s)>=2:
            s.sort(reverse=True)
            ans=s[0]-s[1]
            s.pop(1)
            s.pop(0)
            s.append(ans)
        if s:
            return s[-1]
        else:
            return 0