W, H = map(int, input().split())
# 가로 세로인 것을 조심하자
start = [0, 0]
coni_w, coni_h = map(int, input().split())
flag = True

if coni_w > W-1 or coni_h > H-1 or coni_w < 0 or coni_h < 0:
    flag = False

# 걸리는 시간
sum_coni = coni_w + coni_h
upper = 1
for u in range(2, sum_coni+1):
    upper *= u

garo = sero = 1

for g in range(2, coni_w+1):
    garo *= g

for s in range(2, coni_h+1):
    sero *= s

result = upper / (garo*sero)
if flag:
    print(sum_coni)
    print(int(result))
else:
    print('fail')
# 가로 최댓값 coni_W, 세로 최댓값 coni_h