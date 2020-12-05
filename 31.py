import pprint
def solution(info, query):
    result = [0]*len(query)
    scores = [[0, {}] for _ in range(len(info))]

    for i in range(len(info)):
        info[i] = info[i].split(' ')
        scores[i][0] = int(info[i][-1])
        for x in range(4):
            scores[i][1][info[i][x]] = True

    scores = sorted(scores, key=lambda x: -x[0])
    pprint.pprint(scores)
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

        for score in scores:
            if score[0] < query[q][-1]:
                break

            if (score[1].get(query[q][0]) or query[q][0] == '-')\
                and (score[1].get(query[q][1]) or query[q][1] == '-')\
                    and (score[1].get(query[q][2]) or query[q][2] == '-') \
                    and (score[1].get(query[q][3]) or query[q][3] == '-'):
                result[q] += 1


    return result

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
