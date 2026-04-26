class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) // 2
        for i in range(n):
            temp = matrix[i]
            matrix[i] = matrix[len(matrix) - 1 - i] 
            matrix[len(matrix) - 1 - i]  = temp
        
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        