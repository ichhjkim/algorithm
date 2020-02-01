def solution(A, B):
    num = A*B
    n = bin(num)
    n = n[2:]
    result = n.count('1')
    return result

