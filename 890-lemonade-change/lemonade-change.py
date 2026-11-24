class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        if len(bills)==1 and bills[0]==5:
            return True
        if len(bills)==1 or bills[1]<bills[0] : 
            return False
        c5=0
        c10=0
        for i in range(len(bills)):
            if bills[i]==5:
                c5+=1
            elif bills[i]==10 and c5>0:
                c5-=1
                c10+=1
            elif bills[i]==20 and c5>0:
                if c10>0:
                    c10-=1
                    c5-=1
                elif c5>=3:
                    c5-=3
                else:
                    return False
            else:
                return False
        return True
