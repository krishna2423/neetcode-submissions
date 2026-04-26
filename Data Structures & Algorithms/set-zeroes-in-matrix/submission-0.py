class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for c in range(len(matrix[0])):
                        zeros.add((i, c))
                    for r in range(len(matrix)):
                        zeros.add((r, j))
     
        for x in zeros:
            matrix[x[0]][x[1]] = 0