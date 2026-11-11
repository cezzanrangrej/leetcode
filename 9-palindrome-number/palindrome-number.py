class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        def p(s,left,right):
            if right-left==0 or left>=right:
                return True
            if s[left]!=s[right]:
                return False          
            return p(s,left+1, right-1)
        return p(s,0,len(s)-1)