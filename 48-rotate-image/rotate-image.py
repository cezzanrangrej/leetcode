class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
        for k in range(n):
            left=0
            right=n-1
            while left < right:
                matrix[k][left],matrix[k][right]=matrix[k][right],matrix[k][left]
                left += 1
                right-= 1