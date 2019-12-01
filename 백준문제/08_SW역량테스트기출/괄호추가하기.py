def combination(depth, st, result):
    global m
    if depth == m:
        confirm(result)

    else:
        for i in range(st, len(calcul)):
            result.append(calcul[i])
            combination(depth+1, i+2, result)
            result.pop()

def confirm(final):
    global f_result
    visited = [0] * N
    final = final[:]
    new_result = []
    for f in range(len(final)):
        for idx in range(3):
            visited[final[f][idx]] = 1

    for v in range(1, N):
        if v-1 == 0 and not visited[v-1]:
            new_result.append(contents[v-1])

        if not visited[v-1] and visited[v]:
            new_result.append(final.pop(0)[-1])
        elif v-1 == 0 and visited[v-1]:
            new_result.append(final.pop(0)[-1])
        elif not visited[v]:
            new_result.append(contents[v])
    m_result = new_result[0]
    for i in range(1, len(new_result), 2):
        if new_result[i] == '+':
            m_result += new_result[i + 1]
        elif new_result[i] == '-':
            m_result -= new_result[i + 1]
        elif new_result[i] == '*':
            m_result *= new_result[i + 1]

    if m_result > f_result:
        f_result = m_result


N = int(input())
contents = [0]*N
temp = input()
for i in range(N):
    if i % 2:
        contents[i] = temp[i]
    else:
        contents[i] = int(temp[i])
f_result = contents[0]
for i in range(1, N, 2):
    if contents[i] == '+':
        f_result += contents[i+1]
    elif contents[i] == '-':
        f_result -= contents[i+1]
    elif contents[i] == '*':
        f_result *= contents[i+1]


calcul = []
for x in range(2, N, 2):
    if contents[x-1] == '+':
        calcul.append([x-2, x-1, x, contents[x-2]+contents[x]])
    elif contents[x-1] == '-':
        calcul.append([x-2, x-1, x, contents[x-2]-contents[x]])
    elif contents[x-1] == '*':
        calcul.append([x-2, x-1, x, contents[x-2]*contents[x]])



for m in range(1, (N+1)//4+1):
    result = []
    combination(0, 0, result)

print(f_result)