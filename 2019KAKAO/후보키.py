
candis = []

def solution(relation):
    global candis
    answer = 0
    colums = len(relation[0])
    rows = len(relation)

    for i in range(1, colums+1):
        visited = [0]*colums
        comb(i, 0, 0, colums, visited)

    result = []
    for candi in candis:
        temp = []
        flag = False
        for res in result:
            rc = 0
            for r in res:
                if r in candi:
                    rc += 1
            if rc == len(res):
                flag = True
                break
        if flag: continue
        for rel in relation:
            rel_part = [0]*len(candi)
            c = 0
            for index in candi:
                rel_part[c] = rel[index]
                c += 1
            if rel_part not in temp:
                temp.append(rel_part)
            else:
                break
        if len(temp) == rows:
            result.append(candi)
    return len(result)

def comb(count, depth, s, e, visited):
    global candis
    if depth == count:
        temp = []
        for v in range(len(visited)):
            if visited[v]:
                temp.append(v)
        candis.append(temp)
    else:
        for i in range(s, e):
            if not visited[i]:
                visited[i] = depth+1
                comb(count, depth+1, i+1, e, visited)
                visited[i] = 0

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])


