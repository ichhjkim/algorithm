game = [
    [[-1, 2, 4, 6, 8, 10]],
    [[12, 14, 16, 18, 20], [13, 16, 19, 25]],
    [[22, 24, 26, 28, 30], [22, 24, 25]],
    [[32, 34, 36, 38, 40, -1], [28, 27, 26, 25]],
    # 25일떄
    [[30, 35, 40, -1]]
]
visited = [
    [[0]*5],
    [[0]*6, [0]*5],
    [[0]*6, [0]*4],
    [[0]*6, [0]*5],
    [[0]*4]
]

horses = [[0, 0, 0, 0] for _ in range(4)]
nums = list(map(int, input().split()))
max_result = 0


def moving(num, h):
    orih = h[:]
    for i in range(num):
        h[3] += 1
        if h[3] == len(game[h[1]][h[2]])-1:
            if game[h[1]][h[2]][h[3]] == 10 or game[h[1]][h[2]][h[3]] == 20 or game[h[1]][h[2]][h[3]]==30:
                if game[h[1]][h[2]][h[3]] == 30 and game[h[1]][h[2]][0] == 25:
                    pass
                else:
                    if i < num-1:
                        h[1] += 1
                        h[3] = 0
                    elif i == num-1:
                        h[1] += 1
                        h[2] = 1
                        h[3] = 0

            elif game[h[1]][h[2]][h[3]] == 25:
                h[1] = 4
                h[2] = 0
                h[3] = 0
            elif game[h[1]][h[2]][h[3]] == -1:
                h[0] = 1
                return 0

    if not visited[h[1]][h[2]][h[3]]:
        visited[h[1]][h[2]][h[3]] = 1
        visited[orih[1]][orih[2]][orih[3]] = 0
        return game[h[1]][h[2]][h[3]]

    else:
        return -1

def work(depth, result):
    global max_result, visited

    if depth == 10:
        if result > max_result:
            max_result = result

    else:
        for i in range(4):
            if not horses[i][0]:
                temp = moving(nums[depth], horses[i])
                if temp != -1:
                    print(depth, temp, result+temp)
                    work(depth+1, result+temp)
            else:
                work(depth+1, result)




work(0, 0)
print(max_result)

'''
game = [
    [[2, 4, 6, 8, 10]],
    [[12, 14, 16, 18, 20], [13, 16, 19, 25]],
    [[22, 24, 26, 28, 30], [22, 24, 25]],
    [[32, 34, 36, 38, 40], [28, 27, 26, 25]],
    # 25일떄
    [[30, 35, 40]]
]
num, horse
num
[0, 0, 0, 0]
'''









