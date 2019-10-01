def finding(money):
    count = 0
    for i in range(N):
        t = coins[i]
        while money < K:
            if money + t > K:
                break
            elif money+t == K:
                count += 1
                return count
            else:
                money += t
                count += 1

        if money == K:
            return count


N, K = map(int, input().split())
coins = [0]*N
for i in range(N):
    coins[i] = int(input())

min_count = 100000000000000000000
# k원을 만드는데 필요한 동전 개수의 최솟값
coins.sort(reverse=True)
print(finding(0))

