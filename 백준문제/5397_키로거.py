# 백스페이스 '-'
# 커서 바로 앞에 글자가 존재하면, 그 글자를 지움,
# 화살표: <, >
# 커서 위치는 왼쪽/오른쪽으로 1만큼
# 나머지 문자는 비밀번호의 일부
#커서의 위치가 줄의 마지막이 아니면, 그 문자를 입력하고 커서는 오른쪽으로 한칸 이동
from collections import deque

t = int(input())

for i in range(t):
    pw = input()
    pwlength= len(pw)

    result = deque()
    cursor = 0
    for i in range(pwlength):
        print(result)
        if cursor < 0:
            cursor = 0
        t = pw[i]
        if t == '<' or t == '>':
            if result:
                if t =='>':
                    idx += 1
                else:
                    idx -= 1

        elif t=='-':
            if previous != '<' and previous != '>'  and previous != '-' and result:
                result.pop()
        else:
            result.insert(idx, t)
            idx += 1

        previous = t

    print(''.join(result))






