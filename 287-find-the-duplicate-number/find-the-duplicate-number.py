class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hm={}
        for i in nums:
            if i in hm:
                return i
            else:
                hm[i]=1
     