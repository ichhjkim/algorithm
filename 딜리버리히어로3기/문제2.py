# %3 했는데, 나머지가 1이면 뒤에 끝은 22 // 나머지가 2면 그먄 제일 끝이 2

def solutions(S):
    S = S.replace(' ', '')
    S = S.replace('-', '')
    result = []
    if (len(S)%3) == 1:
        for num in range(len(S)//3):
            if num*3+3 == len(S)-1:
                result.append(S[num*3:num*3+2])
                result.append(S[num*3+2:])
                break
            else:
                result.append(S[num*3:num*3+3])
    elif (len(S)%3) == 2:
        for num in range(len(S)//3+1):
            result.append(S[num*3:num*3+3])
    else:
        for num in range(len(S)//3):
            result.append(S[num*3:num*3+3])

    result = '-'.join(result)
    return result

print(solutions('555372654'))