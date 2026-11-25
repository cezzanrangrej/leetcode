class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ht={}
        for i in s:
            if i in ht:
                return i
            else:
                ht[i]=1