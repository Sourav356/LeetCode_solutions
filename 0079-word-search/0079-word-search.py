class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, idx):
            if idx == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[idx]:
                return False
            temp, board[row][col] = board[row][col], '/'
            res = backtrack(row + 1, col, idx + 1) or \
              backtrack(row - 1, col, idx + 1) or \
              backtrack(row, col + 1, idx + 1) or \
              backtrack(row, col - 1, idx + 1)
            board[row][col] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
        