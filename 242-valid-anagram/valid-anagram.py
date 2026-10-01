class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sh=Counter(s)
        th=Counter(t)
        sort_sh=dict(sorted(sh.items()))
        sort_th=dict(sorted(th.items()))
        
        for i in sort_sh:
            if i not in sort_th:
                return False
            elif sort_sh[i] != sort_th[i]:
                return False
        return True