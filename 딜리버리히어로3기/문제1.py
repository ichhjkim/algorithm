import itertools

def solution(A, B, C, D):
     temp = [A, B, C, D]
     temp = set(itertools.permutations(temp))
     count = 0
     for t in temp:
         if t[0] < 2 and t[2] <= 6:
             count += 1
         elif t[0] == 2 and t[1] < 4 and t[2] <= 6:
             count += 1

     return count

print(solution(6, 2, 4, 7))