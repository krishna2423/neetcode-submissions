class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        bottom = len(matrix) - 1
        top = 0
        right = len(matrix[0]) - 1
        left = 0
        while top <= bottom and left <= right:
            i = top
            j = left
            while j <= right:
                res.append(matrix[i][j])
                j += 1
            top += 1
            i = top
            j = right
            while i <= bottom:
                res.append(matrix[i][j])
                i += 1
            right -= 1
            i = bottom
            j = right
            if top <= bottom:
                while j >= left:
                    res.append(matrix[i][j])
                    j -= 1
                bottom -= 1
                i = bottom
                j = left
            if left <= right:
                while i >= top:
                    res.append(matrix[i][j])
                    i -= 1
                left += 1
        return res