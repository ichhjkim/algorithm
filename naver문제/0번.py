import itertools

def solution(A):
    # t = [0]*depth
    for depth in range(len(A)-1, -1, -1):
        candis = list(itertools.combinations(A, depth))

        for can in candis:
            once = []
            for c in can:
                flag = True
                for i in c:
                    if i not in once:
                        once.append(i)
                    else:
                        flag = False
                        break
                if not flag:
                    break

            else:
                print(once)
                return len(once)

    return 0

print(solution(['potato', 'kayak', 'banana', 'racecar']))