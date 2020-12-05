def solution(board, r, c):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    min_result = 999999999999


    return answer

def check(board):

    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                return True

    return False

def ctrl(direction, recent, board):

    now = [recent[0], recent[1]]

    while True:

        if now[0] < 0 or now[1] < 0 or now[0] > 3 or now[1] > 3:
            now[0] -= direction[0]
            now[1] -= direction[1]
            return now

        if board[now[0]][now[1]]:
            return now
        else:
            now[0] += direction[0]
            now[1] += direction[1]

