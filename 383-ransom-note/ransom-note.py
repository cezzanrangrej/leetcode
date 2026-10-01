class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r={}
        m={}
        for i in ransomNote:
            if i in r:
                r[i]+=1
            else:
                r[i]=1
        
        for j in magazine:
            if j in m:
                m[j]+=1
            else:
                m[j]=1

        for k in r:
            if k not in m:
                return False
            else:
                if r[k] > m[k]:
                    return False
        return True