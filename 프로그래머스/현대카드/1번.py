import datetime

def solution(purchase):
    answer = [0]*5
    answer[0] = 29
    time =datetime.datetime(2019, 1, 1)
    result = {}
    for i in range(365):
        t = time.strftime("%Y-%m-%d")
        time += datetime.timedelta(days=1)
        result[t] = 0

    for p in purchase:
        ps = p.split(' ')
        ps[0] = ps[0].replace('/', '-')
        result[ps[0]] += int(ps[1])

    rk = sorted(result.keys())
    prv = 0
    for x in range(len(rk)-29):
        t = 0
        for i in range(30):
            idx = x + i
            print(idx)
            t += result[rk[idx]]
        if t >= 0 and t < 10000:
            tv = 0
        elif t >= 10000 and t< 20000:
            tv = 1
        elif t >= 20000 and t < 50000:
            tv = 2
        elif t>= 50000 and t< 100000:
            tv = 3
        elif t >= 100000:
            tv = 4
        if tv == prv:
            answer[tv] += 1
            prv = tv
        else:
            answer[tv] += 1
            prv = tv
    return answer

print(solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]))