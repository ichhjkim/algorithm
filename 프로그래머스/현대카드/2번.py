def solution(ip_addrs, langs, scores):
    answer = -1

    ip = {}

    for i in range(len(ip_addrs)):

        if ip.get(ip_addrs[i]):
            if langs[i][0] == "C":
                if ip[ip_addrs[i]]["C"].get(scores[i]):
                    ip[ip_addrs[i]]["C"][scores[i]]+= 1
                else:
                    ip[ip_addrs[i]]["C"][scores[i]] = 1
            else:
                if ip[ip_addrs[i]][langs[i]].get(scores[i]):
                    ip[ip_addrs[i]][langs[i]][scores[i]] += 1
                else:
                    ip[ip_addrs[i]][langs[i]][scores[i]] = 1


        else:
            ip[ip_addrs[i]] = {
                "C": {},
                "Java": {},
                "JavaScript": {},
                "Python3": {}
            }
            if langs[i][0] == "C":
                ip[ip_addrs[i]]["C"][scores[i]] = 1
            else:
                ip[ip_addrs[i]][langs[i]][scores[i]] = 1

    lgs = ["C, Java", "JavaScript", "Python3"]
    result = 0
    for k, v in ip.items():
        total = 0
        lg = [[] for _ in range(4)]
        idx = 0
        for lk, lv in ip[k].items():
            for sk, sv in ip[k][lk].items():
                if sv == 2:
                    lg[idx].append(2)
                else:
                    lg[idx].append(sv)
                total += sv
            idx += 1

        if total >= 4:
            result += total
        elif total == 3:
            flag = True
            for m in range(4):
                if sum(lg[m]) == 3:
                    if not flag: break
                    flag = False
                elif lg[m]:
                    if not flag: break
            else:
                if not flag:
                    result += 3
        elif total == 2:
            flag = True
            for m in range(4):
                if len(lg[m]) == 1 and lg[m][0]==2:
                    if not flag: break
                    flag = False
                elif lg[m]:
                    if not flag: break
            else:
                if not flag:
                    result += 2

    result = len(ip_addrs) - result
    if result:
        answer = result
    return answer

print(solution(["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111", "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"], ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"], [294, 197, 373, 45, 294, 62, 373, 373]))