#!/bash/bin/python

def done_or_notDone(board):
    temp = [1,2,3,4,5,6,7,8,9]

    for row in board:
        checkRuleB(row, temp)

    for i in range(0,9):
        tempList = []
        for j in range(0,9):
            tempList.append(board[j][i])
        checkRuleA(tempList, temp)
        checkRuleB(tempList)

    for i in range(0,7,3):
        for j in range(0,7,3):
            tempList = board[0+i:2+i, 0+j:2+j)]
            checkRuleA(tempList, temp)

    def checkRuleA(lst, temp):
        if set(lst) - set(temp) != set([]):
            return "Try again"
    def checkRuleB(lst):
        if sum(lst) != 45:
            return "Try again"
