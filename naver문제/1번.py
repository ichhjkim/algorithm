def solution(S):
    temp = list(S)
    result = [0]*len(temp)

    for i in range(len(temp)//2):
        if (temp[i]=="?") or (temp[len(temp)-1-i]=="?"):
            if temp[i] == temp[len(temp)-1-i]:
                result[i] = 'a'
                result[len(temp)-1-i] = 'a'
            elif temp[i] == "?":
                result[i] = temp[len(temp)-1-i]
                result[len(temp)-1] = result[i]
            elif temp[i] != "?":
                result[i] = temp[i]
                result[len(temp)-1-i] = temp[i]
        elif (temp[i]==temp[len(temp)-1-i]):
            result[i] = temp[i]
            result[len(temp)-1-i] = temp[i]
        else:
            return "NO"
    if len(temp) % 2:
        result[len(temp)//2] = S[len(temp)//2]

    return ''.join(result)

print(1, solution("?ab??a"))
print(2, solution('bab??a'))
print(3, solution('?a?'))