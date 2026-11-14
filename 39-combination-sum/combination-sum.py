class Solution:
    def combinationSum(self, c: list[int], target: int) -> list[list[int]]:
        result,path=[],[]
        def fun(start,total):
            if total==target:
                result.append(path[:])
                return 
            
            if total>target:
                return

            for i in range(start, len(c)):
                path.append(c[i])
                fun(i,total+c[i])
                path.pop()
                
        fun(0,0)
        return result