class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate each row
        for r in range(9):
            rowSet = set()
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if val in rowSet:
                        return False
                    rowSet.add(val)

        # Validate each column
        for c in range(9):
            colSet = set()
            for r in range(9):
                val = board[r][c]
                if val != '.':
                    if val in colSet:
                        return False
                    colSet.add(val)

        # Validate each 3x3 box
        for boxRow in range(0, 9, 3):       # 0, 3, 6
            for boxCol in range(0, 9, 3):   # 0, 3, 6
                boxSet = set()
                for r in range(boxRow, boxRow + 3):
                    for c in range(boxCol, boxCol + 3):
                        val = board[r][c]
                        if val != '.':
                            if val in boxSet:
                                return False
                            boxSet.add(val)

        return True
