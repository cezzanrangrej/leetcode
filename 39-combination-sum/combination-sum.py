class Solution:
    def combinationSum(self, c: list[int], target: int) -> list[list[int]]:
        result=[]
        def fun(start,path,total):
            if total==target:
                result.append(path[:])
                return 
            
            if total>target:
                return
            for i in range(start, len(c)):
                path.append(c[i])
                fun(i,path,total+c[i])
                path.pop()
                
        fun(0,[],0)
        return result