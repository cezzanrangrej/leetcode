class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        path,result=[],[]
        used=[False] * len(nums)
        def fun():
            if len(path)==len(nums) and path not in result:
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]==False:
                    path.append(nums[i])
                    used[i]=True
                    fun()

                    path.pop()
                    used[i]=False    
        fun()
        return result