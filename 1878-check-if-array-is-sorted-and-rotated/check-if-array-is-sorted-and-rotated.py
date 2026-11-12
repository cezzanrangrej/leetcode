class Solution:
    def check(self, nums: list[int]) -> bool:
        def fun(c,i):
            n=len(nums)
            if i>len(nums)-1:
                return True
            if nums[i%n]>nums[(i+1)%n]:
                if c==1:
                    return False
                c+=1
            return fun(c,i+1)
        return fun(0,0)