M, C = map(int, input().split())
messages = [0]*M
for i in range(M):
    messages[i] = int(input())

consumers = [0]*C
# 위 리스트의 max 값을 구하면 됨
for m in range(M):
    idx = consumers.index(min(consumers))
    consumers[idx] += messages[m]

print(max(consumers))