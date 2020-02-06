# 크기가 3*3 배열 A, 1초가 지날때마다 배열에 연산이 적용됨.
# R dustks 모든 행에 대해 정렬, 행의 갯수>=열의 갯수
# C 배열 A 모든 열에 대해서 정렬을 수행, 행의 갯수 < 열의 갯수

# 각각의 수가 행/열에서 정렬될때마다 몇번 나왔는지 알아야 함.
# 각각의 수가 몇번 나왔는지, 수의 등장 횟수가 커지는 순으로, 수의 등장 횟수가 동일하면 수가 커지는 순으로

# 각 연산이 진행된 후, 행의 크기가 가장 큰 행을 기준으로 모든 행의 크기가 커지고,
# 정렬하고 새롭게 생긴 공간은 0으로 채워 넣는다.
## 또 행/열의 크키가 100을 넘어가는 경우, 처음 100개를 제외한 나머지는 버린다.

# r, c, k가 주어졌을 떄, A[r][c]에  들어있는 값 ==k일때 까지의 최소시간을 구해랏

r, c, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(3)]

# 행
height = len(board)
# 열
width = len(board[0])

def R():
    newBoard = []
    for y in range(len(board)):
        temp = {}
        for x in range(len(board[0])):

