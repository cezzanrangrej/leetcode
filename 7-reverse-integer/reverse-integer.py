class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        s=list(str(abs(x)))
        def r(left, right):
            if left>right:
                re=(int("".join(s)))
                if re>2**31-1 or re<-2**31:
                    return 0
                return sign*re
            s[left],s[right]=s[right],s[left]

            return r(left+1,right-1)
        return r(0,len(s)-1)