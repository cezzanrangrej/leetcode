class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def r(left, right):
            if left>right:
                return s
            s[left],s[right]=s[right],s[left]

            return r(left+1,right-1)
        return r(0,len(s)-1)