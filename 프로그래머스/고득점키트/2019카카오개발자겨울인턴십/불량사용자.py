import itertools, copy
temp = []
num = 0
def solution(user_id, banned_id):
    global temp, num
    answer = 0
    temp_bans = {}
    for ban in banned_id:
        if temp_bans.get(ban):
            temp_bans[ban] += 1
        else:
            temp_bans[ban] = 1

    bans = []
    for k, v in temp_bans.items():`
        bans.append([v, k, []])
    visited = [0]*(len(user_id))
    for ui, user in enumerate(user_id):
        for bi, ban in enumerate(bans):
            if len(user) == len(ban[1]):
                for i in range(len(ban[1])):
                    if ban[1][i] == '*':
                        continue
                    elif user[i] != ban[1][i]:
                        break
                else:
                    bans[bi][2].append(user)

    result = []
    for ban in bans:
        t = itertools.combinations(ban[2], ban[0])
        result.append(list(t))

    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j] = list(result[i][j])

    comb(result, 0, [0]*len(result))

    #print(set(temp))
    return len(set(temp))

def comb(result, depth, final):
    global temp, num
    if depth == len(result):
        t = []
        for i in range(len(final)):
            for j in range(len(final[i])):
                if final[i][j] not in t:
                    t.append(final[i][j])
                else:
                    return

        if t not in temp:
            t.sort()
            temp.append(copy.deepcopy(tuple(t)))

    else:
        for i in range(len(result[depth])):
            final[depth] = result[depth][i]
            comb(result, depth+1, final)
            final[depth] = 0


user_id  =	["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
# 	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
# 	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])