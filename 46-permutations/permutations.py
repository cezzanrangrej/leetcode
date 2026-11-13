class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        result=[]
        def bt(path):
            if len(path)==len(nums):
                result.append(path[:])
                return
                
            for i in nums:
                if i not in path:
                    path.append(i)
                    bt(path)
    
                    path.pop()
        

        bt([])
        return result