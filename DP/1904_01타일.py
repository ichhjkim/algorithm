# 00, 1
n = int(input())
# 피보나치처럼 풀면 되지 않을까
result = [0]*(n+1)
tile = [0]*2
for i in range(1, n+1):
    if i==1:
        tile[0] = 1
    elif i==2:
        tile[1] = 2
    else:
        tile[1], tile[0] = (tile[0]+tile[1])%15746, tile[1]

print(tile[1])