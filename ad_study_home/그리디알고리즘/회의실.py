N = int(input())
rooms = []
for i in range(N):
    rooms.append(list(map(int, input().split())))

rooms = sorted(rooms, key=lambda element : (element[1], element[0]))
# print(rooms)
queue = [rooms[0]]
s = 1
count = 1
while queue:

    stand = queue.pop(0)
    for i in range(s, N):

        if stand[1] <= rooms[i][0]:
            s = i+1
            count += 1
            queue.append(rooms[i])
            break

print(count)






