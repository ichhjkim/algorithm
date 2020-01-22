A, B = input().split()

diff = len(B) - len(A)
min_result = 100


for d in range(diff+1):
    result = 0
    for a in range(len(A)):
        if B[d+a] != A[a]:
            result += 1

    if min_result > result:
        min_result = result


print(min_result)

