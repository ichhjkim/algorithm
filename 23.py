import itertools

def solution(orders, course):
    answer = []
    menus = ''
    for order in orders: menus += order
    menus = list(set(menus))
    menus.sort()
    result = []
    for c in course:

        temp = []
        max_count = 0
        for combi in candidates:
            count = 0
            for order in orders:
                flag = True
                for com in combi:
                    if not com in order:
                        flag = False
                        break
                if flag:
                    count += 1

            if count >= 2:
                if count >= max_count:
                    max_count = count
                    temp.append([combi, count])
        for x in range(len(temp)):
            if temp[x][1] >= max_count:
                result.append(list(temp[x][0]))

    for x in range(len(result)):
        result[x] = ''.join(result[x])
    result = sorted(result)
    print(result)
    return result

def Combination(s, depth, visted, )