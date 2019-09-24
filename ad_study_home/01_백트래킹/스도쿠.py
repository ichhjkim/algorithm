sudoku = [list(map(int, input().split())) for _ in range(9)]

def cheight(x, y):
    global candidates

    height = [0] * 10
    for i in range(9):
        if sudoku[i][y]:
            height[sudoku[i][y]] = 1

    for h in range(1, 10):
        if not height[h]:
            if h not in candidates:
                candidates.append(h)

def cwidth(x, y):
    global candidates

    width = [0] * 10
    for i in range(9):
        if sudoku[x][i]:
            width[sudoku[x][i]] = 1

    for w in range(1, 10):
        if not width[w]:
            if w not in candidates:
                candidates.append(w)


def csquare(x, y):
    global candidates

    square = [0] * 10

    sero = x//3
    garo = y //3

    for i in range(sero*3, 3*sero+3):
        for j in range(garo*3, 3*garo+3):
            if sudoku[i][j]:
                square[sudoku[i][j]] = 1

    for s in range(1, 10):
        if not square[s]:
            if s not in candidates:
                candidates.append(s)





def verify():
    s_height = 0
    s_width = 0
    s_square = 0
    for i in range(9):
        for j in range(9):
            s_height += sudoku[j][i]
            s_width += sudoku[i][j]
        else:
            if s_height != 45 or s_width != 45:
                return False
            s_height = 0
            s_width = 0

    for m in range(3):
        for n in range(3):
            for a in range(3):
                for b in range(3):
                    s_square += sudoku[3*m+a][3*n+b]

            else:
                if s_square != 45:
                    return False
                s_square = 0

    return True

zeros = []
candidates = []
for x in range(9):
    for y in range(9):
        if not sudoku[x][y]:
            cheight(x, y)
            cwidth(x, y)
            csquare(x, y)
            zeros.append([[x, y], candidates])
            candidates = []

z = 0

def backtrack(z):
    # print(z)
    if z == len(zeros):
        if verify():
            for s in range(9):
                for g in range(9):
                    print(sudoku[s][g], end=' ')
                print()
            return

    else:
        for i in range(len(zeros[z][1])):
            sudoku[zeros[z][0][0]][zeros[z][0][1]] = zeros[z][1][i]
            backtrack(z+1)
            sudoku[zeros[z][0][0]][zeros[z][0][1]] = 0

backtrack(z)







