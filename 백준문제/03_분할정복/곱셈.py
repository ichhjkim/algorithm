def power(A, B):
    global C
    if not B:
        return 1

    if not B % 2:
        newthing = power(A, B//2)
        return (newthing*newthing) % C
    else:
        newthing = power(A, (B-1)//2)
        return (newthing*newthing)*A % C

A, B, C = map(int, input().split())

if not A % C:
    print(0)
else:
    print(power(A, B))