N = int(input())
rooms = []
for i in range(N):
    rooms.append(list(map(int, input().split())))

rooms = sorted(rooms, key=lambda element: element[1])
compare = sorted(rooms)
max_count = 0
print(rooms)
print(compare)
queue = [rooms[0]]
idx = 0
while queue:
    count = 0
    print(queue, '큐========')
    temp = queue.pop(0)
    for j in range(N):
        if temp == compare[j]:
            continue
        if compare[j][0] < temp[1] and compare[j][1] > temp[0]:
            print(compare[j], '인덱스')
            count += 1
        elif compare[j][0] >= temp[1]:
            queue.append(compare[j])
            idx = compare.index(compare[j])
            break

    if max_count < count:
        max_count = count

print(max_count)

