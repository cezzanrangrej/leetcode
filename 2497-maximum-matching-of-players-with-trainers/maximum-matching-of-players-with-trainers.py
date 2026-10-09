class Solution:
    def matchPlayersAndTrainers(self, p: list[int], t: list[int]) -> int:
        c=0
        p.sort()
        t.sort()
        i=0
        j=0
        while i<len(p) and j< len(t):
            if p[i]<=t[j]:
                c+=1
                i+=1
                j+=1
            else:
                j+=1
        return c