import sys
from itertools import permutations

N = int(sys.stdin.readline())
scores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_result = -1

def play(candi):
    # 9명 // 수비 공격 번갈아
    # N 이닝동안 게임 진행,

    idx = 0
    result = 0
    for score in scores:

        b1, b2, b3 = 0, 0, 0
        out = 0
        while out < 3:
            # 아웃인 경우
            if score[candi[idx]] == 0:
                out += 1
            elif score[candi[idx]] == 1:
                result += b3
                b1, b2, b3 = 1, b1, b2

            elif score[candi[idx]] == 2:
                result += (b2+b3)
                b1, b2, b3 = 0, 1, b1

            elif score[candi[idx]] == 3:
                result += (b1+b2+b3)
                b1, b2, b3 = 0, 0, 1
            else:
                result += (b1+b2+b3+1)
                b1, b2, b3 = 0, 0, 0
            idx = (idx+1) % 9


    return result


for candi in permutations(range(1, 9), 8):
    candi = list(candi[:3]) + [0] + list(candi[3:])
    max_result = max(max_result, play(candi))

print(max_result)