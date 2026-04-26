class Solution:
    def searchMatrix(self, board: List[List[int]], target: int) -> bool:
        tr = 0
        lc = 0
        br = len(board) - 1
        rc = len(board[0]) - 1

        while tr <= br and lc <= rc:
            mr = (tr + br) // 2
            mc = (lc + rc) // 2

            if board[mr][mc] == target:
                return True
            
            # how to know if we want to update the row
            lb1 = board[mr][lc]
            lb2 = board[mr][rc]

            if target < lb1:
                br = mr - 1
            elif target > lb2:
                tr = mr + 1
            else:
                if board[mr][mc] > target:
                    rc = mc - 1
                else:
                    lc = mc + 1
        return False