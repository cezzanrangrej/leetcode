class Solution:
    def secondHighest(self, s: str) -> int:
        mx=-1
        sm=-1
        for i in s:
            if i.isalpha():
                continue
            elif int(i)>sm and int(i)<mx:
                sm=int(i)
            elif int(i)>mx:
                sm=mx
                mx=int(i)
        return sm
    
