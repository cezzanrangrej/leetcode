class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0
        if bills[0] != 5:
            return False

        for i in bills:
            if i==5:
                five+=1
            elif i==10:
                ten+=1
                if not five>0:
                    return False
                five-=1
            elif i==20:
                if not five>0:
                    return False
                five-=1
                if ten>0:
                    ten-=1
                    continue
                elif not five>=2:
                    return False
                five-=2
        return True
