def solution(k, room_number):
    rooms = {}
    size = len(room_number)
    answer = [0]*size
    for s in range(size):
        num = room_number[s]
        if not rooms.get(num):
            rooms[num] = 1
            answer[s] = num

        else:
            temp = sorted(rooms)
            a = temp.index(num)
            for k in range(a+1, len(temp)):
                num += 1
                if num < temp[k]:
                    rooms[num] = 1
                    answer[s] = num
                    break
            else:
                num += 1
                rooms[num] = 1
                answer[s] = num

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))

# https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html