class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=[]

        board=['.'*n for _ in range(n)]

        def issafe(row,col,board,n):
            drow=row
            dcol=col

            while row>=0 and col>=0:
                if board[row][col]=='Q':
                    return False
                row-=1
                col-=1
            row=drow
            col=dcol

            while col>=0:
                if board[row][col]=='Q':
                    return False
                col-=1
            
            row=drow
            col=dcol
            
            while row<n and col>=0:
                if board[row][col]=='Q':
                    return False
                row+=1
                col-=1

            return True

        def solve(col,board,ans,n):
            if col==n:
                ans.append(list(board))
                return

            for row in range(n):
                if issafe(row, col, board, n):
                    board[row]=board[row][:col]+'Q'+board[row][col+1:]
                    solve(col+1,board,ans,n)
                    board[row]=board[row][:col]+'.'+board[row][col+1:]

        solve(0,board,ans,n)
        return len(ans)