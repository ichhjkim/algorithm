first = list(input().split())
N = int(first[0])
arr_way = first[1]
max_sero = 0
arr = [0]*N
start = 0
def findstart(n):

    if arr_way == 'TOP':
        start = 0
    elif arr_way == 'MIDDLE':
        start = (max_sero-arr[n][1])//2
    elif arr_way == 'BOTTOM':
        start = (max_sero-arr[n][1])
    return start

for n in range(N):
    arr[n] = []
    num = list(input().split())
    arr[n].append(int(num[0]))
    arr[n].append(2*int(num[0])-1)
    for m in num[1]:
        arr[n].append(int(m))

    if arr[n][1] > max_sero:
        max_sero = arr[n][1]
result = [[] for _ in range(max_sero)]

def onefunc(n):
    start = findstart(n)
    for h in range(start, start+arr[n][1]):
        a = '.'*(arr[n][0]-1)+'#'
        result[h].append(a)

    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

def twofunc(n):
    start = findstart(n)
    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

    for h in range(start, start+arr[n][1]):
        if h == start or h == (start+ arr[n][1] + start - 1) // 2 or h == start + arr[n][1]-1:
            two = '#'*arr[n][0]
            result[h].append(two)
        elif h > start and h < (start+ arr[n][1] + start - 1) // 2:
            two = '.'*(arr[n][0]-1) + '#'
            result[h].append(two)
        elif h > (start+ arr[n][1] + start - 1) // 2 and h < start+arr[n][1]-1:
            two = '#' + '.'*(arr[n][0]-1)
            result[h].append(two)

def threefunc(n):
    start = findstart(n)
    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

    for h in range(start, start+arr[n][1]):
        if h == start or h == (start+ arr[n][1] + start - 1) // 2 or h == start+arr[n][1] - 1:
            three = '#' * arr[n][0]
            result[h].append(three)
        else:
            three = '.' * (arr[n][0] - 1) + '#'
            result[h].append(three)

def fourfunc(n):
    start = findstart(n)
    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

    for h in range(start, start+arr[n][1]):
        if h < (start+ arr[n][1] + start - 1) // 2:
            four = '#'+ '.'*(arr[n][0]-2) + '#'
            result[h].append(four)
        elif h == (start+ arr[n][1] + start - 1) // 2:
            four = '#'*(arr[n][0])
            result[h].append(four)
        elif h >(start+ arr[n][1] + start - 1) // 2:
            four = '.'*(arr[n][0]-1) + '#'
            result[h].append(four)

def fivefunc(n):
    start = findstart(n)
    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

    for h in range(start, start+arr[n][1]):
        if h == start or h == (start+ arr[n][1] + start - 1) // 2 or h == start + arr[n][1] - 1:
            five = '#' * arr[n][0]
            result[h].append(five)
        elif h > start and h < (start+ arr[n][1] + start - 1) // 2:
            five = '#' + '.' * (arr[n][0] - 1)
            result[h].append(five)

        elif h > (start+ arr[n][1] + start - 1) // 2and h < start+arr[n][1] - 1:
            five = '.' * (arr[n][0] - 1) + '#'
            result[h].append(five)

def sixfunc(n):
    start = findstart(n)
    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

    for h in range(start, start+arr[n][1]):

        if h < (start+ arr[n][1] + start - 1) // 2:
            six = '#' + '.' * (arr[n][0] - 1)
            result[h].append(six)
        elif h == (start+ arr[n][1] + start - 1) // 2 or h == start+arr[n][1]-1:
            six = '#'*arr[n][0]
            result[h].append(six)
        else:
            six = '#'+'.'*(arr[n][0]-2)+'#'
            result[h].append(six)

def sevenfunc(n):
    start = findstart(n)
    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

    for h in range(start, start+arr[n][1]):

        if h == start:
            seven = '#'*arr[n][0]
            result[h].append(seven)
        else:
            seven = '.'*(arr[n][0]-1) + '#'
            result[h].append(seven)

def eightfunc(n):
    start = findstart(n)
    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

    for h in range(start, start+arr[n][1]):
        if h == start or h == (start+ arr[n][1] + start - 1) // 2 or h == start+arr[n][1]-1:
            result[h].append('#'*arr[n][0])
        else:
            eight = '#' + '.'*(arr[n][0]-2) + '#'
            result[h].append(eight)

def ninefunc(n):
    start = findstart(n)
    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

    for h in range(start, start+arr[n][1]):
        if h == start or h == (start+ arr[n][1] + start - 1) // 2:
            result[h].append('#' * arr[n][0])
        elif h > start and h < (start+ arr[n][1] + start - 1) // 2:
            nine = '#' + '.'*(arr[n][0]-2)+'#'
            result[h].append(nine)
        else:
            nine = '.'*(arr[n][0]-1) + '#'
            result[h].append(nine)

def zerofunc(n):
    start = findstart(n)
    for u in range(0, start):
        result[u].append('.' * arr[n][0])

    for b in range(start+arr[n][1], max_sero):
        result[b].append('.'*arr[n][0])

    for h in range(start, start+arr[n][1]):
        if h == start or h == start+arr[n][1]-1:
            zero = '#'*arr[n][0]
            result[h].append(zero)
        else:
            zero = '#' + '.'*(arr[n][0]-2) + '#'
            result[h].append(zero)


for x in range(len(arr)):

    for y in range(2, len(arr[x])):
        if arr[x][y] == 1:
            onefunc(x)
        elif arr[x][y] == 2:
            twofunc(x)
        elif arr[x][y] == 3:
            threefunc(x)
        elif arr[x][y] == 4:
            fourfunc(x)
        elif arr[x][y] == 5:
            fivefunc(x)
        elif arr[x][y] == 6:
            sixfunc(x)
        elif arr[x][y] == 7:
            sevenfunc(x)
        elif arr[x][y] == 8:
            eightfunc(x)
        elif arr[x][y] == 9:
            ninefunc(x)
        elif arr[x][y] == 0:
            zerofunc(x)

for i in range(len(result)):
    print(' '.join(result[i]))