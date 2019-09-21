def product_line(product_num):
    global min_cost
    global cost
    global products

    if product_num == N:
        if cost < min_cost:
            min_cost = cost

    else:
        for i in range(N):

            if not factory[i]:
                factory[i] = 1
                cost += products[product_num][i]
                if cost < min_cost:
                    product_line(product_num+1)
                cost -= products[product_num][i]
                factory[i] = 0



T = int(input())

for tc in range(1, T+1):

    N = int(input())
    products = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 10000000000000000
    cost = 0
    factory = [0]*N
    product_num = 0
    product_line(product_num)

    print('#{} {}'.format(tc, min_cost))