def solution(N, K):
    result = 0
    for x in range(3, 2**N, 3):
       t = bin(x)[2:].count('1')
       if t == K: result += 1
    return result

solution(3, 3)