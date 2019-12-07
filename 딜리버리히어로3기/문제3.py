def solution(S):
    re = []
    r = []
    for s in S:
        if s not in r:
            r.append(s)
        else:
            re.append(''.join(r))
            r = [s]
    if r:
        re.append(''.join(r))
    return (len(re), re)



