class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:

        ans=[]

        board=['.'*n for _ in range(n)]
        horizontal=[0]*n

        low_diagonal=[0]*(2*n-1)

        upper_diagonal=[0]*(2*n-1)


        def solve(horizontal,low_diagonal,upper_diagonal,col,board,ans,n):
            if col==n:
                ans.append(list(board))
                return

            for row in range(n):
                if horizontal[row]==0 and low_diagonal[row+col]==0 and upper_diagonal[n-1+col-row]==0:

                    board[row]=board[row][:col]+'Q'+board[row][col+1:]
                    horizontal[row]=1 
                    low_diagonal[row+col]=1
                    upper_diagonal[n-1+col-row]=1
                    solve(horizontal,low_diagonal,upper_diagonal,col+1,board,ans,n)
                    board[row]=board[row][:col]+'.'+board[row][col+1:]
                    horizontal[row]=0
                    low_diagonal[row+col]=0
                    upper_diagonal[n-1+col-row]=0
                    

        solve(horizontal,low_diagonal,upper_diagonal,0,board,ans,n)
        return ans
            