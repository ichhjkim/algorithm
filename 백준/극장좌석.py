def backtrack(num):
    global count
    global fixed

    if num == f:
        count += 1

    else:
        for i in range(num-1, num+2):
            if i < 1 or i > N or seats[i]:
                continue
            else:
                seats[i] = 1
                backtrack(num+1)
                seats[i] = 0


N = int(input())

num_seat = int(input())
seats = [1]+[0]*(N)
fixed = []
for _ in range(num_seat):
    a = int(input())
    seats[a] = 1
    fixed += [a]

fixed += [N+1]
count = 0
result = 1
num = 1

for f in fixed:
    count = 0
    backtrack(num)
    result *= count
    num = f+1

print(result)





