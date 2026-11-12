class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def bt(open, close, n, s, res):
            if open==n and close==n:
                res.append("".join(s[:]))
                return
            
            if open<n:
                s.append('(')
                bt(open+1, close, n, s, res)
                s.pop()
            if close < open:
                s.append(')')
                bt(open, close+1, n, s, res)
                s.pop()
            return res
        return bt(0,0,n,[],[])