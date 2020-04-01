while True:
    cases = list(map(int, input().split()))
    n = cases[0]

    if not n: break

    cases = cases[1:]

    max_result = 0

    for i in range(len(cases)):
        h = cases[i]
        st = h
        time = len(cases)-i
        num = 0
        flag = True
        for x in range(i+1, len(cases)):
            num += 1
            if st <= cases[x]:
                pass
            else:
                result = num*st
                st = cases[x]
                flag = False
                if max_result < result:

                    max_result = result
        if flag:
            result = h*time
            if max_result < result:
                max_result = result

    print(max_result)














