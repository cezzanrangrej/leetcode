class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        num=[1,2,3,4,5,6,7,8,9]
        result,path=[],[]
        used=[False] * 9

        def fun(start, total):
            if len(path)==k and total==n:
                result.append(path[:])
                return
            
            if len(path)>k:
                return 
            if total> n:
                return 
            
            for i in range(start, 9):
                if used[i]==False:
                    path.append(num[i])
                    used[i]=True
                    fun(i+1, total+num[i])

                    path.pop()
                    used[i]=False
        fun(0,0)
        return result