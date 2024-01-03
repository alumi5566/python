import copy
def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    ret = set()
    board = [['.' for i in range(n)] for j in range(n)]
    def isValid(row, col, board):
        cnt = 0
        for i in range(n):
            if board[row][i] == 'Q':
                cnt += 1
        if cnt > 1:
            # print("row cnt ",cnt)
            return False

        cnt = 0
        for j in range(n):
            if board[j][col] == 'Q':
                cnt += 1
        if cnt > 1:
            # print("col cnt ",cnt)
            return False

        cnt = 0
        i, j = row, col
        while i >= 0 and i < n and j >=0 and j < n:
            if board[i][j] == 'Q':
                cnt += 1
            i += 1
            j += 1
        if cnt > 1:
            return False

        cnt = 0
        i, j = row, col
        while i >= 0 and i < n and j >=0 and j < n:
            if board[i][j] == 'Q':
                cnt += 1
            i -= 1
            j -= 1
        if cnt > 1:
            return False

        cnt = 0
        i, j = row, col
        while i >= 0 and i < n and j >=0 and j < n:
            if board[i][j] == 'Q':
                cnt += 1
            i += 1
            j -= 1
        if cnt > 1:
            return False

        cnt = 0
        i, j = row, col
        while i >= 0 and i < n and j >=0 and j < n:
            if board[i][j] == 'Q':
                cnt += 1
            i -= 1
            j += 1
        if cnt > 1:
            return False
        return True
    # def transger(board):
    #     for i in range(n):
    #
    def backtracking(board, queen):
        # print(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    board[i][j] = 'Q'
                    if isValid(i, j, board):
                        # print("valid:", i, j)
                        if queen+1 == n:
                            print(board)
                            ret.add(tuple(map(tuple, board)))
                            # ret.append(copy.copy(board))
                            board[i][j] = '.'
                            return
                        backtracking(board, queen+1)
                        board[i][j] = '.'
                    else:
                        # print("not valid:", i, j)
                        board[i][j] = '.'
        return True
    backtracking(board, 0)
    # print(isValid(0, 0, [["Q"]]) )
    res = []
    for r in ret:
        tmp = []
        for i in range(n):
            tmp.append("".join(r[i]))
        res.append(tmp)

    return res

ret = solveNQueens(7)
print("sol: ", ret)

# retList = [list(item) for item in ret]
# print("sol: ", retList)