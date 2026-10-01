class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for j in h:
            if h[j]==1:
                return s.index(j)
        return -1