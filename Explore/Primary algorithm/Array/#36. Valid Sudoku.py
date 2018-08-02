# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# A partially filled sudoku which is valid.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# Example 1:
#
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# Example 2:
#
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        flag = True
        check9 = []
        for row in board:
            for col in range(9):
                if row[col] == '.':
                    continue
                check9.append(int(row[col]))
            flag = flag and self.isValid9nums(check9)
            check9 = []
        if flag is False:
            return False

        check9 = []
        for row in range(9):
            for col in range(9):
                if board[col][row] == '.':
                    continue
                check9.append(int(board[col][row]))
            flag = flag and self.isValid9nums(check9)
            check9 = []
        if flag is False:
            return False

        check9 = []
        for subboard in range(9):
            row = subboard % 3
            col = int(subboard / 3)
            for i in range(3):
                for j in range(3):
                    if board[col*3 + i][row*3 + j] == '.':
                        continue
                    check9.append(int(board[col*3 + i][row*3 + j]))
            flag = flag and self.isValid9nums(check9)
            check9 = []

        return flag

    def isValid9nums(self, nums):
        checkbit = float('inf')
        if len(nums) > 1:
            nums.sort()
            for n in range(len(nums) - 1):
                checkbit = nums[n + 1] - nums[n]
                if checkbit == 0:
                    return False
        return True