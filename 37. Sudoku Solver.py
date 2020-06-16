class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # self.tmp = board
        self.func(board)
        return

    def func(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    available = [str(x) for x in range(1, 10)]
                    # print(available)
                    for t in range(9):
                        if board[i][t] in available:
                            available.remove(board[i][t])
                        if board[t][j] in available:
                            available.remove(board[t][j])
                    smallX = i // 3
                    smallY = j // 3
                    for x in range(smallX * 3, smallX * 3 + 3):
                        for y in range(smallY * 3, smallY * 3 + 3):
                            if board[x][y] in available:
                                available.remove(board[x][y])
                    if len(available) == 0:
                        return False

                    for c in available:
                        board[i][j] = c
                        tmp = self.func(board)
                        if tmp == True:
                            return True
                    board[i][j] = '.'
                    return False
        return True


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(board)
    solution = Solution()
    solution.solveSudoku(board)
    print(board)