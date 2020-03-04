T = int(input())

for tc in range(1, T+1):

    t = input()

    result = t.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    print('{} {}'.format(tc, result))

    num = '23,920'
    num = num.split(',')
    num = ''.join(num)
    print(num)