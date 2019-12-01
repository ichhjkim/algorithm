N = int(input())

seats = list(map(int, input().split()))
max_count = 0
count = 0
for s in range(N):
    if seats[s]:
        count = 1
    else:
        count += 1
        if count > max_count:
            max_count = count

print(max_count//2)
