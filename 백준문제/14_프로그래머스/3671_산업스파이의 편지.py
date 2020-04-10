import itertools
c = int(input())

for _ in range(c):
    nums = input()
    count = 0
    max_len = len(nums)
    counts = []
    for i in range(1, max_len+1):
        num = list(itertools.permutations(nums, i))
        #print(num)

        for x in num:
            n = ''.join(x)
            n = int(n)
            #print(n)
            if n > 2:
                for dv in range(2, int(n**(1/2))+1):
                    if not n % dv:
                        break
                else:
                    if n not in counts:
                        counts.append(n)
                        count += 1
            elif n == 2 and (n not in counts):
                count += 1
                counts.append(n)


    print(count)



