class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        result=[]
        used=[False]*len(nums)
        def bt(path):
            if len(path)==len(nums):
                result.append(path[:])
                return
                
            for i in range(len(nums)):
                if used[i]==False:
                    path.append(nums[i])
                    used[i]=True
                    bt(path)
    
                    path.pop()
                    used[i]=False
        

        bt([])
        return result