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
                            # print(board)
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

def solveNQueensDFS(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    def dfs(col,vals):
        if col==n: #每行都run好了
            res.append(vals)
            return
        curStr='.'*n
        for row in range(n): #決定row的位置
            if check(col,row): #查看是否可以放置
                board[col]=row
                #遞迴決定下一行
                dfs(col+1,vals+[ curStr[:row]+'Q'+curStr[row+1:] ])

    def check(col,row):
        for pos in range(col): #看先前的其他行是否已經有人列與當前row相等
            #若有哪列已經與row相等 or 斜對角相等 則false
            if board[pos]==row or abs(col-pos)==abs(row-board[pos]):
                return False
        return True

    board=[-1]*n #board[x]=y : 第x行、第y列中放置queen
    res=[]
    dfs(0,[])
    # print(len(res))
    return res

ret = solveNQueens(7)
print("sol: ", len(ret))
print("sol: ", ret)

ret = solveNQueensDFS(7)
print("sol: ", len(ret))
print("sol: ", ret)
# retList = [list(item) for item in ret]
# print("sol: ", retList)