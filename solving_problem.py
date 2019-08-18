import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    count = int(input())
    pipe = list(map(int, input().split()))
    all_pipes = []
    for i in range(count):
        all_pipes.append(pipe[2 * i: 2 * i + 2])

    n = 0
    m = 0
    result = [all_pipes[0]]
    while len(result) < len(all_pipes):

        for i in range(1, len(all_pipes)):
            if all_pipes[n][0] == all_pipes[i][1]:
                result.insert(0, all_pipes[i])
                n = i
                break
            elif all_pipes[m][1] == all_pipes[i][0]:
                result.append(all_pipes[i])
                m = i
                break

    f_result = []
    for i in result:
        i = list(map(str, i))
        f_result.extend(i)

    print("#{} {}".format(tc, ' '.join(f_result)))