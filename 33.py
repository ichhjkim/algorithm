import pprint
def solution(info, query):
    result = [0]*len(query)
    temp = [
        [[[[], []], [[], []]], [[[], []], [[], []]]],
        [[[[], []], [[], []]], [[[], []], [[], []]]],
        [[[[], []], [[], []]], [[[], []], [[], []]]],
    ]

    for i in range(len(info)):
        info[i] = info[i].split(' ')
        info[i][-1] = int(info[i][-1])
        if info[i][1] == 'backend':
            info[i][1] = 0
        else:
            info[i][1] = 1

        if info[i][2] == "junior":
            info[i][2] = 0
        else:
            info[i][2] = 1

        if info[i][3] == 'chicken':
            info[i][3] = 0
        elif info[i][3] == 'pizza':
            info[i][3] = 1

        if info[i][0] == 'java':
            info[i][0] = 0
        elif info[i][0] == 'python':
            info[i][0] = 1
        else:
            info[i][0] = 2

        temp[info[i][0]][info[i][1]][info[i][2]][info[i][3]].append(info[i][-1])

    for a in range(3):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    temp[a][b][c][d].sort(reverse=True)

    for q in range(len(query)):
        query[q] = query[q].split('and')
        my_query = query[q][-1].split(' ')

        query[q] += [0]
        query[q][-2] = my_query[1]
        query[q][-1] = my_query[2]
        if not query[q][-1] == '-':
            query[q][-1] = int(query[q][-1])

        for no in range(4):
            query[q][no] = query[q][no].replace(' ', '')
        search = [0]*5

        if query[q][0] == 'java': search[0] = [0]
        elif query[q][0] == 'python': search[0] = [1]
        elif query[q][0] == 'cpp': search[0] = [2]
        else: search[0] = [0, 1, 2]

        if query[q][1] == 'backend': search[1] = [0]
        elif query[q][1] == 'frontend': search[1] = [1]
        else: search[1] = [0, 1]

        if query[q][2] == 'junior': search[2] = [0]
        elif query[q][2] == 'senior': search[2] = [1]
        else: search[2] = [0, 1]

        if query[q][3] == 'chicken': search[3] = [0]
        elif query[q][3] == 'pizza': search[3] = [1]
        else: search[3] = [0, 1]

        if not query[q][-1] == '-':
            search[4] = query[q][-1]
        else:
            search[4] = 0
        for lan in range(len(search[0])):
            for po in range(len(search[1])):
                for job in range(len(search[2])):
                    for food in range(len(search[3])):
                        scores = temp[search[0][lan]][search[1][po]][search[2][job]][search[3][food]][:]

                        for score in scores:
                            if score >= search[4]:
                                result[q] += 1
                            else:
                                break

    return result
통과 (13.12ms, 10.5MB)

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])