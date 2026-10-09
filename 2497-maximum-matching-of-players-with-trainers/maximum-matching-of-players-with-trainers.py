class Solution:
    def matchPlayersAndTrainers(self, p: list[int], t: list[int]) -> int:
        c=0
        p.sort()
        t.sort()
        i=0
        j=0
        while i<len(p):
            if len(t)<=j: return c
            if p[i]>t[j]: j+=1
            else:
                c+=1
                j+=1
                i+=1
        return c