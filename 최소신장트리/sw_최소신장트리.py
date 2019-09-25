import sys

sys.stdin = open('최소신장트리.txt', 'r')

T = int(input())

def union(x, y):
    parents[finding(y)] = finding(x)

def finding(x):
    if parents[x] == x:
        return x
    else:
        finding(parents[x])


for tc in range(1, T+1):

    V, E = map(int, input().split())

    board = [0]*(E)

    for r in range(E):
        a, b, w = map(int, input().split())
        board[r] = [w, a, b]

    print(board)
    # 자식 부모
    parents = [v for v in range(V+1)]

    for _ in range(E):

        b = board.pop(0)

        parents[b[2]] = b[1]
