class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """n = len(matrix) // 2
        for i in range(n):
            temp = matrix[i]
            matrix[i] = matrix[len(matrix) - 1 - i] 
            matrix[len(matrix) - 1 - i]  = temp
        
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp"""
        n = len(matrix) - 1
        l, t = 0, 0
        r, b = n, n
        while l < r and t < b:
            for i in range(r - l):
                temp = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = temp

            l += 1
            t += 1
            r -= 1
            b -= 1  

