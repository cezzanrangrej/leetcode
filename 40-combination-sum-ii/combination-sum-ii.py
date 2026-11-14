class Solution:
    def combinationSum2(self, c: list[int], target: int) -> list[list[int]]:
        c.sort()
        n=len(c)
        result,path,=[],[]
        used=[False]*n
        def fun(start,total):
            if total==target:
                result.append(path[:])
                return
            
            if total>target:
                return 
                
            
            for i in range(start,n):
                if i > start and c[i] == c[i-1]:
                    continue
                if used[i]==False:
                    path.append(c[i])
                    used[i]=True
                    fun(i+1,total+c[i])

                    path.pop()
                    used[i]=False
        fun(0,0)
        return result
        