import time

def solution(N, K):
    result = 0
    for x in range(3, 2**N, 3):
       #t = bin(x).count('1')
       
       if t == K:
           result += 1

    return result

t = time.time()
print(solution(1125899906842624, 3))
print(time.time() - t)