def solution(s):
    answer = 100000

    for i in range(1, (len(s)//2)+2):
        splited = []
        for j in range(len(s)//i+1):
            t = s[j*i:(j+1)*i]
            if t: splited.append(t)
        count = []

        letters = []
        for x in splited:
            if letters:
                if x != letters[-1]:
                    letters.append(x)
                    count.append(0)
                else:
                    count[-1] += 1
            else:
                letters.append(x)
                count.append(0)

        result = ''
        for c in range(len(count)):
            if count[c] > 0:
                result += str(count[c]+1) + letters[c]
            else:
                result += letters[c]
        if len(result) < answer:
            answer = len(result)

    return answer

test = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"
]
for t in test:
    print(solution(t))

