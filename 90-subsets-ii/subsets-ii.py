class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        def fun(start,path):
            #if start==len(nums):
            result.append(path[:])
                #return
                
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                fun(i+1,path)
                path.pop()


        fun(0,[])
        return result