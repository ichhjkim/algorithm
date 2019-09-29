def combination(result, s, depth):
    global max_result, M

    if depth == 3:
        if max_result < result and result <= M:
            max_result = result

    else:
        for i in range(s, len(cards)):
            combination(result+cards[i], i+1, depth+1)


N, M = map(int, input().split())

cards = list(map(int, input().split()))
max_result = 0
combination(0, 0, 0)
print(max_result)