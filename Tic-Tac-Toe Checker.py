def isSolved(board):
    arr = ""
    #row check
    col_board = []
    
    for j in range(3):
        ele = []
        for i in board:
            ele.append(i[j])
            i = list(map(str,i))
            if "".join(i) == "111":
                return 1
            elif "".join(i)=="222":
                return 2
            else:
                arr = arr + "".join(i)
        col_board.append(ele)
    del ele
    
    #DIAGONAL CHECK
    ## left diag check
    diag = ""
    for i in range(3):
        diag = diag + str(board[i][i])
    if diag == "111":
        return 1
    elif diag == "222":
        return 2
    
    ##right diagonal
    diag = ""
    for i,j in zip(range(3),reversed(range(3))):
        diag = diag + str(board[i][j])
    if diag == "111":
        return 1
    elif diag == "222":
        return 2
    
    #COLUMN CHECK
    board = col_board
    del col_board
    for i in board:
        i = list(map(str,i))
        if "".join(i) == "111":
                #print("yes")
            return 1
        elif "".join(i)=="222":
            return 2
        
    del board
    
    #finally check if space left(-1) or not(0)
    arr = [str(i) for i in arr]
    if "0" in arr:
        return -1
    else:
        return 0
