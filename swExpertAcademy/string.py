import sys

sys.stdin = open('test_input.txt', 'r',  encoding='UTF8')

for t in range(10):
    tc = input()

    temp = input()

    result = input()
    aws = 0
    for i in range(len(result)):
        if result[i] == temp[0]:
            for s in range(1, len(temp)):
                if i+s < len(result) and result[i+s] != temp[s]:
                    break
                elif i+s == len(result):
                    break
            else:
                aws += 1

    print('#{} {}'.format(tc, aws))

