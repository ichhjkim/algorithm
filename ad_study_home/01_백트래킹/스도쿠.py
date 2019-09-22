sudoku = [list(map(int, input().split())) for _ in range(9)]

height = [0]*9
width = [0]*9
square = [0]*9
# 0의 개수를 셉니답.
# 0 위치 찾으면 index 찾아여
# 가로 체크 먼저, 네모 합 체크 먼저, 세로 체크크
def check():
